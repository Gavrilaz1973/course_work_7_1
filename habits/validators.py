from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from habits.models import Habit


class Validate_sim():
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2

    def __call__(self, value):
        field_vol_1 = dict(value).get(self.field_1)
        field_vol_2 = dict(value).get(self.field_2)
        if field_vol_1 and field_vol_2:
            raise serializers.ValidationError("Не использовать связянную привычку и вознаграждение.")


class Validate_time():
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time_to_act = dict(value).get(self.field)
        if time_to_act > 120:
            raise serializers.ValidationError("Время на выполнение не больше 120 сек.")