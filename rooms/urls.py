from django.urls import path

from rooms import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
]
