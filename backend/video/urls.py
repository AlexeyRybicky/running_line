"""В модуле содержаться маршруты для приложения `user_selection`"""

from django.urls import path
from .views import UserTextView, create_video_view

# pylint: disable=C0103
app_name = 'video_text'

urlpatterns = [
    path('text_list/', UserTextView.as_view(), name='video_text'),
    path('create_video/', create_video_view, name='create_video'),
]
