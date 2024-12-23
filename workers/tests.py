from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from workers.models import Brigade
from workers.models import Worker


class WorkerTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.brigade = Brigade.objects.create(number=1)
        self.worker = Worker.objects.create(surname="Иванов", name="Иван", status="WR")
        self.worker.brigade.add(self.brigade)
        self.client.force_authenticate(user=self.user)

    def test_worker_retrieve(self):
        url = reverse("workers:retrieve-workers", args=(self.worker.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.worker.name)

    def test_worker_create(self):
        url = reverse("workers:create-workers")
        data = {
            "surname": "Петров",
            "name": "Петр",
            "status": "WR",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Worker.objects.all().count(), 2)

    def test_worker_update(self):
        url = reverse("workers:update-workers", args=(self.worker.pk,))
        data = {
            "surname": "Сидоров",
            "name": "Петр",
            "status": "WR",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("surname"), "Сидоров")

    def test_worker_destroy(self):
        url = reverse("workers:delete-workers", args=(self.worker.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Worker.objects.all().count(), 0)

    def test_worker_list(self):
        url = reverse("workers:list-workers")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.worker.pk,
                    "surname": self.worker.surname,
                    "name": self.worker.name,
                    "patronymic": None,
                    "wages": None,
                    "created_date": self.worker.created_date.strftime(
                        "%Y-%m-%dT%H:%M:%S.%fZ"
                    ),
                    "status": self.worker.status,
                    "brigade": [self.brigade.pk],
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class BrigadeTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.brigade = Brigade.objects.create(number=1)
        self.worker = Worker.objects.create(surname="Иванов", name="Иван", status="WR")
        # self.worker.brigade.add(self.brigade)
        self.client.force_authenticate(user=self.user)

    def test_brigade_retrieve(self):
        url = reverse("workers:retrieve-brigades", args=(self.brigade.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("number"), self.brigade.number)

    def test_brigade_create(self):
        url = reverse("workers:create-brigades")
        data = {
            "number": 2,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Brigade.objects.all().count(), 2)

    def test_brigade_update(self):
        url = reverse("workers:update-brigades", args=(self.brigade.pk,))
        data = {"number": 3}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("number"), 3)

    def test_brigade_destroy(self):
        url = reverse("workers:delete-brigades", args=(self.brigade.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Brigade.objects.all().count(), 0)

    def test_brigade_list(self):
        url = reverse("workers:list-brigades")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.brigade.pk,
                    "number": self.brigade.number,
                    "created_date": self.brigade.created_date.strftime(
                        "%Y-%m-%dT%H:%M:%S.%fZ"
                    ),
                    "specialization": None,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
