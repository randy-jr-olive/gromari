from django.urls import path

import enviro

urlpatterns = [
    path('', views.enviro, name='enviro'),
]
