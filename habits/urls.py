from django.urls import path
from rest_framework.routers import DefaultRouter
from habits.apps import HabitsConfig
from habits.views import Nice_habitViewSet, HabitListView, HabitCreateView, HabitUpdateView, HabitRetrieveView, \
    HabitDestroyView, HabitPublicView

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r'nice', Nice_habitViewSet, basename='habits')

urlpatterns = [
    path('', HabitListView.as_view(), name='habit_list'),
    path('create/', HabitCreateView.as_view(), name='habit_create'),
    path('update/<int:pk>/', HabitUpdateView.as_view(), name='habit_update'),
    path('retrieve/<int:pk>/', HabitRetrieveView.as_view(), name='habit_retrieve'),
    path('destroy/<int:pk>/', HabitDestroyView.as_view(), name='habit_destroy'),
    path('public/', HabitPublicView.as_view(), name='public_habit'),
]+router.urls