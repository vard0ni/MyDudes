# MyDudes
Жизнь лучше симуляции!

### Инструменты разработки

**Стек:**
- Python >= 3.8
- Django Rest Framework
- Postgres

## Старт

#### 1) Создать образ

    docker-compose build

##### 2) Запустить контейнер

    docker-compose up
    
##### 3) Перейти по адресу

    http://127.0.0.1:8000/api/v1/swagger/

## Разработка с Docker

##### 1) Сделать форк репозитория

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) В корне проекта создать .env.dev

    DEBUG=1
    SECRET_KEY=
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    
    # Data Base
    POSTGRES_DB=
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DATABASE=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_HOST=
    POSTGRES_PORT=5432
    DATABASE=postgres
    
##### 4) Создать образ

    docker-compose build

##### 5) Запустить контейнер

    docker-compose up
    
##### 6) Создать суперюзера

    docker exec -it pysonet_pysonet_back_1 python manage.py createsuperuser
                                                        
##### 7) Если нужно очистить БД

    docker-compose down -v
