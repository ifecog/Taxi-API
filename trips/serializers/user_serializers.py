from typing import Dict, Any

from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, RefreshToken

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)
    is_admin = serializers.SerializerMethodField(read_only=True)
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    class Meta:
        model = get_user_model()
        fields = ['id', '_id', 'name', 'email', 'phone_number', 'is_admin', 'confirm_password']
        
    def get__id(self, obj):
        return obj.id
    
    def get_name(self, obj):
        name = ''
        try:
            name = obj.first_name + ' ' + obj.last_name
            if name == '':
                return obj.email
        except:
            pass
        
        return name
    
    def get_is_admin(self, obj):
        return obj.is_staff
    

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ['id', '_id', 'name', 'email', 'phone_number', 'is_admin', 'token']
        
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        
        return str(token.access_token)
    
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    token_class = RefreshToken

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        
        serializer = UserSerializerWithToken(self.user).data

        for key, value in serializer.items():
            data[key] = value
        
        return data
