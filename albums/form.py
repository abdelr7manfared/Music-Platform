from django.forms import ModelForm
from .models import Album
from .models import Song
class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields='__all__'
        help_texts={
        'album_approved':'Approve the album if its name is not explicit'
         }   
       #widgets={'release_date' : DateInput(attrs={'type': 'date'}),}
    
        

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'
