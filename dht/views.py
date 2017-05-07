from rest_framework import serializers, generics, viewsets, permissions
from dht.models import Resource, File_list, Request, Type, Resource_shield, Node_shield, Resource_text
from dht.serializers import ResourceSerializer, FileListSerializer, RequestSerializer, TypeSerializer, \
    ResourceShieldSerializer, NodeShieldSerializer, ResourceTextSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class FileListViewSet(viewsets.ModelViewSet):
    queryset = File_list.objects.all()
    serializer_class = FileListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ResourceShieldViewSet(viewsets.ModelViewSet):
    queryset = Resource_shield.objects.all()
    serializer_class = ResourceShieldSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class NodeShieldViewSet(viewsets.ModelViewSet):
    queryset = Node_shield.objects.all()
    serializer_class = NodeShieldSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ResourceTextViewSet(viewsets.ModelViewSet):
    queryset = Resource_text.objects.all()
    serializer_class = ResourceTextSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
