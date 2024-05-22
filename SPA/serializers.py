from rest_framework import serializers

from SPA.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            "id",
            "action",
            "user",
            "place",
            "time",
            "is_pleasant",
            "frequency",
            "linked_habit",
            "reward",
            "action_time",
            "is_published",
        ]
        extra_kwargs = {"linked_habit": {"required": False}, "reward": {"required": False}}
        validators = []

    def validate(self, data):
        if data.get("is_pleasant"):
            if data.get("reward"):
                raise serializers.ValidationError("Приятная привычка не может иметь вознаграждение")
            elif data.get("linked_habit"):
                raise serializers.ValidationError("Приятная привычка не может иметь связанную привычку")
        else:
            if data.get("reward") is not None and data.get("linked_habit") is not None:
                raise serializers.ValidationError(
                    "Невозможно одновременно выбрать связанную привычку и вознаграждение"
                )
        return data

    def validate_action_time(self, value):
        if value > 120:
            raise serializers.ValidationError("Время выполнения должно быть не больше 120 секунд.")
        return value

    def validate_frequency(self, value):
        if value > 7:
            raise serializers.ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
        return value

    def validate_linked_habit(self, value):
        if value:
            if value.is_pleasant is False:
                raise serializers.ValidationError("Связанная привычка может быть только приятной")
            return value
