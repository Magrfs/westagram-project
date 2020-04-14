import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Comment
from account.models import Account


class CommentView(View):
    def post(self, request):
        data = json.loads(request.body) # 바디에 들어있던 제이슨을 딕셔너리로 데이터에 담는것
        try:
            Comment.objects.create(
                author=data['author'],
                comment=data['comment']
            )
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status=403)

    def get(self, request):
        comment_data = Comment.objects.values() # 쿼리셋이 출력된다. values 는 딕셔너리를 담고 있다.
        return JsonResponse({'comments': list(comment_data)}, status=200) # list로 담는 이유는? json이랑 가장 친한 형태가 딕셔너리이다. 그걸 리스트로 묶어서 보내주면 제이슨이 좋아하기 때문이다. 
        # 쿼리셋으로 줘야 추가 작업을 할 수 있기때문에 쿼리셋을 만들어 놓은것이다. 결과물이 다수가 올걸 가정했다는 의미이다.