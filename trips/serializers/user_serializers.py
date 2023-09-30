from typing import Dict, Any

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, RefreshToken

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)
    is_admin = serializers.SerializerMethodField(read_only=True)
    confirm_password = serializers.SerializerMethodField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', '_id', 'email', 'phone_number', 'password']
        
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
    
    def validate_password(self, data):
        password = data['password']
        confirm_password = data['confirm_password']
        
        if password != confirm_password:
            return serializers.ValidationError({
                'confirm_password': ['Passwords do not match.']
            })
            
        return data


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', '_id', 'name', 'email', 'phone_number', 'is_admin', 'token']
        
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        
        return str(token.access_token)
    
    

