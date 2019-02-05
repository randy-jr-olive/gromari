from django.urls import path

from rooms import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('room/<int:room_id>', views.roomDetails, name='roomDetails'),
    path('room/delete/<int:room_id>', views.deleteRoom, name='deleteRoom'),
    path('room/<int:room_id>/plant/<int:plant_id>', views.plantDetails, name='plantDetails'),
    path('plant/delete/<int:plant_id>', views.deletePlant, name='deletePlant'),
]
