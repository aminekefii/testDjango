from django.conf import settings
from django.db import models


class Forum(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    forum = models.ForeignKey(
        Forum,
        on_delete=models.CASCADE,
        related_name="posts",
    )

    def __str__(self):
        return f"Post of {self.user} in {self.forum}"
