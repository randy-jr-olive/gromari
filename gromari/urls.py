from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from . import views

urlpatterns = [
    path('', include('rooms.urls'), name='rooms'),
    path('admin/', admin.site.urls),
    path('register/', accounts_views.register, name='register'),
    path('profile/', accounts_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('rooms/', include('rooms.urls'), name='rooms'),
]

urlpatterns += staticfiles_urlpatterns()
