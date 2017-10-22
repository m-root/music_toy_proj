from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # / Music /
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # Music/Album/Add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add')

]