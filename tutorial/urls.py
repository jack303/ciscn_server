from django.conf.urls import url
from tutorial import views

urlpatterns = [
    url(r'^snippet_list/$',views.snippet_list,name='snippet_list'),

]