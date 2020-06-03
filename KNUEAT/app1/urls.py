from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('home',views.home, name='home'),
    path('category',views.category, name='category'),
    path('restaurant',views.restaurant, name='restaurant'),
]