from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from SPA.models import Habit
from user.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="testor@mail.ru")
        self.client.force_authenticate(user=self.user)
        self.habit_1 = Habit.objects.create(
            action="TestHabit1",
            user=self.user,
            place="TestPlace",
            time="2024-05-22T00:00:00Z",
            is_pleasant=True,
            frequency=1,
            action_time=100,
        )
        self.habit_2 = Habit.objects.create(
            action="TestHabit2",
            user=self.user,
            place="TestPlace",
            time="2024-05-22T15:00:00Z",
            is_pleasant=False,
            linked_habit=self.habit_1,
            frequency=1,
            action_time=100,
            is_published=True,
        )

    def test_habit_retrieve(self):
        url = reverse("SPA:habit_detail", args=(self.habit_2.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit_2.action)

    def test_habit_create_1(self):
        url = reverse("SPA:create_habit")
        data = {
            "action": "TestHabit3",
            "place": "TestPlace2",
            "time": "2024-05-22T15:00:00Z",
            "is_pleasant": "false",
            "frequency": 1,
            "action_time": 100,
            "is_published": "true",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 3)

    def test_habit_create_2(self):
        url = reverse("SPA:create_habit")
        data = {
            "action": "TestHabit3",
            "place": "TestPlace2",
            "time": "2024-05-22T15:00:00Z",
            "is_pleasant": "true",
            "reward": "reward",
            "frequency": 1,
            "action_time": 100,
            "is_published": "true",
        }
        response = self.client.post(url, data)
        result = list(response.json().values())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result[0][0], "Приятная привычка не может иметь вознаграждение")

    def test_habit_create_3(self):
        url = reverse("SPA:create_habit")
        data = {
            "action": "TestHabit3",
            "place": "TestPlace2",
            "time": "2024-05-22T15:00:00Z",
            "is_pleasant": "true",
            "linked_habit": self.habit_1.pk,
            "frequency": 1,
            "action_time": 100,
        }
        response = self.client.post(url, data)
        result = list(response.json().values())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result[0][0], "Приятная привычка не может иметь связанную привычку")

    def test_habit_create_4(self):
        url = reverse("SPA:create_habit")
        data = {
            "action": "TestHabit3",
            "place": "TestPlace2",
            "time": "2024-05-22T15:00:00Z",
            "is_pleasant": "false",
            "linked_habit": self.habit_1.pk,
            "reward": "reward",
            "frequency": 1,
            "action_time": 100,
        }
        response = self.client.post(url, data)
        result = list(response.json().values())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result[0][0], "Невозможно одновременно выбрать связанную привычку и вознаграждение")

    def test_habit_create_5(self):
        url = reverse("SPA:create_habit")
        data = {
            "action": "TestHabit3",
            "place": "TestPlace2",
            "time": "2024-05-22T15:00:00Z",
            "is_pleasant": "false",
            "frequency": 10,
            "action_time": 100,
        }
        response = self.client.post(url, data)
        result = list(response.json().values())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result[0][0], "Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")

    def test_habit_create_6(self):
        url = reverse("SPA:create_habit")
        data = {
            "action": "TestHabit3",
            "place": "TestPlace2",
            "time": "2024-05-22T15:00:00Z",
            "is_pleasant": "false",
            "frequency": 7,
            "action_time": 200,
        }
        response = self.client.post(url, data)
        result = list(response.json().values())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(result[0][0], "Время выполнения должно быть не больше 120 секунд.")

    def test_habit_update(self):
        url = reverse("SPA:habit_update", args=(self.habit_2.pk,))
        data = {
            "action": "NEWTestHabit",
            "place": "NEWPlace",
            "time": "2024-05-22T15:00:00Z",
            "frequency": 7,
            "action_time": 20,
        }
        response = self.client.put(url, data)
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get("action"), "NEWTestHabit")
        self.assertEqual(result.get("place"), "NEWPlace")
        self.assertEqual(result.get("frequency"), 7)
        self.assertEqual(result.get("action_time"), 20)

    def test_habit_delete(self):
        url = reverse("SPA:habit_delete", args=(self.habit_1.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_user_list(self):
        url = reverse("SPA:user_habits")
        response = self.client.get(url)
        data = response.json().get("results")
        result = {
            "id": self.habit_1.pk,
            "action": self.habit_1.action,
            "user": self.user.pk,
            "place": self.habit_1.place,
            "time": self.habit_1.time,
            "is_pleasant": self.habit_1.is_pleasant,
            "frequency": self.habit_1.frequency,
            "linked_habit": self.habit_1.linked_habit,
            "reward": self.habit_1.reward,
            "action_time": self.habit_1.action_time,
            "is_published": self.habit_1.is_published,
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data[0], result)
        self.assertEqual(len(data), 2)

    def test_habit_published_list(self):
        self.user_1 = User.objects.create(email="testor_1@mail.ru")
        self.client.force_authenticate(user=self.user_1)
        url = reverse("SPA:published_habits")
        response = self.client.get(url)
        data = response.json().get("results")
        result = {
            "id": self.habit_2.pk,
            "action": self.habit_2.action,
            "user": self.user.pk,
            "place": self.habit_2.place,
            "time": self.habit_2.time,
            "is_pleasant": self.habit_2.is_pleasant,
            "frequency": self.habit_2.frequency,
            "linked_habit": self.habit_1.pk,
            "reward": self.habit_2.reward,
            "action_time": self.habit_2.action_time,
            "is_published": self.habit_2.is_published,
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data[0], result)
        self.assertEqual(len(data), 1)

    def tearDown(self):
        pass
