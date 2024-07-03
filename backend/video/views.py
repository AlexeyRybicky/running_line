"""
В модуле содержиться логика отвечающая за создание видео с бегущей строкой,
и отображения списка вводимого текста
"""

import uuid

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from video.models import VideoText
from video.serializers import VideoTextSerializer
from video.utils import create_video


class UserTextView(APIView):
    """Класс представления для получения списка вводимого текста"""

    # pylint: disable=W0613
    def get(self, request):
        """получение списка вводимого текста"""
        texts = VideoText.objects.all()
        serializer = VideoTextSerializer(texts, many=True)
        return Response(serializer.data)


@csrf_exempt
def create_video_view(request):
    """Функция для обработки запросов на создание видео c бегущей строкой"""
    unique_video_suffix = str(uuid.uuid4())[:3]

    if request.method == 'POST':
        text = request.POST['text']
        VideoText.objects.create(text=text)
        video_file_path = create_video(text)
        with open(video_file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='video/mp4')
            response['Content-Disposition'] = (f'attachment; '
                                               f'filename="video{unique_video_suffix}.mp4"')
            return response
    return render(request, 'video.html')
