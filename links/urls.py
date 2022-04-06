from django.urls import path

from links import views

urlpatterns=[
    path('useful_link',views.useful_link,name='useful_link'),
     #useful_link should be written in html file
]