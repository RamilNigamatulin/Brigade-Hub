from django.urls import path

from workers.apps import WorkersConfig
from workers.views import (
    WorkerCreateAPIView,
    WorkerListAPIView,
    WorkerDestroyAPIView,
    WorkertUpdateAPIView,
    WorkerRetrieveAPIView,
    BrigadeCreateAPIView,
    BrigadeDestroyAPIView,
    BrigadeUpdateAPIView,
    BrigadeListAPIView,
    BrigadeRetrieveAPIView,
)

app_name = WorkersConfig.name

urlpatterns = [
    path("workers/", WorkerListAPIView.as_view(), name="list-workers"),
    path("workers/create/", WorkerCreateAPIView.as_view(), name="create-workers"),
    path("workers/<int:pk>/", WorkerRetrieveAPIView.as_view(), name="retrieve-workers"),
    path(
        "workers/<int:pk>/delete/",
        WorkerDestroyAPIView.as_view(),
        name="delete-workers",
    ),
    path(
        "workers/<int:pk>/update/",
        WorkertUpdateAPIView.as_view(),
        name="update-workers",
    ),
    path("brigades/", BrigadeListAPIView.as_view(), name="list-brigades"),
    path("brigades/create/", BrigadeCreateAPIView.as_view(), name="create-brigades"),
    path(
        "brigades/<int:pk>/", BrigadeRetrieveAPIView.as_view(), name="retrieve-brigades"
    ),
    path(
        "brigades/<int:pk>/delete/",
        BrigadeDestroyAPIView.as_view(),
        name="delete-brigades",
    ),
    path(
        "brigades/<int:pk>/update/",
        BrigadeUpdateAPIView.as_view(),
        name="update-brigades",
    ),
]
