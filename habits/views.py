from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habits.models import Nice_habit, Habit
from habits.pagination import HabitsPaginator
from habits.permissions import IsOwnerOrStaff
from habits.serializers import Nice_habitSerializer, HabitSerializer


class Nice_habitViewSet(ModelViewSet):
    queryset = Nice_habit.objects.all()
    serializer_class = Nice_habitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class HabitCreateView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrStaff]


class HabitListView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator
    permission_classes = [IsAuthenticated, IsOwnerOrStaff]


class HabitUpdateView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrStaff]


class HabitRetrieveView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrStaff]


class HabitDestroyView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrStaff]


class HabitPublicView(ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitsPaginator
    permission_classes = [IsAuthenticatedOrReadOnly]
