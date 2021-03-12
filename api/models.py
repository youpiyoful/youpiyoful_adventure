"""mapping of tables for api django app"""

from django.db import models
from django.db.models.deletion import CASCADE


class Post(models.Model):
    """Model of table post"""

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    body = models.TextField(blank=True, default="")
    owner = models.ForeignKey(
        "auth.User", related_name="posts", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created"]
