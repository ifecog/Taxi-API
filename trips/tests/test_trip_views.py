from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .test_user_views import create_user, PASSWORD

from trips.serializers.trip_serializers import *
from trips.models import Trip


class HttpTripTest(APITestCase):
    def setUp(self):
        user = create_user()
        response = self.client.post(reverse('user-login'), data={
            'email': user.email,
            'password': PASSWORD
        })
        self.access = response.data['access']
        
    def test_user_can_list_trips(self):
        trips = [
            Trip.objects.create(pickup_latitude=37.7749, pickup_longitude=-122.4194, dropoff_latitude=37.8072, dropoff_longitude=-122.4056),
            Trip.objects.create(pickup_latitude=37.8849, pickup_longitude=-122.6194, dropoff_latitude=37.9072, dropoff_longitude=-122.4156),
            # Trip.objects.create(pickup_address='B', dropoff_address='C')
        ]
        response = self.client.get(reverse('trip-trip-list'), HTTP_AUTHORIZATION=f'Bearer {self.access}')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        exp_trip_ids = [str(trip.id) for trip in trips]
        act_trip_ids = [trip['id'] for trip in response.data]
        self.assertCountEqual(exp_trip_ids, act_trip_ids)
        