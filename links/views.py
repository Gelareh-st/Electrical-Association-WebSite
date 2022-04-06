import imp
from django.shortcuts import render

from links.models import Use_link

# Create your views here.

def useful_link(request):
    link1=Use_link()  # we're going to add more useful links. 
    link1.Description=""
    link1.Title=""

    links=[] 

    return render(request,'useful_link.html',{'links': links}) #useful_link.html is not made yet
