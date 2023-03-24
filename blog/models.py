from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Commentary(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="commentaries"
    )
    created_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Commentaries"