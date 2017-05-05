# from django.shortcuts import render

# Create your views here.
# from rest_framework import response,permissions,viewsets,renderers
# from rest_framework.decorators import (
#     permission_classes,detail_route
# )

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets

from dht_info.serializers import SubjectSerializer, UserSerializer
from .models import Subject


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    pass

class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = ('id')
    pass

class SubjectUpdateView(generics.UpdateAPIView):

    """
        We can easily break these down into individual views
         if we need to, but using viewsets keeps 
         the view logic nicely organized as well as being very concise.
    """
class UserViewSet(viewsets.ModelViewSet):
    """
       API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

