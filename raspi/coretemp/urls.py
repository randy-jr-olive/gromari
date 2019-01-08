from django.urls import path

import coretemp

urlpatterns = [
    path('', views.coretemp, name='coretemp'),
]
