from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


PASSWORD = 'pAssw0rd'


class AuthenticationTest(APITestCase):
    
    def test_user_can_sign_up(self):
        response = self.client.post(reverse('sign-up'), data={
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@gmail.com',
            'phone_number': '+2349087746532',
            'password': PASSWORD,
            'confirm_password': PASSWORD,
        })
        
        User = get_user_model()
        user = User.objects.last()
        
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['first_name'], user.first_name)
        self.assertEqual(response.data['last_name'], user.last_name)
        self.assertEqual(response.data['email'], user.email)
        self.assertEqual(response.data['phone_number'], user.phone_number)
        