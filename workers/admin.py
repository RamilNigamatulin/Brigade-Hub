from django.contrib import admin
from workers.models import Worker, Brigade


@admin.register(Worker)
class Worker(admin.ModelAdmin):
    list_filter = (
        "id",
        "surname",
        "name",
    )
    list_display = (
        "id",
        "surname",
        "name",
    )
    search_fields = ("title",)


@admin.register(Brigade)
class Brigade(admin.ModelAdmin):
    list_filter = (
        "id",
        "number",
        "specialization",
    )
    list_display = (
        "id",
        "number",
        "specialization",
    )
    search_fields = ("title",)
