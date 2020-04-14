from django.db import models


class Account(models.Model):
    email = models.CharField(max_length=200) # 이메일은 전세계에서 유일하다. 데이터베이스에 저장될때도 그래야된다. unique=True 옵션을 추가해주자.
    password = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts'
