from django.db import models


class Account(models.Model):
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts'
