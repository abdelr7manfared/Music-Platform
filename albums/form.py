from django.forms import ModelForm
from .models import Album
from django.forms.widgets import DateInput

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields='__all__'
        help_texts={
        'album_approved':'Approve the album if its name is not explicit'
         }   

        widgets={
        'release_date' : DateInput(attrs={'type': 'date'}),
        }
    


