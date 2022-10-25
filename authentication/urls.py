from django.urls import path
from .views import CreateUser,LoginUser
from knox import views as knox_views
urlpatterns = [
    path("register/",CreateUser.as_view()),
    path("login/",LoginUser.as_view()),
    path("logout/",knox_views.LogoutView.as_view())
]
