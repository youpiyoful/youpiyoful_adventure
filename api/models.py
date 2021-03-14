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


class Comment(models.Model):
    """
    The Comment model is similar to the Post model and has a many-to-one relationship
    with users through the owner field. A comment also has a many-to-one relationship
    with a single post through the post field.
    """

    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey(
        "auth.user", related_name="comments", on_delete=models.CASCADE
    )
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)

    class Meta:
        ordering = ["created"]
