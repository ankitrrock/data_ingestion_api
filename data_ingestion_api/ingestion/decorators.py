from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def validate_request():
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            # Check for API-KEY in headers
            api_key = request.headers.get('API-KEY')
            if not api_key:
                return Response(
                    {"error": "'API-KEY' header is required."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Check for 'file' in form-data
            if 'file' not in request.FILES or not request.FILES['file']:
                return Response(
                    {"error": "'file' is required in form-data."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # If payload is valid, proceed to the actual function
            return func(self, request, *args, **kwargs)
        return wrapper
    return decorator
