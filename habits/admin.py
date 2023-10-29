from django.contrib import admin

from habits.models import Habit, Nice_habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('action', 'period')


@admin.register(Nice_habit)
class Nice_habitAdmin(admin.ModelAdmin):
    list_display = ('action',)
