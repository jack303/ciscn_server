from django.contrib.auth.models import User
from rest_framework import serializers
from dht.models import  Request, Type, Resource_shield, Node_shield, Resource_text

class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','password')


class RequestSerializer(serializers.ModelSerializer):
    #
    class Meta:
        model = Request
        fields = ('__all__')

class TypeSerializer(serializers.ModelSerializer):
    #
    class Meta:
        model = Type
        fields = ('__all__')

class ResourceShieldSerializer(serializers.ModelSerializer):
    #
    class Meta:
        model = Resource_shield
        fields = ('__all__')

class NodeShieldSerializer(serializers.ModelSerializer):
    #
    class Meta:
        model = Node_shield
        fields = ('__all__')

class ResourceTextSerializer(serializers.ModelSerializer):
    #
    class Meta:
        model = Resource_text
        fields = ('__all__')
