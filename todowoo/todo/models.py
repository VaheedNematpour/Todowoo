from django.contrib.auth.models import User
from django.db import models


class Todos(models.Model):
    title = models.CharField(max_length=256)
    memo = models.TextField(blank=True, null=True)
    important = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
