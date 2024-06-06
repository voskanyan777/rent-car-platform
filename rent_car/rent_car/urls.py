from django.contrib import admin
from django.urls import path
from app.views import index, login, catalog, description

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', login),
    path('catalog/', catalog),
    path('description/<str:car_name>/', description, name='description')
]
