from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
class UserTesting(APITestCase):
    def setUp(self):
        data = {
            "username":"1jash_upadhyay1",
            "password":"1123451",
            "confirm_password":"1123451",
            "email":"1test@xyz.com1"
        }
        self.client.post(reverse('create'),data)
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
    def delete_user_success(self):
        pass
    def delete_user_failure(self):
        pass