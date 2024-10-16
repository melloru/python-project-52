from django.db import models


class Users(models.Model):
    nickname = models.CharField(max_length=150)
    name = models.CharField(max_length=150, unique=True)
    surname = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)