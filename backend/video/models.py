"""В модуле содержиться моделm базы данных для приложения `video`"""

from django.db import models


class VideoText(models.Model):
    text = models.TextField(
        max_length=250,
        blank=True,
        unique=False,
        help_text="Текст для видео",
    )

    def __str__(self):
        return self.text
