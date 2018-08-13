from django.urls import path
from . import views
from django.contrib.auth.views import login

app_name='app'

urlpatterns = [
    path('top', views.top, name = 'top'),
    path('registration', views.registration, name = 'registration'),
    path('delete', views.delete, name= 'delete'),
    path('login', login, name= 'login'),
    path('userlogout', views.userlogout, name='userlogout'),
    path('search', views.search, name= 'search')
]