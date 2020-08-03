from django.contrib import admin
from django.urls import path, include
from . import views
from login import views as login_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', include('login.urls')),
    path('profile/', login_views.profile, name='profile')
]
