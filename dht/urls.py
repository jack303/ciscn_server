from rest_framework import routers
from django.conf.urls import url,include

from dht import views

router = routers.DefaultRouter()
router.register(r'node_shield',views.NodeShieldViewSet)
router.register(r'request',views.RequestViewSet)
router.register(r'resource_shield',views.ResourceShieldViewSet)
router.register(r'resource_text',views.ResourceTextViewSet)
router.register(r'type',views.TypeViewSet)

urlpatterns = [
    url(r'^requestinfo/(?P<info_hash>[ -~]+)/$', views.getbyxml),
    url(r'', include(router.urls)),
    url(r'^user_login/$',views.UserLogin),
    url(r'^resourceRecord/$',views.ResourceRecord),
    url(r'^nodeRecord/$',views.NodeRecord),
    # url(r'^r')

]