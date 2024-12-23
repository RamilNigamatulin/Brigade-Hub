from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from workers.models import Worker, Brigade
from workers.validators import WorkersValidator


class WorkerSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"

    def validate(self, data):
        """Проверяем валидность данных."""

        required_status = ["status"]
        for status in required_status:
            if status not in data:
                raise ValidationError(f"Поле '{status}' обязательно для заполнения.")

        WorkersValidator()(data)
        return data


class BrigadeSerializer(ModelSerializer):
    class Meta:
        model = Brigade
        fields = "__all__"


class BrigadeDetailSerializer(ModelSerializer):
    workers = WorkerSerializer(many=True, source='worker_set')

    class Meta:
        model = Brigade
        fields = ["id", "number", "specialization", "created_date", "workers",]


class WorkerDetailSerializer(ModelSerializer):
    brigade = BrigadeSerializer(many=True)

    class Meta:
        model = Worker
        fields = "__all__"
