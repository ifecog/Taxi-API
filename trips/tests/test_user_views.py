import base64
import json

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


PASSWORD = 'pAssw0rd'


def create_user(email='test@gmail.com', password=PASSWORD):
    User = get_user_model()
    return User.objects.create_user(
        first_name='test',
        last_name='user',
        email=email,
        phone_number='+2349087756534',
        password=password
    )


class AuthenticationTest(APITestCase):
    
    def test_user_can_sign_up(self):
        response = self.client.post(reverse('user-signup'), data={
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
        self.assertEqual(response.data['email'], user.email)
        self.assertEqual(response.data['phone_number'], user.phone_number)
        
    
    def test_user_can_login(self):
        user = create_user()
        response = self.client.post(reverse('user-login'), data={
            'email': user.email,
            'password': PASSWORD,
        }, format='json')
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        # ensure access and refresh tokens are in the response data
        self.assertIsNotNone(response.data.get('access'))
        self.assertIsNotNone(response.data.get('refresh'))
        
        # parse payload from access token
        access_token = response.data['access']
        header, payload, signature = access_token.split('.')
        decoded_payload = base64.b64decode(f'{payload}==')
        payload_data = json.loads(decoded_payload)
        # print(payload_data)
        
        self.assertEqual(payload_data['user_id'], user.id)
        
        