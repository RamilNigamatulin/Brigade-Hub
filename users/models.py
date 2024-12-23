from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    first_name = models.CharField(
        max_length=30,
        verbose_name="Имя пользователя",
        help_text="Введите имя пользователя",
        **NULLABLE,
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия пользователя",
        help_text="Введите фамилию пользователя",
        **NULLABLE,
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="Телефон",
        help_text="Введите номер телефона",
        **NULLABLE,
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
        help_text="Введите адрес электронной почты",
        unique=True,
    )
    image = models.ImageField(
        verbose_name="Изображение профиля",
        help_text="Загрузите изображение профиля",
        upload_to="photo/users/",
        **NULLABLE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
