from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'(?P<src_lang>[a-z]{2})/(?P<trgt_lang>[a-z]{2}$)',views.speechToText,name='speechToText'),
    # url(r'(?P<num>[0-9]+)/(?P<co>\[.*\])',views.snap_coordinate,name='Location_route'),
    # url(r'(?P<source>[0-9]+)/(?P<target>[0-9]+)',views.route,name='Location_route')
]