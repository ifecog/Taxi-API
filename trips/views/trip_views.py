
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from trips.serializers.trip_serializers import TripSerializer
from trips.models import Trip


# class TripViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Trip.objects.order_by('-created_time')
#     serializer_class = TripSerializer

class TripViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['get'])
    def trip_list(self, request):
        trips = Trip.objects.order_by('-created_time')
        serializer = TripSerializer(trips, many=True)
        
        return Response(serializer.data)