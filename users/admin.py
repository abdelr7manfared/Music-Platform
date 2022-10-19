from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .form import CustomUserChangeForm,CustomUserCreationForm
from .models import User
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display=['username','email','bio']
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username','email', 'is_staff', 'is_active','bio')
    list_filter = ('username','email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','bio')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password', 'password2', 'is_staff', 'is_active','bio')}
        ),
    )

