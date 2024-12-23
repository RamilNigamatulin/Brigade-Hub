from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)

from rest_framework import filters
from workers.models import Worker, Brigade
from workers.paginations import WorkersPagination
from workers.serializers import (
    WorkerSerializer,
    BrigadeSerializer,
    WorkerDetailSerializer,
    BrigadeDetailSerializer,
)


class WorkerCreateAPIView(CreateAPIView):
    """Создаем нового работника."""

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerListAPIView(ListAPIView):
    """Выводим список рабочих."""

    queryset = Worker.objects.all().order_by("pk")
    serializer_class = WorkerSerializer
    pagination_class = WorkersPagination
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "surname",
        "name",
    ]


class WorkertUpdateAPIView(UpdateAPIView):
    """Редактируем работника."""

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerRetrieveAPIView(RetrieveAPIView):
    """Выводим одного работника."""

    queryset = Worker.objects.all()
    serializer_class = WorkerDetailSerializer


class WorkerDestroyAPIView(DestroyAPIView):
    """Удаляем работника."""

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class BrigadeCreateAPIView(CreateAPIView):
    """Создаем новую бригаду."""

    queryset = Brigade.objects.all()
    serializer_class = BrigadeSerializer


class BrigadeListAPIView(ListAPIView):
    """Выводим список бригад."""

    queryset = Brigade.objects.all().order_by("pk")
    serializer_class = BrigadeSerializer
    pagination_class = WorkersPagination


class BrigadeRetrieveAPIView(RetrieveAPIView):
    """Выводим одну бригаду."""

    queryset = Brigade.objects.all()
    serializer_class = BrigadeDetailSerializer


class BrigadeUpdateAPIView(UpdateAPIView):
    """Редактируем бригаду."""

    queryset = Brigade.objects.all()
    serializer_class = BrigadeSerializer


class BrigadeDestroyAPIView(DestroyAPIView):
    """Удаляем бригаду."""

    queryset = Brigade.objects.all()
    serializer_class = BrigadeSerializer
