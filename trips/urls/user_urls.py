from django.urls import path
from trips.views.user_views import signup, get_users, LoginView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    # login view
    path('signin/', LoginView.as_view(), name='user-signin'),
    path('signup/', signup, name='user-signup'),
    
    # Token
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    
    path('get_users/', get_users, name='get_users'),
]
