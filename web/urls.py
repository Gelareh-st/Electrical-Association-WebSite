from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(r"", views.Home, name = "Home"),
    path(r"^Master_List$", views.Masters, name = "Master_List"),
]
