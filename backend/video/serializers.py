"""В модуле содержится сериализатор для приложения `video`"""

from django.apps import apps
from rest_framework import serializers


class VideoTextSerializer(serializers.ModelSerializer):
    """Сериализатор для модели `VideoText`"""

    # pylint: disable=missing-docstring
    class Meta:
        model = apps.get_model('video', 'VideoText')
        fields = '__all__'
