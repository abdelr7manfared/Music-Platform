from django.shortcuts import render

from artists.models import Artist
from  .form  import AlbumForm
# Create your views here.
def create(request):
    form=AlbumForm()
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'CreateAlbum.html',{'form':form})

