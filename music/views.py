from django.shortcuts import render, get_object_or_404
from .models import Album, Song


#Indexing Music
def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums' : all_albums}
    return render(request, 'music/index.html', context)

# Try checking if there is an album with the ID and if not it returns an error response
def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album' : album})

def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', { 'album' : album,
                                                    'error_message' : "You did not select a valid song"
                                                    })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'albums': album})