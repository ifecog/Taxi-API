from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from ..serializers.user_serializers import UserSerializer, UserSerializerWithToken, LoginSerializer


User = get_user_model()
# Create your views here.
class UserViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = UserSerializerWithToken(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Check if 'password' and 'confirm_password' fields are present in request data
        if 'password' not in request.data or 'confirm_password' not in request.data:
            return Response({'error': 'Both password and confirm_password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if 'password' and 'confirm_password' match
        if request.data['password'] != request.data['confirm_password']:
            return Response({'error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.validated_data['first_name'] = request.data['first_name']
        serializer.validated_data['last_name'] = request.data['last_name']
        serializer.validated_data['email'] = request.data['email']
        serializer.validated_data['phone_number'] = request.data['phone_number']
        serializer.validated_data['password'] = make_password(request.data['password'])
        
        try:
            serializer.save()          
            
        except Exception as e:
            detail = {'detail': 'User with email already exists, please login!'}
            return Response(detail, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
    def get_users(self, request):
        users = User.objects.order_by('-id')
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
