from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import HttpRequest


class Notes (models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    done_date = models.DateTimeField("date done")
    is_done = models.BooleanField(default=False)
    owner_user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.title
