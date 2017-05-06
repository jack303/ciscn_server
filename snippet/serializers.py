from django.contrib.auth.models import User
from rest_framework import serializers

from snippet.models import Snippet

class UserSerializer(serializers.ModelSerializer):
    # this var name has to be the same with related name
    snippets_user = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets_user')

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('__all__')