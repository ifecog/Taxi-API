from django.urls import path
from trips.views.trip_views import trips_list, trip_details

urlpatterns = [
    path('', trips_list, name='trips-list'),
    path('<uuid:trip_id>/', trip_details, name='trip-details'),
]
