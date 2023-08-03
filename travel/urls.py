from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('book/<uid>/', views.booking, name="book"),
    path('register', views.register_page, name="register"),
    path('login', views.login_page, name="login"),
    path('logout', views.handleLogout, name="logout"),
    path("bookings", views.bookings, name="bookings"),



]
