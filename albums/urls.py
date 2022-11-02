from django.urls import path
from .views import Aproved_Album,Aproved_Album_ManuallyFilter
urlpatterns = [
    path("",Aproved_Album.as_view()),
    path("manual/",Aproved_Album_ManuallyFilter.as_view())
]
