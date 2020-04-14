from django.db import models
from account.models import Account # 연결하려고 했었는데 복잡해서 실패!


class Comment(models.Model):
    author = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
