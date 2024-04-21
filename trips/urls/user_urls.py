from django.urls import path
from trips.views.user_views import signup, get_users, LoginView

urlpatterns = [
    # login view
    path('signin/', LoginView.as_view(), name='user-signin'),
    path('signup/', signup, name='user-signup'),
    path('get_users/', get_users, name='get_users'),
]
