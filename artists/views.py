from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Artist
from albums.form import AlbumForm
from .form import ArtistForm
# Create your views here.
def create(request):
    form = ArtistForm()
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid(): 
            form.save()
            print("Marwan Pablo")
    return render(request,'createArtist.html',{'form':form})

def listArtist(request):
    return render(request,'ListArtist.html',{'data':Artist.objects.prefetch_related('album_set')})