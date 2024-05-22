from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user.models import User


class UserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="testor@mail.ru", password="123qwe456rty", is_staff=True)
        self.client.force_authenticate(user=self.user)

    def test_user_retrieve(self):
        url = reverse("user:user_detail", args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("email"), self.user.email)

    def test_user_create(self):
        url = reverse("user:user_register")
        data = {"email": "NEWtestor@mail.ru", "chat_id": "757575765", "password": "123qwe456rty"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)

    def test_user_update(self):
        url = reverse("user:user_update", args=(self.user.pk,))
        data = {"email": "NEWtestor@mail.ru", "chat_id": "757575765", "password": "123qwe456rty"}
        response = self.client.put(url, data)
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get("email"), "NEWtestor@mail.ru")

    def test_habit_delete(self):
        url = reverse("user:user_delete", args=(self.user.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)

    def test_user_list(self):
        url = reverse("user:users_list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 1)

    def tearDown(self):
        pass
