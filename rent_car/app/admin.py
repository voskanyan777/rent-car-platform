from django.contrib import admin
from .models import CarModel, CarReviewModel, OrdersModel

admin.site.register(CarModel)
admin.site.register(CarReviewModel)
admin.site.register(OrdersModel)
