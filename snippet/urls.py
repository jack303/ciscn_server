from django.conf.urls import url
from snippet import views
urlpatterns = [

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^snippet_list/$',views.SnippetList.as_view(),name='snippet_list'),
    url(r'^snippet_detail/(?P<pk>\d+)/$',views.SnippetDetail.as_view(),name='snippet_detail'),
]