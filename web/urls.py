from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r"", views.Home, name = "Home"),
    path(r"Masters/", views.Master_list.as_view(),
         name="Master_view"),
    path(r"Members/", views.Members_list.as_view(),
         name="Members"),
    path(r"Courses/", views.Courses_list.as_view(),
         name = "Courses_List"),
    path("Master/<int:pk>/", views.Master_Detail.as_view(),
         name = "Master_Detail"),
    path("Manage/Master", views.Manage_Master.as_view(),
         name = "Manage_Master"),
    path("Manage/Member", views.Manage_Member.as_view(),
         name = "Manage_Member"),
    
    path("Manage/Course", views.Manage_Courses.as_view(),
         name = "Manage_Course"),
     
    path("Manage/note", views.Manage_Member.as_view(),
         name = "Manage_note"),

    path("Manage/blog", views.Manage_Member.as_view(),
         name = "Manage_blog"),

    path("Manage/University", views.Manage_Member.as_view(),
         name = "Manage_University"),

    path("Manage", views.Manage.as_view(), name= "Manage"),

    path("Manage/Master/del_Master/<int:pk>", views.delete_Master.as_view(),
         name = "del_Master"),
    path("Manage/Member/del_Member/<int:pk>", views.delete_Member.as_view(),
         name = "del_Member"),

    path("Edit_Master/<int:pk>", views.Update_Master.as_view(),
         name = "Edit_Master"),
]