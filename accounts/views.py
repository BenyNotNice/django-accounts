from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import OTPRequestSerializer, OTPVerifySerializer
from .services import KavehnegarAPI, OTPService

User = get_user_model()

class OTPRateThrottle(AnonRateThrottle):
    rate = '3/m'  # 3 requests per minute

@method_decorator(csrf_exempt, name='dispatch')
class RequestOTPView(APIView):
    throttle_classes = [OTPRateThrottle]

    def post(self, request):
        serializer = OTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            
            # Generate and Cache OTP
            code = OTPService.generate_otp()
            OTPService.cache_otp(phone_number, code)
            
            # Send SMS
            kavehnegar = KavehnegarAPI()
            try:
                # In production, you might want to run this asynchronously (Celery)
                kavehnegar.verify_lookup(receptor=phone_number, token=code)
            except Exception as e:
                # Log the error and OTP for development
                import logging
                logger = logging.getLogger(__name__)
                logger.error(f"SMS Service Error: {e}")
                logger.warning(f"Development Mode - OTP for {phone_number}: {code}")
                
                # In development, continue even if SMS fails
                # In production, you might want to return an error
                from django.conf import settings
                if not settings.DEBUG:
                    return Response(
                        {"error": "SMS Service Unavailable"},
                        status=status.HTTP_503_SERVICE_UNAVAILABLE
                    )
            
            return Response(
                {"message": "OTP sent successfully"},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class VerifyOTPView(APIView):
    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            code = serializer.validated_data['code']
            
            if OTPService.verify_otp(phone_number, code):
                user, created = User.objects.get_or_create(phone_number=phone_number)
                
                if not user.is_active:
                     return Response(
                        {"error": "User account is disabled."},
                        status=status.HTTP_403_FORBIDDEN
                    )

                refresh = RefreshToken.for_user(user)
                
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'is_new_user': created
                }, status=status.HTTP_200_OK)
            
            return Response(
                {"error": "Invalid or expired OTP"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index_view(request):
    return render(request, 'accounts/index.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def dashboard_view(request):
    # Get phone number from query params (passed from login)
    phone_number = request.GET.get('phone', 'کاربر')
    is_new_user = request.GET.get('new', 'false') == 'true'
    
    context = {
        'phone_number': phone_number,
        'is_new_user': is_new_user,
    }
    return render(request, 'accounts/dashboard.html', context)

