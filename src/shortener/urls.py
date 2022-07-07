from django.urls import path

from .views import index, register_user, logout_user, login_user, url_list, redirect_url


app_name = 'shortener'

urlpatterns = [
    path('', index, name='index'),
    path('register_user/', register_user, name='register_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('login_user/', login_user, name='login_user'),
    path('url_list/', url_list, name='url_list'),
    path('<str:hash_url>/', redirect_url, name='redirect_url')
]
