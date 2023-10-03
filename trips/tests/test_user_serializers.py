from rest_framework.test import APITestCase

from trips.serializers.user_serializers import UserSerializer


class USerSerializersTest(APITestCase):
    
    def test_user_serializer_is_valid(self):
        data = {'name': 'Test Serializer'}
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid())