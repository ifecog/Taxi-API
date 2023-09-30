from django.urls import path
from rest_framework.routers import DefaultRouter
from ..views.user_views import UserViewSet, MyTokenObtainPairView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('users/login/', MyTokenObtainPairView.as_view(), name='token-obtain-pair'),
    # Other app-specific URL patterns if any
]

urlpatterns += router.urls
