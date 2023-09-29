from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


# Register your models here.
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('first_name', 'last_name', 'email', 'is_staff', 'is_active',)
    list_display_links = ('first_name', 'last_name', 'email')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone_number', 'first_name', 'last_name')}),
        ('permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'phone_number', 'password2', 'first_name', 'last_name')
        }),
        ('permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')})
    )
    search_fields = ('email',)
    ordering = ('email',)
    

admin.site.register(User, UserAdmin)