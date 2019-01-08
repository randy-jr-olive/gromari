from django.urls import path

from coretemp import views

urlpatterns = [
    path('', views.coretemp, name='coretemp'),
]
