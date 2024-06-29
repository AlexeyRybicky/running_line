"""В модуле содержиться приложения"""

from django.apps import AppConfig


class VideoConfig(AppConfig):
    """Настройки приложения `video`"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'video'
