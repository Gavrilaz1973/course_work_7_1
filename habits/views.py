from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from habits.models import Nice_habit, Habit
from habits.pagination import HabitsPaginator
from habits.serializers import Nice_habitSerializer, HabitSerializer


class Nice_habitViewSet(ModelViewSet):
    queryset = Nice_habit.objects.all()
    serializer_class = Nice_habitSerializer
    # pagination_class = Nice_habitPaginator


class HabitCreateView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitListView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator


class HabitUpdateView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetrieveView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitPublicView(ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator
