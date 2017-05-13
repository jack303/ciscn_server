from collections import OrderedDict

import time,datetime

import app as app

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from rest_framework import serializers, generics, viewsets, permissions, status
from rest_framework.decorators import detail_route, api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from dht.models import Request, Type, Resource_shield, Node_shield, Resource_text, SearchHash, Node
from dht.serializers import RequestSerializer, TypeSerializer, \
    ResourceShieldSerializer, NodeShieldSerializer, ResourceTextSerializer, \
    UserLoginSerializer


ResourceRecordModel = {
    "id": "resource-003",
    "ip": "114.117.194.2",
    'src': 'img address',
    'heading': 'ip地址',
    'belonging': '归属地',
    'capturetime': '捕获时间',
    'resourcename': '资源名',
    'resourcetype': '资源文件类型',
    'classfystandard': '资源分类',
    'labeltype': 'undefined'
}

NodeRecordModel = {
    'src': 'img address',
    'ip': 'ip地址',
    'heading': 'ip',
    'belonging': '归属地',
    'capturetime': '捕获时间',
    'antinum': '叛乱资源数',
    'pornnum': '色情资源数',
    'vionum': '暴力资源数',
    'feature': ['特点', ]
}
RealtimeNonLiveRecord = {
    "recordtype": "nonlive",
    "id": "id",
    "ip": "ip",
    "src": "img address",
    "title": "ip",
    "belonging": "四川成都市",
    "capturetime": "Sun, 23 Apr 2017 09:42:35 GMT",
    "filename": "name",
    "filetype": ["视频文件"],
    "classification": ["色情"]
}

RealtimeLiveRecord = {
    "src": "../images/harmfulinfo/porn_128px_1075595_easyicon.net.png",
    "title": "斗鱼专业色情主播",
    "capturetime": "Sun, 23 Apr 2017 09:44:35 GMT",
    "platform": "斗鱼tv",
    "number": "10092",
    "livetype": "色情"
}

LiveRecord = {
    "liveId": "live-001",
    "src": "../images/harmfulinfo/porn_128px_1075595_easyicon.net.png",
    "title": "斗鱼专业色情主播",
    "capturetime": "Sun, 23 Apr 2017 09:44:35 GMT",
    "platform": "斗鱼tv",
    "number": "10092",
    "livetype": "色情"
}


# # login

@api_view(['GET', 'POST'])
def UserLogin(request, *args):
    if 'username' in request.GET:
        user = authenticate(username=request.GET['username'], password=request.GET['password'])
        serializer = UserLoginSerializer(user)
        if user is not None:
            login(request, user)
            # print(request.user)
            return Response(serializer.data['username'], status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_200_OK)
    if 'username' in request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        serializer = UserLoginSerializer(user)
        if user is not None:
            login(request, user)
            # print(request.user)
            return Response(serializer.data['username'], status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_200_OK)



