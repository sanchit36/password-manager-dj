from django.db import models
from django.contrib.auth.models import User
from .utils import encrypt_user_data


class Site(models.Model):
    user = models.ForeignKey(User, on_delete=models.CharField)
    name = models.CharField(max_length=255)
    password = models.TextField()

    def save(self, *args, **kwargs):
        self.password = encrypt_user_data(
            self.user.username, self.user.password, self.password)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
