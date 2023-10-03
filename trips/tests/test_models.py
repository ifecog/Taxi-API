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
        trip = create_trip()
        
        self.assertIsNotNone(trip.id)
        self.assertEqual(trip.status, Trip.REQUESTED)
        
    
    def test_str_representation(self):
        # Create a Trip instance
        trip = create_trip()
        
        # Check that the string representation matches the expected format
        expected_str = f'{trip.id}'
        self.assertEqual(str(trip), expected_str)