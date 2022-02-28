
from django.shortcuts import render
from ast import Lambda
import re
from unicodedata import category
from django.shortcuts import redirect, render

from web.models import Master, People
#returns Home Page And its Contents Data
def Home(request):
    pass

#-------------------------------------------------------------
"""Masters Control And Render View
   IN CONTROL  View The Website Manager Must Loged In / Features : Create/Edit/Delete
"""
"""Showing All Masters"""
def Masters(request, master):
    if request.method == "POST":
        result  = Master.objects.filter(f"{master}")
        master_info_list = map(lambda item:f"{item.first_name}{item.last_name}",
                                result)
        context = {"Master_list":master_info_list}
        return render(request, "web\Master.html", context)
    else:
#Pop The Aditional Data`s From Masters_Delivery_list
#For Increas The Delivery Speed
        Masters_Delivery_list = Master.objects.values_list(
                                                'first_name',
                                                'last_name' ,
                                                'Picture_URL',
                                                'EmailAddress',
                                                'Performance_resukt'
                                                )
        context = {"Masters_Delivery_list":Masters_Delivery_list}
        return render(request, "Master_List.html", context)
#---------------------------------------------------------------------
"""Get The Master`s Information And Push in to Data Base"""
def Masters_Create(request):
    if request.method == "POST":
        First_name = request.POST["first_name"].strip().lower()
        Last_name  = request.POST["last_name"].strip().lower()
        if Master.objects.filter(first_name = f"{First_name}",
                                last_name = f"{Last_name}"
                                ):
            context = {"Message": "This Object is allready exist"}
            return render(request, "web\Master.html", context)
        else:
            First_name = request.POST["first_name"].strip().lower()
            Last_name  = request.POST["last_name"].strip().lower()
    else:
        redirect("Master_List")

