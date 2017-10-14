from django.conf.urls import url
from . import views

urlpatterns = [
    # / Music /
    url(r'^$', views.index, name='index'),

    # /Music/[id]

    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail')
]