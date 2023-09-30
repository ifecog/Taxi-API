from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from ..serializers.user_serializers import UserSerializer, UserSerializerWithToken, MyTokenObtainPairSerializer

# Create your views here.
class UserViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['get'])
    def get_users(self, request):
        User = get_user_model()
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
