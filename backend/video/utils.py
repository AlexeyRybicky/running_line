"""В модуле содержиться скрипт для создания видео"""

import uuid

import cv2
import numpy as np


# pylint: disable=R0914
# pylint: disable=E1101
def create_video(text):
    """
    Создает видео с заданным текстом.

    Аргументы:
        text: Текст, который будет отображаться в видео.

    Возвращает:
        None
    """

    # Основные настройки для создания видео
    fps = 30
    seconds = 3
    frame_count = fps * seconds
    unique_video_suffix = str(uuid.uuid4())[:3]

    width, height = 640, 480
    video = cv2.VideoWriter(
        f'video_{unique_video_suffix}.mp4',
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps, (width, height)
    )

    # Настройки шрифта, поддерживает кириллицу
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 12
    font_thickness = 4
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    color = (255, 255, 255)

    # Настройки позиции
    x, y = width, (height + text_size[1] // 2) // 2  # Начальная позиция текста
    dx, dy = -text_size[0] // frame_count, 0  # направление движения текста

    # Cоздание последовательности кадров для видео.
    for _ in range(frame_count):  # 3 seconds
        img = np.zeros((height, width, 3), np.uint8)
        cv2.putText(img, text, (x, y), font, font_scale, color, font_thickness)
        video.write(img)

        # обновление позиции текста
        x += dx
        y += dy

    video.release()
