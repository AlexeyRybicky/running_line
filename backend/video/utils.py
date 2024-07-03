"""В модуле содержиться скрипт для создания видео"""

import tempfile

import cv2
import numpy as np


# pylint: disable=R0914
# pylint: disable=E1101
# pylint: disable=R1732
def create_video(text):
    """
    Создает видео с заданным текстом.

    Аргументы:
        text: Текст, который будет отображаться в видео.

    Возвращает:
       video_file_path: путь к созданному видеофайлу
    """

    # Основные настройки для создания видео
    fps = 30
    seconds = 3
    frame_count = fps * seconds

    width, height = 640, 480
    # создание временного файла, будет удален после закрытия
    video_file_path = tempfile.NamedTemporaryFile(suffix='.mp4').name
    video = cv2.VideoWriter(
        video_file_path,
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

    if text_size[0] < width // 2:
        dx, dy = -(width // 2) // frame_count, 0

    # Cоздание последовательности кадров для видео.
    for _ in range(frame_count):  # 3 seconds
        img = np.zeros((height, width, 3), np.uint8)
        cv2.putText(img, text, (x, y), font, font_scale, color, font_thickness)
        video.write(img)

        # обновление позиции текста
        x += dx
        y += dy

    video.release()
    return video_file_path
