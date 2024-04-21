from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from .test_user_views import create_user, PASSWORD

from trips.serializers.trip_serializers import *
from trips.models import Trip


def create_first_trip():
    return Trip.objects.create(pickup_latitude=37.7749, pickup_longitude=-122.4194, dropoff_latitude=37.8072, dropoff_longitude=-122.4056
    )


def create_second_trip():
    return Trip.objects.create(pickup_latitude=37.8849, pickup_longitude=-122.6194, dropoff_latitude=37.9072, dropoff_longitude=-122.4156
    )



class HttpTripTest(APITestCase):
    
    def setUp(self):
        user = create_user()
        response = self.client.post(reverse('user-signin'), data={
            'email': user.email,
            'password': PASSWORD
        })
        self.access = response.data['access']
    
        
    def test_user_can_list_trips(self):
        trips = [create_first_trip(), create_second_trip()]
        
        response = self.client.get(reverse('trips-list'), HTTP_AUTHORIZATION=f'Bearer {self.access}')
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        exp_trip_ids = [str(trip.id) for trip in trips]
        act_trip_ids = [trip['id'] for trip in response.data]
        
        self.assertCountEqual(exp_trip_ids, act_trip_ids)
        
    
    def test_user_can_view_trip_detail(self):
        trip = create_first_trip()
        
        expected_url = reverse('trip-details', kwargs={'trip_id': trip.id})
        
        response = self.client.get(expected_url, HTTP_AUTHORIZATION=f'Bearer {self.access}')

        self.assertEqual(status.HTTP_200_OK, response.status_code)

        self.assertEqual(response.data['id'], str(trip.id))
        self.assertEqual(response.data['pickup_latitude'], format(trip.pickup_latitude, '.6f'))
        self.assertEqual(response.data['pickup_longitude'], format(trip.pickup_longitude, '.6f'))
        self.assertEqual(response.data['dropoff_latitude'], format(trip.dropoff_latitude, '.6f'))
        self.assertEqual(response.data['dropoff_longitude'], format(trip.dropoff_longitude, '.6f'))