from app.views import index, register, catalog, description, cart, login_view, logout_user
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('register/', register),
    path('login/', login_view),
    path('logout/', logout_user),
    path('catalog/', catalog),
    path('description/<str:car_name>/', description, name='description'),
    path('cart/', cart)
]
