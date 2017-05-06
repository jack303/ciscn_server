from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from tutorial import views

urlpatterns = [
    url(r'^snippet_list/$',views.snippet_list,name='snippet_list'),
    url(r'^snippet_list_class/$',views.SnippetList.as_view(),name='snippet_list'),
    url(r'^snippet_detail/(?P<pk>\d+)/$',views.snippet_detail,name='snippet_detail'),

]
# urlpatterns = format_suffix_patterns(urlpatterns)