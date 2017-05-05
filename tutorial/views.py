from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from tutorial.models import Snippet
from tutorial.serialzers import SnippetSerializer

@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)

        #In order to allow non-dict objects to be serialized
        #  set the safe parameter to False.
        return JsonResponse(serializer.data,status=200,safe=False)


    pass