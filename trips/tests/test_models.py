from django.test import TestCase
from django.urls import reverse

from trips.models import Trip

def create_trip():
    return Trip.objects.create(
        pickup_latitude=37.7749,
        pickup_longitude=-122.4194,
        dropoff_latitude=37.8072,
        dropoff_longitude=-122.4056,
        status=Trip.REQUESTED
    )

class TripModelTestCase(TestCase):
    
    def test_create_trip(self):
        # create anew trip instance
        trip = create_trip()
        # check that the trip was created successfuly
        self.assertIsNotNone(trip.id)
        self.assertEqual(trip.status, Trip.REQUESTED)
        
        # # get the absolute url for trip
        # absolute_url = trip.get_absolute_url()
        
        # # check that the absolute url matches the expexted_url
        # expected_url = reverse('trip:trip_detail', kwargs={'trip_id': trip.id})
        # self.assertEqual(absolute_url, expected_url)