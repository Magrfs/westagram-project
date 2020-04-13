import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Comment
from account.models import Account


class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)
        Comment.objects.create(
            author=data['author'],
            comment=data['comment']
        )
        return HttpResponse(status=200)

    def get(self, request):
        comment_data = Comment.objects.values()
        return JsonResponse({'comments': list(comment_data)}, status=200)
