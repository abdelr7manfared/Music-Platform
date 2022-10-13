from django.shortcuts import render
from django.views.generic import TemplateView
from  .form  import AlbumForm
from django.http import HttpResponse
# Create your views here.
class CreateAlbum(TemplateView):
    template_name = "CreateAlbum.html"
    form_class = AlbumForm
    def get(self,request):
        #print(request.user.is_authenticated)
        if request.user.is_authenticated:
            form = self.form_class()
            return render(request,self.template_name,{'form':form})
        else:
            return HttpResponse('User is authenticated')
    def post(self,request):
        form  = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request,self.template_name,{'form':form})