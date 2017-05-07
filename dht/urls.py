from rest_framework import routers
from django.conf.urls import url,include

from dht import views

router = routers.DefaultRouter()
router.register(r'resource',views.ResourceViewSet)
router.register(r'file_list',views.FileListViewSet)
router.register(r'node_shield',views.NodeShieldViewSet)
router.register(r'request',views.RequestViewSet)
router.register(r'resource_shield',views.ResourceShieldViewSet)
router.register(r'resource_text',views.ResourceTextViewSet)
router.register(r'type',views.TypeViewSet)

urlpatterns = [
    url(r'',include(router.urls)),
]