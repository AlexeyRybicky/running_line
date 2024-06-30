# Инструкция по запуску

1. Скачать репозиторий выполнив команду:
```shell
git clone https://github.com/AlexeyRybicky/running_line.git
```

2. Перейдите в скаченый каталог
3. Создайте файл с переменными окружения(.env)  для работы проекта, за образец возьмите содержимое файла .env.template
4. Что бы запустить проект с помощью Docker выполните команду:
```shell
docker compose -f docker-compose.yml up --build
```
5. Для генерации ведео перейдите по адресу http://localhost:8000/api/create_video/
6. Для просмотра введенных запросов перейдите по адресу http://localhost:8000/api/text_list/
7. Для прогона тестов зайдите в Docker контейнер выполнив команду
```shell
docker exec -it running_line-app-1 /bin/bash
```
8. Внутри контейнера выполните команду:
```shell
python manage.py test
```