from django.contrib import admin

from APIs.models import Event

class EventAdmin(admin.ModelAdmin):#customize the Admin panel
    list_display = ['Title', 'registry_start', 'registry_end',
                    'created_date' , 'update_date', 'Decription']
    search_fields = ['Title', 'created_date']

admin.site.register(Event, EventAdmin)