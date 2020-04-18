import json
import bcrypt
import jwt

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Account
from westagram_project.settings import SECRET_KEY
from .utils import login_decorator


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Account.objects.filter(email=data['email']).exists():
                return HttpResponse(status=409)
            hashed_password = bcrypt.hashpw(
                data['password'].encode('utf-8'), bcrypt.gensalt())
            Account.objects.create(
                email=data['email'],
                password=hashed_password.decode('utf-8'),
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

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode(
                        {'id': user.id}, SECRET_KEY, algorithm='HS256'
                    ).decode('utf-8')
                    return JsonResponse({"token:": token}, status=200)
                return HttpResponse(status=401)
            return HttpResponse(status=401)

        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)

#         access_token = request.headers.get('Authorization', None) # 헤더스에 기본으로 있는 공용키 Authorization
#         secret = SECRET_KEY
#         if access_token:
#             decode = jwt.decode(access_token, secret, algorithms="HS256")   # 더 철저하려면 알고리즘도 숨겨야한다. 순수하게 디코드에러는 페이로드 에러
#             user_id = decode.get("id", None)

#             request.user = user # 파이썬에서는 가변객체에서 동적으로 할당이 가능하다. 유저가 원래 없는게 가능하게 가능하다. 유저란 키를 주고 유저 객체를 넘겨준것이다.
