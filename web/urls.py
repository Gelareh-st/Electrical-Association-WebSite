from django.contrib import admin
from django.urls import path, re_path

from web.models import Master, Members
from . import views

urlpatterns = [
    path(r"", views.Home, name = "Home"),
    path(r"Masters/", views.Master_list.as_view(),
         name="Master_view"),
    path(r"Members/", views.Members_list.as_view(),
         name="Members"),
    path(r"Courses/", views.Courses_list.as_view(),
         name = "Courses_List"),

    path("Member/<int:pk>/", views.Member_Detail.as_view(),
         name = "Member_Detail"),

    path("Master/<int:pk>/", views.Master_Detail.as_view(),
         name = "Master_Detail"),

    path("Manage/Master", views.Manage_Master.as_view(),
         name = "Manage_Master"),
    path("Manage/Member", views.Manage_Member.as_view(),
         name = "Manage_Members"),
    
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

    path("Edit_Member/<int:pk>", views.Update_People.as_view(), kwargs = dict(model = Members),
         name = "Edit_Member"),
    path("Edit_Master/<int:pk>", views.Update_People.as_view(), kwargs = dict(model = Master),
         name = "Edit_Master"),
    path("Like_Master/<int:pk>/", views.VoteOnMaster.as_view(), kwargs=dict(choice = "Like"), name = "Like_MASTER"),
    path("DisLike_Master/<int:pk>/", views.VoteOnMaster.as_view(), kwargs=dict(choice = "Dislike"), name = "DisLike_MASTER")
]