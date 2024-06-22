from django.shortcuts import render

from .models import CarModel


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def catalog(request):
    cars = CarModel.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'catalog.html', context=context)


def description(request, car_name):
    car_info = CarModel.objects.get(name=car_name)
    return render(request, 'description.html', context={"car": car_info})
