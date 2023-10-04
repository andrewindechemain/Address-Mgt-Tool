"""Django configurations for registering Models in the Admin view
Learn more from: https://docs.djangoproject.com/en/4.2/ref/django-admin/
."""
from django.contrib import admin
from .models import Address

class AddressAdmin(admin.ModelAdmin):
    list_display = ('ip', 'customer', 'allocated')
    search_fields = ('ip', 'allocated')

admin.site.register(Address,AddressAdmin)
