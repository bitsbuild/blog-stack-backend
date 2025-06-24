from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
class UserTesting(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="1jashupadhyay1",password="1123451",email="1jashupadhyay.java@gmail.com1")
    def test_create_user_success(self):
        data = {
            "username":"jash_upadhyay",
            "password":"12345",
            "confirm_password":"12345",
            "email":"test@xyz.com"
        }
        response = self.client.post(reverse('create'),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_create_user_failure_passwords_did_not_match(self):
        data = {
            "username":"jash_upadhyay",
            "password":"12345",
            "confirm_password":"123456",
            "email":"test@xyz.com"
        }
        response = self.client.post(reverse('create'),data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
    def test_create_user_failure_repeat_email(self):
        data = {
            "username":"jash_upadhyay",
            "password":"12345",
            "confirm_password":"12345",
            "email":"1test@xyz.com1"
        }
        response = self.client.post(reverse('create'),data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
    def test_create_user_failure_repeat_username(self):
        data = {
            "username":"1jash_upadhyay1",
            "password":"12345",
            "confirm_password":"12345",
            "email":"1test@xyz.com1"
        }
        response = self.client.post(reverse('create'),data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
    def test_delete_user_success(self):
        token = Token.objects.get(user__username='1jashupadhyay1')
        self.client.credentials(HTTP_AUTHORIZATION='Token '+str(token.key))
        response = self.client.post(reverse('delete'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_delete_user_failure(self):
        token = ''
        self.client.credentials(HTTP_AUTHORIZATION='Token '+token)
        response = self.client.post(reverse('delete'))
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)