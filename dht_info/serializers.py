from django.contrib.auth.models import User
from rest_framework import serializers
from dht_info.models import DhtResource

#
from dht_info.models import Subject

from django.contrib.auth.models import User,Group
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'#('id', 'title', 'slug')




#
class DhtResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DhtResource
        fields = '__all__'

    def create(self, validated_data):


        # response to post
        # validated_data['comment'] = self.context['request']
        pass


#
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')