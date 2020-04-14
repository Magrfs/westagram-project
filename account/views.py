import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Account


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Account.objects.filter(email=data['email']).exists():
                return HttpResponse(status=409)

            Account.objects.create(
                email=data['email'],
                password=data['password'],
            )
            return HttpResponse(status=200)

        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)


class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if Account.objects.filter(email=data['email']).exists():
                user = Account.objects.get(email=data['email'])

                if user.password == data['password']:
                    return HttpResponse(status=200)
                return HttpResponse(status=401)
            return HttpResponse(status=401)

        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)
