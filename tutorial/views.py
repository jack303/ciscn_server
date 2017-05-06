# -*-coding:utf-8 -*-
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, permissions, mixins, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from tutorial.models import Snippet
from tutorial.serialzers import SnippetSerializer

# @csrf_exempt  # avoid the csrf token of method POST
@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
def snippet_list(request,format=None):
    # manage lists of object
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)

        #In order to allow non-dict objects to be serialized
        #  set the safe parameter to False.
        # version without rest-framework
        #return JsonResponse(serializer.data,status=200,safe=False)

        # with rest-framework
        return Response(serializer.data,content_type='application/json;utf-8')
    elif request.method == 'POST':

        serializer = SnippetSerializer(data=request.data)
        # save the serializer means to create or update the snippet object
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
#@permission_classes((permissions.AllowAny,))
def snippet_detail(request, pk,format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data,)

    elif request.method == 'PUT':
        # !!  how to update an object from put data
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes((permissions.AllowAny,))
class SnippetList(APIView):
    def get(self,format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return Response(serializer.data)

class SnippetDetail(APIView):
    def get_object(self,pk):

        pass
    def get(self,pk,format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    pass
