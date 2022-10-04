from django.contrib import admin

from event.models import Event, User

# Register your models here.
admin.site.register(Event)
admin.site.register(User)