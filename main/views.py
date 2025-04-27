from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Car
from .views_account import account

# Create your views here.
def index(request):
    car_of_the_week = Car.objects.order_by('-created_at').first()
    context = {
        'car_of_the_week': car_of_the_week
    }
    return render(request, 'main/index.html', context)


def cars(request):
    cars = Car.objects.all().order_by('-created_at')
    context = {
        'cars': cars
    }

    return render(request, 'main/cars.html', context)

def about(request):
    return render(request, 'main/about.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('main:account')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'main/login.html'
