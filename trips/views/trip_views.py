
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from trips.serializers.trip_serializers import TripSerializer
from trips.models import Trip


@api_view(['GET'])
def trips_list(request):
    trips = Trip.objects.order_by('-created_time')
    serializer = TripSerializer(trips, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])
def trip_details(request, trip_id=None):
    trip = get_object_or_404(Trip, id=trip_id)
    serializer = TripSerializer(trip, many=False)
    
    return Response(serializer.data)
