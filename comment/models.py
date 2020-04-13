from django.db import models
from account.models import Account


class Comment(models.Model):
    author = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