@api_view(['GET'])
def ResourceRecord(request):
    page = int(request.GET['page'])
    if 'ip' in request.GET:
        node_ip = request.GET['ip']
        porn = request.GET['showPornInfo']
        anti = request.GET['showAntiInfo']
        vio = request.GET['showViolenceInfo']
        text = request.GET['showText']
        image = request.GET['showImage']
        video = request.GET['showVideo']
        time = request.GET['time']

        result = SearchHash.objects.filter(source_ip=node_ip).all()

        # if porn == 'true':
        #     result = result.filter(porn_num__gt=0).all()
        # else:
        #     result = result.all()
        # if anti == 'true':
        #     result = result.filter(anti_num__gt=0).all()
        # else:
        #     result = result.all()
        # if vio == 'true':
        #     result = result.filter(vio_num__gt=0).all()
        # else:
        #     result = result.all()
        if text == 'true':
            result = result.all()
        else:
            result = result.exclude(category='document').all()
        if image == 'true':
            result = result.all()
        else:
            result = result.exclude(category='other').all()
        if video == 'true':
            result = result.all()
        else:
            result = result.exclude(category='video').all()
        time = datetime.datetime.strptime(time,"%d %B %Y - %I:%M %p")
        result = result.filter(last_seen__gte=time).all()
        if (page - 1) * 5 >= len(result):
            return Response({
                'detail': 'no more resource'
            })
        result = result[(page - 1) * 5:5]
    # result = SearchHash.objects.order_by('-create_time')[:5]
    response = [0]*len(result)
    i = 0
    for item in result:
        temp = ResourceRecordModel.copy()
        temp["id"] = item.id
        temp["ip"] = item.source_ip
        temp['src'] = "http://img2.imgtn.bdimg.com/it/u=1524255442,3514440980&fm=23&gp=0.jpg"
        temp['heading'] = item.source_ip
        temp['belonging'] = "双流"
        temp['capturetime'] = item.create_time.strftime("%d %B %Y - %I:%M %p")
        temp['resourcename'] = item.name
        temp['resourcetype'] = item.category
        temp['classfystandard'] = '色情'
        temp['labeltype'] = 'undefined'
        response[i] = temp
        i = i + 1
    return Response(response)

@api_view(['GET'])
def ResourceDetail(request):

    return Response()

@api_view(['GET'])
def NodeRecord(request):
    page = int(request.GET['page'])

    #params:{'showPornInfo':true,'showAntiInfo':true,'showViolenceInfo':true,'area':'China'}
    porn = request.GET['showPornInfo']
    anti = request.GET['showAntiInfo']
    vio = request.GET['showViolenceInfo']
    area = request.GET['area']

    if area is not '':
        result = Node.objects.filter(belonging__contains=area).all()
    else:
        result = Node.objects.all()
    if porn == 'true' :
        result = result.filter(porn_num__gt=0).all()
    else:
        result = result.all()
    if anti == 'true':
        result = result.filter(anti_num__gt=0).all()
    else:
        result = result.all()
    if vio == 'true':
        result = result.filter(vio_num__gt=0).all()
    else:
        result = result.all()

    if (page-1) * 5 >= len(result):
        return Response({
            'detail': 'no more nodes'
        })
    result = result[(page-1)*5:5]
    response = [0]*len(result)
    i=0
    for item in result:
        temp = NodeRecordModel.copy()
        # temp["ip"]= item.id
        temp["ip"]= item.ip
        temp['src']=item.img_src
        temp['heading']=item.ip
        temp['belonging']= item.belonging
        temp['capturetime']= item.capture_time
        temp['antinum']=item.anti_num
        temp['pornnum']= item.porn_num
        temp['vionum']= item.vio_num
        features = item.feature.split('|')
        temp['feature']= features
        response[i] = temp
        i = i+1
    return Response(response)
@api_view(['GET'])
def NodeResourceList(request):
   node_ip = request.GET['ip']
   page = request.GET['page']
   result = SearchHash.objects.filter(source_ip=node_ip).all()
   if (page - 1) * 5 >= len(result):
       return Response({
           'detail': 'no more nodes'
       })
   result = result[(page - 1) * 5:5]
   i =0
   for item in result:
        item.name

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


@api_view(['GET'])
def getbyxml(request, info_hash, format=None):
    print(info_hash)
    ob = Request.objects.filter(time__gte=info_hash).all()
    ser = RequestSerializer(ob)
    return Response(ser.data)
    pass


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ResourceShieldViewSet(viewsets.ModelViewSet):
    queryset = Resource_shield.objects.all()
    serializer_class = ResourceShieldSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class NodeShieldViewSet(viewsets.ModelViewSet):
    queryset = Node_shield.objects.all()
    serializer_class = NodeShieldSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ResourceTextViewSet(viewsets.ModelViewSet):
    queryset = Resource_text.objects.all()
    serializer_class = ResourceTextSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
