from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser


class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    
    list_display = ('username', 'email', 'is_admin',)
    
    list_filter = ('is_admin',)
    
    fieldsets = (
            (None, {'fields': ('username', 'email', 'password', 'avatar')}),
            ('Permissions', {'fields': ('is_admin',)})
        )
    
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_admin')}
        ),
    )
    
    search_fields = ('email',)
    
    ordering = ('email',)
    

    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
