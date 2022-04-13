# TrackMarketplace
Это приложение для парсинга сайта __wildberries.ru__.
Пользователь может зарегистрироваться и начать отслеживать товар на сайте.

# Stack
* Python 3.10
* Django/DRF
* simple jwt token
* apsschedule
* postgres
* docker

# Как развернуть проект на сервер:
1. Убедитесь что на сервере установлены Python 3.10, docker 
и docker-compose.
2. Клонируйте репозиторий
    ```bash
    $ git clone https://github.com/NiKuma0/TrackMarketplace.git
    ```
3. Создайте файл `.env` как [здесь](.env_exaple)

4. Запустите docker-compose
    ```bash
    $ sudo docker-compose up
    ```
5. Примените миграции
    ```bash
    $ sudo docker-compose exec app python manage.py \
    migrate --settings app.settings.prod
    ```