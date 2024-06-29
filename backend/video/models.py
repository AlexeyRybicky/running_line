"""В модуле содержиться моделm базы данных для приложения `video`"""

from django.db import models


class VideoText(models.Model):
    """Представляет модель для отображения текста на основе которого создавалось видео"""
    objects: models.Manager

    text = models.CharField(
        max_length=250,
        blank=False,
        unique=False,
        help_text="Текст для видео",
    )

    # pylint: disable=E0307
    def __str__(self):
        return self.text
