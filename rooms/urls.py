from django.urls import path

from rooms import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('room/', views.roomDetails, name='roomDetails'),
    path('room/<int:id>', views.roomDetails, name='roomDetails'),
    path('room/delete/<int:id>', views.deleteRoom, name='deleteRoom'),
    path('plant/', views.plantDetails, name='plantDetails'),
    path('plant/<int:id>', views.plantDetails, name='plantDetails'),
    path('plant/delete/<int:id>', views.deletePlant, name='deletePlant'),
]
