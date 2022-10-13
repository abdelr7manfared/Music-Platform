from django.http import HttpResponse
from django.shortcuts import render
from .models import Artist
from .form import ArtistForm
from django.views.generic import TemplateView
# Create your views here.
class ArtistList(TemplateView):
    template_name = "ListArtist.html"
    def get(self,request):
        return render(request,self.template_name,{'data':Artist.objects.prefetch_related('album_set')})

class CreateArtist(TemplateView):
    template_name = "createArtist.html"
    form_class = ArtistForm
    def get(self,request):
        if request.user.is_authenticated:
            form = self.form_class()            
            return render(request,self.template_name,{'form':form})
        else : 
            return HttpResponse("User is authenticated")
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request,self.template_name,{'form':form})

