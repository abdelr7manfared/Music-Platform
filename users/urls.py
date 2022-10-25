from django.urls import path
from .views import UserDetail 
urlpatterns = [
    path("<int:pk>/",UserDetail.as_view()),
]