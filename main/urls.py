from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('account/', views.account, name='account'),
]
