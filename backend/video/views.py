"""
В модуле содержиться логика отвечающая за создание видео с бегущей строкой,
и отображения списка вводимого текста
"""

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import VideoText
from .serializers import VideoTextSerializer
from .utils import create_video


class UserTextView(APIView):
    """Класс представления для получения списка вводимого текста"""

    # pylint: disable=W0613
    def get(self, request):
        texts = VideoText.objects.all()
        serializer = VideoTextSerializer(texts, many=True)
        return Response(serializer.data)


def create_video_view(request):
    """Функция для обработки запросов на создание видео c бегущей строкой"""
    if request.method == 'POST':
        text = request.POST['text']
        VideoText.objects.create(text=text)
        create_video(text)
        return render(request, 'video.html', {'text': text})
    return render(request, 'video.html')
