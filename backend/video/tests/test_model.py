"""В модуле содержаться тесты для модели базы данных VideoText"""

from django.db import transaction, DataError
from django.test import TestCase
from video.models import VideoText


# pylint: disable=missing-docstring
class VideoTextModelCreateTest(TestCase):
    def setUp(self):
        self.assertEqual(VideoText.objects.count(), 0)

    def test_simple_create(self):
        """Теста для проверки создания объекта в базе данных"""
        fake_text = "fake text"
        video = VideoText.objects.create(text=fake_text)
        self.assertEqual(VideoText.objects.count(), 1)

        video_db = VideoText.objects.get(pk=video.pk)
        self.assertEqual(video_db.text, fake_text)

    def test_too_big_length(self):
        """Тест для проверки не корректной длины текста"""
        with self.assertRaises(DataError):
            with transaction.atomic():
                VideoText.objects.create(text="t" * 253)
        self.assertEqual(VideoText.objects.count(), 0)

    def test_length_text(self):
        """Тест для проверки корректной длины текста"""
        VideoText.objects.create(text="t" * 250)
        self.assertEqual(VideoText.objects.count(), 1)


# pylint: disable=missing-docstring
class VideoTextModelTest(TestCase):
    def setUp(self):
        self.fake_text = "fake text"
        self.assertEqual(VideoText.objects.count(), 0)
        self.video = VideoText.objects.create(text="fake text")
        self.fake_text_db = VideoText.objects.get(pk=self.video.pk)

    # pylint: disable=W0212
    def test_text_blank(self):
        """Тест для проверки пустого значения"""
        blank = self.fake_text_db._meta.get_field("text").blank
        self.assertFalse(blank)

    # pylint: disable=W0212
    def test_text_unique(self):
        """Тест для проверки уникальности поля"""
        unique = self.fake_text_db._meta.get_field("text").unique
        self.assertFalse(unique)

    def test_str_method(self):
        """Тест для проверки __str__"""
        self.assertEqual(str(self.fake_text_db), self.fake_text)
