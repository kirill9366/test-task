## Установка

Скопируйте данный репозиторий и перейдите в загруженную директорию.

Выполните следующие команды для запуска проекта

```sh
docker build -t test_task .
sudo docker run --publish 8000:8000 test_task
```

И перейдите по ссылке

```sh
127.0.0.1:8000
```
Документация к API:
https://app.swaggerhub.com/apis/kirill9366/test-task/1.0.0-oas3-oas3-oas3-oas3
