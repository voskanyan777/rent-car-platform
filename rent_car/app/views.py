from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegisterForm
from .models import CarModel


def index(request):
    return render(request, 'index.html')


# def login(request):
#     return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return render(request, 'index.html', )
    else:
        form = UserRegisterForm()
    return render(request, 'login.html', {'form': form})


def catalog(request):
    cars = CarModel.objects.all()
    context = {
        'cars': cars
    }
    return render(request, 'catalog.html', context=context)


def description(request, car_name):
    car_info = CarModel.objects.get(name=car_name)
    return render(request, 'description.html', context={"car": car_info})


def cart(request):
    return render(request, 'cart.html')
