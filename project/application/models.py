from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Users(models.Model):
    fullname = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=True )
    user_role = models.IntegerField(default=1)
    created_on = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.email
