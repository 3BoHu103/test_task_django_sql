from django.urls import path

from .views import index, register_user, logout_user, login_user


app_name = 'shortener'

urlpatterns = [
    path('', index, name='index'),
    path('register_user/', register_user, name='register_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('login_user/', login_user, name='login_user')
]
