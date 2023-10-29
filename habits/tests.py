from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email="test@sky.pro", is_superuser=True, is_staff=True)
        self.client.force_authenticate(user=self.user)


    def test_create_habit(self):
        '''Тестирование создания привычки'''
        data = {
            "place": "test",
            "action": "test",
            "period": "daily",
            "time_to_act": "100"
        }

        response = self.client.post('/habits/create/', data=data)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {
                'id': 1,
                'place': 'test',
                'time': None,
                'action': 'test',
                'period': 'daily',
                'reward': None,
                'time_to_act': 100,
                'is_public': False,
                'user': None,
                'related_habit': None
            }
        )
        self.assertTrue(
            Habit.objects.all().exist()
        )


    def test_list_habit(self):

        """ Тестирование вывода списка привычек"""
        response = self.client.get('/habits/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_lesson(self):
        """ Тестирование удаления привычки"""
        Habit.objects.create(
            place="test",
            action="test",
            period="daily",
            time_to_act=100
        )
        response = self.client.delete('/habits/destroy/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_lesson(self):
        """ Тестирование изменения привычки"""
        Habit.objects.create(
            place="test",
            action="test",
            period="daily",
            time_to_act="100"
        )
        response = self.client.patch('/habits/update/3/', {"time_to_act": "50"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_public_habit(self):
        """ Тестирование вывода списка публичных привычек"""
        response = self.client.get('/habits/public/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)