from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', "post.views.post_list"),
    url(r'^create/$', "post.views.post_create"),
    url(r'^detail/$', "post.views.post_detail"),
    url(r'^update/$', "post.views.post_update"),
    url(r'^delete/$', "post.views.post_delete"),
    # #url(r'^post/$', "<appname>.views.<function_name>"),
]