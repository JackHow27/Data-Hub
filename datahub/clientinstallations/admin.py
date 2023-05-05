from django.contrib import admin
from .models import Client, ApplicationInstance

class clientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'shortcode')

class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version', 'client')

admin.site.register(Client, clientAdmin)
admin.site.register(ApplicationInstance, AppAdmin)