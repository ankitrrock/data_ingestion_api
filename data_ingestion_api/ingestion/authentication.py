from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

API_KEY = 'mysecretkey'

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('API-KEY')
        if api_key != API_KEY:
            raise AuthenticationFailed('Invalid API Key')
        return (None, None)
