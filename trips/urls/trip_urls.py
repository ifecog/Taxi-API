from django.urls import path
from rest_framework.routers import DefaultRouter
from trips.views.trip_views import TripViewSet

router = DefaultRouter()
router.register(r'trips', TripViewSet, basename='trip')

urlpatterns = [
    
]

urlpatterns += router.urls