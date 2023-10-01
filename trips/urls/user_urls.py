from django.urls import path
from rest_framework.routers import DefaultRouter
from ..views.user_views import UserViewSet, LoginView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('users/login/', LoginView.as_view(), name='user-login'),
    # Other app-specific URL patterns if any
]

urlpatterns += router.urls
