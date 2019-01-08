from django.urls import path

from enviro import views

urlpatterns = [
    path('', views.enviro, name='enviro'),
]
