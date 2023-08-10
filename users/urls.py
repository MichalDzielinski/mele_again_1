from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('my-login', views.my_login, name='my-login'),
    path('my-logout', views.my_logout, name='my-logout'),
]