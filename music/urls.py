from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # / Music /
    url(r'^$', views.index, name='index'),

    # /Music/[id]

    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /Music/Album_[id]/favourite/
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),
]