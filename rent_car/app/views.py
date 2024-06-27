from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from .forms import UserRegisterForm
from .models import CarModel


def index(request):
    return render(request, 'index.html')


# def login(request):
#     return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return render(request, 'index.html', )
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return render(request, 'catalog.html')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
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
    return render(request, 'cart.html', context={'user': request.user})


def logout_user(request):
    logout(request)
    return render(request, 'index.html')
