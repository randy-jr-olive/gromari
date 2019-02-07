from django.urls import path

from rooms import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('room/<int:room_id>', views.roomDetails, name='roomDetails'),
    path('room/delete/<int:room_id>', views.deleteRoom, name='deleteRoom'),
    path('room/<int:room_id>/plant/<int:plant_id>', views.plantDetails, name='plantDetails'),
    path('plant/delete/<int:plant_id>', views.deletePlant, name='deletePlant'),
    path('journal', views.journalHome, name='journalHome'),
    path('journal/delete/<int:journal_id>', views.deleteJournalEntry, name='deleteJournalEntry'),
    path('journal/<int:journal_id>', views.journalDetails, name='journalDetails'),
    path('journal/<int:journal_id>/<str:room_tag>', views.journalDetails, name='journalDetails'),
]
