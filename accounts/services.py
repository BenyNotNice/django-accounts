import requests
import random
import logging
from django.core.cache import cache
from django.conf import settings
from rest_framework.exceptions import APIException

logger = logging.getLogger(__name__)

class KavehnegarAPI:
    def __init__(self):
        self.api_key = getattr(settings, 'KAVEHNEGAR_API_KEY', '')
        self.base_url = f"https://api.kavenegar.com/v1/{self.api_key}/verify/lookup.json"

    def verify_lookup(self, receptor, token, template='verify'):
        if not self.api_key:
            logger.warning("Kavehnegar API Key is missing.")
            # In development, you might want to bypass this or raise error
            # return False 
        
        params = {
            'receptor': receptor,
            'token': token,
            'template': template
        }
        try:
            response = requests.post(self.base_url, data=params, timeout=5)
            response.raise_for_status()
            result = response.json()
            return result
        except requests.RequestException as e:
            logger.error(f"Kavehnegar Service Error: {e}")
            raise APIException("SMS Service Unavailable")

class OTPService:
    @staticmethod
    def generate_otp():
        return str(random.randint(1000, 9999))

    @staticmethod
    def cache_otp(phone_number, code):
        key = f"otp_{phone_number}"
        cache.set(key, code, timeout=120) # 120 seconds expiry

    @staticmethod
    def verify_otp(phone_number, code):
        key = f"otp_{phone_number}"
        cached_code = cache.get(key)
        if cached_code == code:
            cache.delete(key) # Invalidate after use
            return True
        return False
