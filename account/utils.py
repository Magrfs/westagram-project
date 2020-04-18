import jwt
import json

from django.http import JsonResponse
from .models import Account

from westagram_project.settings import SECRET_KEY


def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        if 'Authorization' not in request.headers:
            return JsonResponse({"message": "INVALID_CLIENT_TOKEN"}, status=401)

        token = request.headers["Authorization"]

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms="HS256")
            user = Account.objects.get(id=data['id'])
            request.user = user

        except jwt.DecodeError:
            return JsonResponse({"message": "INVALID_TOKEN"}, status=401)
        except Account.DoesNotExist:
            return JsonResponse({"message": "UNKNOWN_USER"}, status=401)

        return func(self, request, *args, **kwargs)
    return wrapper
