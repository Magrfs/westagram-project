import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Account


class SignUpView(View):
    def post(self, request):
        signup_data = json.loads(request.body)
        try:
            # get()을 통해서 하면 execption을 피할수 없고 귀찮아진다. 그래서 필터 + exists를 쓴다.
            # 테이블에 존재하지 않는 객체를 호출하면(DB에서 호출하면) DOESNOTEXIST 에러가 난다.
            if Account.objects.filter(email=signup_data['email']).exists(): # exists()는 있으면 트루, 없으면 폴스. 내가 원하는 데이터가 실제로 있는지 없는지 할 때 exist를 쓴다.

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
            if Account.objects.filter(email=signin_data['email']).exists():
                user = Account.objects.get(email=signin_data['email']) # 이렇게 변수에 안담고 밑에 if문에서 비교할 때 확인해도 된다.

                if user.password == signin_data['password']:
                    return HttpResponse(status=200)

                return HttpResponse(status=401)

            return HttpResponse(status=400) # 계정 틀려도 401

        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)
