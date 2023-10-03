from rest_framework.test import APITestCase

from trips.serializers.user_serializers import UserSerializer


class USerSerializersTest(APITestCase):
    
    def test_user_serializer_is_valid(self):
        data = {
            'name': 'Test Serializer',
            'email': 'test@example.com',
            'password': 'mysecretpassword',
            'confirm_password': 'mysecretpassword',
        }
        serializer = UserSerializer(data=data)
        # if not serializer.is_valid():
        #     print(serializer.errors)  # Print validation errors
        #     print(serializer.data)
        self.assertTrue(serializer.is_valid())