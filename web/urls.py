from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(r"", views.Home, name = "Home"),
    path("Master_List", views.Masters, name = "Master_List"),
    #path(r"^Courses_List$",views.Courses_List, name="Courses_List"),
   # path(r"^Events$", views.Event_Viewer, name = "Event_Viewer"),
    #Uncomplete
    path(r"Edit_Master/<str:id>", views.Edit_Master, name = "Edit_Master"),
    #path(r"Delete_Master", views.Delete_Master, name = "Delete_Master"),
    path(r"Add_Master", views.Add_Master, name = "Add_Master"),#add_master
    #path(r"Edit_Courses", views.Edit_Courses, name = "Edit_Courses"),
    #path(r"Delete_Courses", views.Delete_Courses, name = "Delete_Courses"),
    #path(r"Add_Course", views.Add_Courses, name = "Add_Courses"),
   # path(r"Edit_Member", views.Edit_Member, name = "Edit_Member"),
   # path(r"Add_Member", views.Add_Member, name = "Add_Member"),
  #  path(r"Delete_Member", views.Delete_Member, name = "Delete_Member"),
 #   path(r"Members", views.Members, name = "Members"),
]

