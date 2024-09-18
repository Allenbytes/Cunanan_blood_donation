from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User, Profile

class UserAdmin(DefaultUserAdmin):
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ()  # Ensure this is empty as no many-to-many fields

    # Ensure 'list_filter' does not reference non-existent fields
    list_filter = ('is_staff', 'is_superuser', 'is_active')

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
