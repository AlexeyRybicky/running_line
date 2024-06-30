"""В модуле содержаться тесты для представлений приложения `video`"""

from django.test import TestCase
from rest_framework.test import APIClient
from video.models import VideoText
from video.serializers import VideoTextSerializer


# pylint: disable=missing-docstring
class UserTextViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.texts = VideoText.objects.all()
        self.link = '/api/text_list/'

    def test_get_text_list(self):
        """Тест для проверки получения списка вводимого текста"""
        response = self.client.get(f'{self.link}')
        self.assertEqual(response.status_code, 200)
        serializer = VideoTextSerializer(self.texts, many=True)
        self.assertEqual(response.data, serializer.data)


# pylint: disable=missing-docstring
class CreateVideoViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.text_data = {'text': 'Test text'}
        self.link = '/api/create_video/'

    def test_create_video_view_post(self):
        """Тест для проверки создания видео при отправке POST запроса"""
        response = self.client.post(f'{self.link}', self.text_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(VideoText.objects.filter(text='Test text').exists())

    def test_create_video_view_get(self):
        """Тест для проверки отображения шаблона при GET запросе"""
        response = self.client.get(f'{self.link}')
        self.assertEqual(response.status_code, 200)
