from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts import views as accounts_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', accounts_views.register, name='register'),
    path('rooms/', include('rooms.urls')),
]

urlpatterns += staticfiles_urlpatterns()
