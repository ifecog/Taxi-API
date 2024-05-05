from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from trips.serializers.user_serializers import UserSerializer, UserSerializerWithToken, LoginSerializer


User = get_user_model()


@api_view(['POST'])
def signup(request):
    serializer = UserSerializerWithToken(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    if 'password' not in request.data or 'confirm_password' not in request.data:
        return Response({'error': 'Both password and confirm_password are required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.data['password'] != request.data['confirm_password']:
        return Response({'error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)
    
    user_data = {
        'first_name': request.data['first_name'],
        'last_name': request.data['last_name'],
        'email': request.data['email'],
        'phone_number': request.data['phone_number'],
        'password': make_password(request.data['password'])
    }
    
    try:
        user = User.objects.create_user(**user_data)
        
        group_data = request.data.get('group')
        if group_data:
            group, _ = Group.objects.get_or_create(name=group_data)
            user.groups.add(group)
        
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        detail = {'detail': 'User with email already exists, please login!'}
        return Response(detail, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
# @permission_classes([IsAdminUser])
def get_users(request):
    users = User.objects.order_by('-id')
    serializer = UserSerializer(users, many=True)
    
    return Response(serializer.data)

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
