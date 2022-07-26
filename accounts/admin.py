from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active' )
    # If I want to click this ('email', 'first_name', 'last_name', 'username') then i will inside this
    list_display_links = ('email', 'first_name', 'last_name', 'username') 
    readonly_fields =  ('last_login', 'date_joined')
    ordering = ('-date_joined',) # Show Decending Order

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()  # Password Read only

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')

admin.site.register(Account, AccountAdmin)
admin.site.register(UserProfile, UserProfileAdmin)