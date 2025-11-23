from django.urls import path
from .views import RequestOTPView, VerifyOTPView, index_view, login_view, dashboard_view

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('api/auth/send-otp/', RequestOTPView.as_view(), name='send-otp'),
    path('api/auth/verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
]
