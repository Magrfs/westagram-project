import json

from django.views import View
from django.http import HttpResponse, JsonResponse

import .models import Account


class SignUpView(View):
    def post(self, request):
        signup_data = json.loads(request.body)
        try:
            if Account.objects.filter(email=signup_data['email']).exists():
                return HttpResponse(status=409)

            Account.objects.create(
                email=signup_data['email'],
                password=signup_data['password'],
            )
            return HttpResponse(status=200)

        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)


class SignInView(View):
    def post(self, request):
        signin_data = json.loads(request.body)

        try:
            if Account.objects.filter(email=signin_data['email']).exist():
                user = Account.objects.get(email=signin_data['email'])

                if user.password == signin_data['password']:
                    return HttpResponse(status=200)

        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)
