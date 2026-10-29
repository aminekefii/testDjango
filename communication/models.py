from django.conf import settings
from django.db import models


class Msg(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_msgs",
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_msgs",
    )

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"
