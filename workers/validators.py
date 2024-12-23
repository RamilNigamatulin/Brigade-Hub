from rest_framework.serializers import ValidationError


class WorkersValidator:

    def __call__(self, data):
        self.validate_status(data)

    def validate_status(self, data):
        """Рабочий не может быть больше чем в одной бригаде."""

        status = data.get("status")
        brigades = data.get("brigade", [])

        if status == "WR" and len(brigades) > 1:
            raise ValidationError("Рабочий не может быть больше чем в одной бригаде.")
