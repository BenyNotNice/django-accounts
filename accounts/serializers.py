from rest_framework import serializers
from django.core.validators import RegexValidator

class OTPRequestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'^09\d{9}$',
                message="Phone number must be 11 digits starting with 09."
            )
        ]
    )

class OTPVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'^09\d{9}$',
                message="Phone number must be 11 digits starting with 09."
            )
        ]
    )
    code = serializers.CharField(max_length=4, min_length=4)
