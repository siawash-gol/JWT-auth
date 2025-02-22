from django.contrib import admin
from backend.Authentication.Profiles.models import Profile, Contact
from django.utils.translation import gettext_lazy as _


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ("user", "username", "get_full_name", "language", 'city')
    fieldsets = (
        ('Main', {
            'fields': ('user', 'email', 'username',)
        }),
        ('Personal', {
            'fields': ('first_name', 'last_name',)
        }),
        ('Nationality', {
            'fields': ('language', 'phone', 'state', 'city')
        })
    )
    list_filter = ['city', 'state', 'language']
    search_fields = ['username', 'first_name', 'last_name', 'email']


@admin.register(Contact)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_checked', 'date_created')
    fieldsets = (
        ('User Information', {'fields': ['email', 'full_name']}),
        ('Message Information', {'fields': ['message', 'is_checked']}),
    )
    search_fields = ('email', 'message', 'full_name')
    list_filter = ('is_checked', 'date_created')
