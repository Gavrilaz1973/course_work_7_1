from rest_framework import serializers

from habits.models import Nice_habit, Habit
from habits.validators import Validate_sim, Validate_time


class Nice_habitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nice_habit
        fields = '__all__'


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [Validate_sim(field_1='related_habit', field_2='reward'),
                      Validate_time(field='time_to_act')]

    # def its_time(self, obj):
    #     send_habit_notification.delay(obj.pk)


# class HabitPublicSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Habit
#         fields = '__all__'
#         validators = [Validate_sim(field_1='related_habit', field_2='reward'),
#                       Validate_time(field='time_to_act')]