
from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    thread_id = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.thread_id
