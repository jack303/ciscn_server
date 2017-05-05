from django.conf.urls import url,include
from dht_info import views


# configure the routers to route the viewsets



urlpatterns = [
    url(r'^subjects/$', views.SubjectListView.as_view(),
        name='subject_list'),
    url(r'^subjects/(?P<id>[0-9]+)/$',
        views.SubjectDetailView.as_view(),
        name='subject_detail'),
    url(r'^subjects/(?P<title>^)/$',
        views.SubjectDetailView.as_view(),
        name='subject_detail'),


]


