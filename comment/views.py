import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Comment
from account.models import Account
from account.utils import login_decorator


class CommentView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            Comment.objects.create(
                author=request.user['email'],
                comment=dody['comment']
            )
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=403)

    @login_decorator
    def get(self, request):
        comment_data = Comment.objects.values()
        return JsonResponse({'comments': list(comment_data)}, status=200)
