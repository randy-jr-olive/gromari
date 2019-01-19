from django.contrib import admin
from .models import Room, Plant, Journal, Equipment, SensorData, Tag

# register the pages in the admin view
admin.site.register(Room)
admin.site.register(Plant)
admin.site.register(Journal)
admin.site.register(Equipment)
admin.site.register(SensorData)
admin.site.register(Tag)
