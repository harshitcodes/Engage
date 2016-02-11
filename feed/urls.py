from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^post_create/$', 'feed.views.post_create', name = 'post_create'),
    url(r'^timeline/$', 'feed.views.timeline', name = 'timeline'),
    url(r'^post/(?P<id>\d+)/$', 'feed.views.post_detail', name = 'detail'),
    url(r'^post/(?P<id>\d+)/edit$', 'feed.views.post_update', name = 'update'),
    url(r'^post/(?P<id>\d+)$', 'feed.views.post_delete', name = 'post_delete'),
    
]

