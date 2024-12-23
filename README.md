## Описание проекта

Brigade Hub  — это Backend-часть.

Он разработан с использованием Django и Django REST Framework. 

## Требования

- Python 3.12
- PostgreSQL

## Установка
1. Клонируйте репозиторий: https://github.com/RamilNigamatulin/Brigade-Hub.git
2. Создайте виртуальное окружение и активируйте его:
    ```
    python -m venv venv
    ```
    ```
    source venv/bin/activate
    ```
3. Переименуйте файл ".env.sample" в ".env" и заполните его.
Для генерации SECRET_KEY введите в консоль команду: 
    ```
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```
4. Установите зависимости командой: 
    ```
    pip install -r requirements.txt
    ```
5. Запустите проект:
    ```
    python manage.py runserver
    ```
6. Для тестирования проекта возможно использования подготовленных фикстур, для их загрузки введите команду:
    ```
    python manage.py loaddata fixtures/general.json
    ```
    или по отдельности: 
    ```
    python manage.py loaddata fixtures/workers.json
    ```
    ```
    python manage.py loaddata fixtures/users.json
    ```
- Пароль для всех пользователей 123qwe.
7. Для использования чистой базы и настройки администратора, внесите соответствующие изменения в файл "csu.py" (логин и пароль администратора, по умолчанию "email=admin@example.com, password=123qwe") и введите команду: 
    ```
    python manage.py csu
    ```
## Эндпоинты

- **Авторизация и аутентификация**:
  - Регистрация пользователя
    ```
    POST /users/register/
    ``` 
    ```
    {
      "email": "user@example.ru",
      "password": "example"
    }
    ```
  - Получение токена
    ```
    POST /users/token/
    ``` 
    ```
    {
      "email": "user@example.ru",
      "password": "example"
    }
    ```
  - Обновление токена
    ```
    POST /users/token/refresh/
    ```
    ```
    {
      "email": "user@example.ru",
      "password": "example"
    }
    ```
  
- **Сотрудники**:
    CRUD для сотрудников
  - Список сотрудников
    ```
    GET /workers/
    ``` 
  - Создание сотрудника
    ```
    POST /workers/create/
    ``` 
    ```
    {
      "surname": "example",
      "name": "example",
      "status": ("WR" or "FR" or "SCH"
    }
    ```
  - Детальная информация о сотруднике
    ```
    GET /workers/<int:id>/
    ```
  - Редактирование сотрудника
    ```
    PUT /workers/<int:id>/update/
    ```
    ```
    {
      "surname": "example",
      "name": "example",
      "status": ("WR" or "FR" or "SCH")
    }
    ```
  - Удаление сотрудника
    ```
    DELETE /workers/<int:id>/delete/
    ```

- **Бригады**:
    CRUD для бригады
  - Список бригад
    ```
    GET /brigades/
    ``` 
  - Создание бригады
    ```
    POST /brigades/create/
    ``` 
    ```
    {
      "number": "example"
    }
    ```
  - Детальная информация о бригаде
    ```
    GET /brigades/<int:id>/
    ```
  - Редактирование бригады
    ```
    PUT /brigades/<int:id>/update/
    ```
    ```
    {
      "number": "example"
    }
    ```
  - Удаление бригады
    ```
    DELETE /brigades/<int:id>/delete/
    ```
  - Список отзывов конкретного объявления
    ```
    GET reviews/advertisement/<int:advertisement_id>/
    ```
    
- **Поиск**:
  - Поиск сотрудников по имени или фамилии
    ```
    GET /workers?search=example
    ``` 
    
- **Тестирование**:
    
  ```
  coverage run --source='.' manage.py test
  ```
  ```
  coverage report -m
  ```
    Тестами покрыто 97% кода