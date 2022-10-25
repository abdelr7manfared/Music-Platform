from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)
        widgets={'bio' : forms.Textarea(attrs={'rows': 8}),}

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
        widgets={'bio' : forms.Textarea(attrs={'rows': 8}),}
