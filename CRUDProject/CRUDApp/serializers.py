from rest_framework import serializers
from .models import User

class UserRetrieveDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('name','email')

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','name','email')