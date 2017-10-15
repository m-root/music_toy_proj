from django.http import Http404
from django.shortcuts import render
from .models import Album

#Indexing Music
def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums' : all_albums}
    return render(request, 'music/index.html', context)

# Try checking if there is an album with the ID and if not it returns an error response
def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'albums' : album})