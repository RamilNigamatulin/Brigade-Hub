from django.db import models

NULLABLE = {"blank": True, "null": True}


class Brigade(models.Model):
    """Создание модели бригады."""

    class Specializations(models.TextChoices):
        FINISHING = "FIN", "Чистовая отделка"
        ROUGH_FINISH = "RF", "Черновая отделка"

    number = models.PositiveIntegerField(
        verbose_name="Номер бригады",
        help_text="Введите номер бригады",
        unique=True,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания записи",
        help_text="Дата создания записи заполняется автоматически",
    )
    specialization = models.CharField(
        max_length=100,
        choices=Specializations.choices,
        verbose_name="Специализация",
        help_text="Введите специализацию бригады",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Бригада"
        verbose_name_plural = "Бригады"

    def __str__(self):
        return self.name, self.specialization


class Worker(models.Model):
    """Создание модели рабочий."""

    class Status(models.TextChoices):
        WORKER = "WR", "Рабочий"
        FOREMAN = "FR", "Бригадир"
        SECTION_CHIEF = "SCH", "Прораб"

    surname = models.CharField(
        max_length=150,
        verbose_name="Фамилия рабочего",
        help_text="Введите фамилию рабочего",
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Имя рабочего",
        help_text="Введите имя рабочего",
    )
    patronymic = models.CharField(
        max_length=150,
        verbose_name="Отчество рабочего",
        help_text="Введите отчество рабочего",
        **NULLABLE,
    )
    brigade = models.ManyToManyField(
        Brigade,
        verbose_name="Бригада",
        help_text="Выберите бригаду",
        **NULLABLE,
    )
    wages = models.PositiveIntegerField(
        verbose_name="Зарплата рабочего",
        help_text="Введите заработную плату рабочего",
        **NULLABLE,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания записи",
        help_text="Дата создания записи заполняется автоматически",
    )
    status = models.CharField(
        max_length=50,
        choices=Status.choices,
        verbose_name="Статус рабочего",
        help_text="Выберите статус рабочего",
    )

    class Meta:
        verbose_name = "Рабочий"
        verbose_name_plural = "Рабочие"

    def __str__(self):
        return self.surname, self.name
