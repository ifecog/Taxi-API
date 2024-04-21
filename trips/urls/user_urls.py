from django.urls import path
from trips.views.user_views import signup, get_users

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('get_users/', get_users, name='get_users'),
]
