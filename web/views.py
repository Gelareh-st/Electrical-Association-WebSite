from contextlib import nullcontext
from http.client import HTTPResponse
import json
import requests
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import (
            render,
            redirect,
            get_object_or_404
            )
from rest_framework.response import Response
from rest_framework import (
                    views,
                    viewsets,
                    permissions
                            )
from .serializers import(
                        Courses_Serializer,
                        )
from django.contrib.auth.mixins import (
            LoginRequiredMixin,
            PermissionRequiredMixin
            )
from web.forms import (
            CoursesForm,
            MasterForm,
            PeopleForm,
            MembersForm
            )
from web.Auxiliary_functions import (
             get_initial,
             get_urls
             )
from django.urls import reverse_lazy
from django.views import (
             View,
             generic
             )
from web.models import (Courses,
            Master, Master_Performance_Vote,
            Members,
            People
            )

message_url = "http://localhost:8000/apimessage/"
#returns Home Page And its Contents Data
def Home(request):
    return render(request, "index.html", {"status": "OK"})

#-------------------------------------------------------------
"""Masters Control And Render View
   IN CONTROL  View The Website Manager Must Loged In / Features : Create/Edit/Delete
"""
#-----------------------------------------------------------------
class Objects_ListView(View):
    def get_queryset(self, request):
        modelname = self.model._meta.verbose_name.title().lower()
        stuff     = self.model.objects.all()
        cntx      = {modelname+'_list':stuff}
        return render(request,'index.html', cntx)
#-----------------------------------------------------------------
#View`s For Lising Objects and Showing their Detailes

class Master_list(generic.ListView):
    
    model = Master
    template_name = "index.html"
    context_object_name = "Masters_List"

class Members_list(generic.ListView):
    model = Members
    context_object_name = "Members_List"
    template_name = "index.html"

class Courses_list(generic.ListView):
    model = Courses
    context_object_name = "Courses_List"
    template_name = "index.html"

class Master_Detail(generic.DetailView):
    model = Master
    template_name = "prof.html"
    context_object_name = "prof"
    def vote_status(self, request, kwargs):
        return requests.get(f"Like_Master/{kwargs['pk']}")
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['liked'] = False
        context['disliked'] = False
        if self.vote_status:
            context['liked'] = True
        return self.render_to_response(context)
# LIKE OR DISLIKE THE MASTER VIEW
class VoteOnMaster(views.APIView):
    #aPI view for create a vote on master
    Model = Master
    def get_master(self, request, **kwargs):
        master = Master.objects.get(id = kwargs["pk"])
        return master 

    def get(self, request, **kwargs):
        Voter = request.session.session_key
        master = self.get_master(request, **kwargs)        
        voted = Master_Performance_Vote.objects.filter(voter = Voter, master = master)
        if voted:
            print(voted[0].vote)
            Result = dict({'voted one': voted[0].master.Info.name, 'liked': voted[0].vote == 'Like',
                        'dislike': voted[0].vote == 'Dislike', 'Voter_Session_Key': voted[0].voter})   
        else:
            Result = None
        return Response(Result)
    def post(self, request, **kwargs):
        master = self.get_master(request, **kwargs)
        Voter = request.session.session_key
        # check the existance of the MPV object , its returns a list of filtered objects
        existance = Master_Performance_Vote.objects.filter(voter = Voter, master = master)
        choice = kwargs['choice']
        if not existance:
            obj = Master_Performance_Vote.objects.create(master = master)
            obj.voter = request.session.session_key
            obj.vote = choice
            obj.save()
            return Response({'status_code':200})
        elif choice != existance[0].vote:
            existance[0].vote = choice
            existance[0].save()
            return Response({'status_code':201})
        else:
            existance[0].delete()
            return Response({'status_code':202})

class Member_Detail(generic.DetailView):
    model = Members
    template_name = "prof.html"
    context_object_name = "prof"
class Course_Detail(generic.DetailView):
    model = Courses
    template_name = "course.html"
    context_object_name = "Course"

#-------------------------------------------------------------------
#generic views for Creating Objects

#decide Choices for diffrent People
class Manage_Master(LoginRequiredMixin, generic.TemplateView):
    #TO DO
        #IF A MASTER EXIST RAISE AN ERROR AND HANDL IT
    http_method_names = ["get", "post", "delete"]
    template_name = "manage_members.html"
    success_url = reverse_lazy('Manage_Master')
    model = Master
    Master_Form = MasterForm()
    People_Form = PeopleForm()
    def get_context_data(self, **kwargs):
        #clear()
        #append(("Faculty" , "Faculty"))
        context = super().get_context_data(**kwargs)
        context['Items'] = Master.objects.all()
        context['Master_Form'] = self.Master_Form
        context['People_Form'] = self.People_Form
        context['courses'] = Courses.objects.all()
        context['Delete_Address'] = "del_Master"
        context['Edit_Address'] = "Edit_Master"
        context['Edit'] = False
        context['title'] = "مدیریت اساتید"
        context['ShowAddress'] = "Master_Detail"
        return context
    
    def post(self, request, **kwargs):
        #default category is Faculty
        #For Create A Master Object if Expected People Object exists just create Master Object
        People_Form = PeopleForm(request.POST)
        Master_Form = MasterForm(request.POST)
        if People_Form.is_valid():
            Person = People_Form
            Person.save()
            Person = People.objects.get(name = request.POST["name"])
        else:
            Person = People.objects.get(name = request.POST["name"])

        Masters = Master_Form.save(commit=False)
        Masters.Info = Person
        Masters.save()
        print("Hey")
        if Masters:
            requests.post(message_url, {"message":"Master Added..."})
        else:
            requests.post(message_url, {"message":"Failed"})
        Masters.save()
        return redirect('Manage_Master')

class delete_Master(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView,
                    SuccessMessageMixin
                    ):
    model = Master
    success_url = reverse_lazy("Manage_Master")
    permission_required = "Master.delete_post"
    success_message = {"message":"object_deleted_successfuly"}
    

class Manage_Member(generic.TemplateView, SuccessMessageMixin):
    
    template_name = "manage_members.html"
    context_object_name = "Items"
    fields = ['Info', 'position']
    fail_message  = "Member is Repeative or Invalid..."
    success_message = "Member added successfully..."
    
    def get_context_data(self,   **kwargs):
        context = super().get_context_data(**kwargs)
        context["People_Form"] = PeopleForm()
        context["Members_Form"]=MembersForm()
        context["Items"] = Members.objects.all()
        context['Delete_Address'] = "del_Member"
        context['Edit_Address'] = "Edit_Member"
        context['Edit'] = False
        context['title'] = "مدیریت اعضای انجمن"
        context['ShowAddress'] = "Member_Detail"
        return context

    def post(self, request, **kwargs):
        People_Form = PeopleForm(request.POST)
        Member_Form = MembersForm(request.POST)
        if People_Form.is_valid():
            Person = People_Form.save()
            Person.category = "Member"
            Person.save()
        else:
            Person = People.objects.get(name = request.POST["name"])
    #  Member = Members.objects.create(position = request.POST['position'], Info = Person)
        Member = Member_Form.save(commit=False)
        Member.Info = Person
        Member.save()
        if Member:
            requests.post(message_url, {"message":"Member Added..."})
        else:
            requests.post(message_url, {"message":"Failed"})
        Member.save()
        return redirect("Manage_Members")

class delete_Member(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView,
                    ):
    #need a layout template for manage objects and inherit them for others
    model = Members
    success_url = reverse_lazy("Manage_Members")
    permission_required = "Members.delete_post"
    success_message = {"message":"object_deleted_successfuly"}

#Forms for define the form that we using    
forms = {"Master_Form": MasterForm, "Members_Form": MembersForm}
class Update_People(LoginRequiredMixin ,generic.TemplateView):
    template_name = "Edit_People.html"
    People_Form = PeopleForm()
    Master_Form = MasterForm()

    def get_context_data(self, **kwargs):
        child_initials = {}
        model = kwargs["model"]
        child_form = forms[f"{model.__name__}_Form"]
        context = super().get_context_data(**kwargs)
        obj = model.objects.get(id = kwargs['pk'])
        context['Items'] = model.objects.all()
        context[f'{model.__name__}_Form'] = child_form(initial = get_initial(model, obj))
        
        context['People_Form'] = PeopleForm(initial={'name':obj.Info.name, 'EmailAddress':obj.Info.EmailAddress, 'Picture_URL':obj.Info.Picture_URL,
                                                       'LinkedIn':obj.Info.LinkedIn, 'GitHub':obj.Info.GitHub})
        context['courses'] = Courses.objects.all()
        context['Delete_Address'] = f"del_{model.__name__}"
        context['Edit_Address'] = f"Edit_{model.__name__}"
        context['Edit'] = True
        context['title'] = f"Edit {model.__name__} Object"
        return context
    def post(self, request,  **kwargs):
        model = kwargs["model"]
        print(request.session)
        child_obj = model.objects.get(id = kwargs["pk"])
        instance = get_object_or_404(People, id = child_obj.Info.id)
        #Person Update Info
        person = PeopleForm(request.POST or None, instance = instance)
        child_update_info = forms[f"{model.__name__}_Form"](request.POST, instance = child_obj)
        if person.is_valid():
            person.save()
        if child_update_info.is_valid():
            child_update_info.save()
        return redirect(f"Manage_{model.__name__}")

# """
# Update Performance Result Field Of Master Object Seperately without access any other fields
# """
# class Performance_result(generic.UpdateView):
#     model = Master

#Procees Required Data For Main Page OF Admin View , Generic, regex
sessionss = []
class Manage(LoginRequiredMixin,
             SuccessMessageMixin,
             generic.TemplateView):
    template_name = "manage.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_patterns'] = get_urls()
        return context


class Manage_Courses(LoginRequiredMixin, generic.TemplateView):
    form_class = CoursesForm
    model = Courses
    template_name = "manage_Courses.html"
    def get_context_data(self, **kwargs):
        field_names = map(lambda item : item.name, list(self.model._meta.fields))
        kwargs.update(dict(fields_list = field_names))
        kwargs.update(dict(object_list = self.model.objects.all()))
        kwargs.update(dict(Edit = False))
        kwargs.update(dict(model_name = self.model.__name__))
        kwargs.update(dict(Show_Address = 'Course_Detail'))
        kwargs.update(dict(create_address = 'Create_Course'))
        kwargs.update(dict(edit_address = 'Edit_Course'))
        kwargs.update(dict(delete_address = 'Delete_Course'))
        kwargs.update(dict(Form = self.form_class))
        print(f"object fields: {self.model._meta.fields}")
        return super().get_context_data(**kwargs)

class Create_Courses(LoginRequiredMixin, generic.CreateView):
    model = Courses
    form_class = CoursesForm
    queryset = Courses.objects.all()
    success_url = reverse_lazy('Manage_Course')

class DeleteCourse(LoginRequiredMixin, generic.DeleteView): 
    #need a layout template for manage objects and inherit them for others
    model = Courses
    fields = [
        'title', 'description', 'tendency', 'Unit', 'Prerequisite', 'Simultaneous'
    ]
    success_url = reverse_lazy("Manage_Course")
    permission_required = "Members.delete_post"
    success_message = {"message":"object_deleted_successfuly"}


class Update_Course(LoginRequiredMixin ,generic.TemplateView):
    template_name = "Edit_Course.html"
    def get_context_data(self, **kwargs):
        model = kwargs["model"]
        context = super().get_context_data(**kwargs)
        obj = model.objects.get(id = kwargs['pk'])
        context['Items'] = model.objects.all()
        context['Form'] = CoursesForm(initial = {'title' :obj.title, 'description': obj.description, 
                                               'tendency': obj.tendency, 'Unit': obj.Unit, 'Prerequisite': obj.Prerequisite, 'Simultaneous': obj.Simultaneous})
        context['courses'] = Courses.objects.all()
        context['Edit'] = True
        context['title'] = f"Edit {model.__name__} Object"
        return context
    def post(self, request, **kwargs):
        model = kwargs["model"]
        instance = get_object_or_404(Courses, id = kwargs['pk'])
        course = CoursesForm(request.POST or None, instance = instance)
        if course.is_valid():
            course.save()
        else : 
            return HTTPResponse("Somthing get Wrong Try Again")
        return redirect("Manage_Course")

class Manage_Courses(LoginRequiredMixin, generic.TemplateView):
    form_class = CoursesForm
    model = Courses
    template_name = "manage_Courses.html"
    def get_context_data(self, **kwargs):
        field_names = map(lambda item : item.name, list(self.model._meta.fields))
        kwargs.update(dict(fields_list = field_names))
        kwargs.update(dict(object_list = self.model.objects.all()))
        kwargs.update(dict(Edit = False))
        kwargs.update(dict(model_name = self.model.__name__))
        kwargs.update(dict(Show_Address = 'Course_Detail'))
        kwargs.update(dict(create_address = 'Create_Course'))
        kwargs.update(dict(edit_address = 'Edit_Course'))
        kwargs.update(dict(delete_address = 'Delete_Course'))
        kwargs.update(dict(Form = self.form_class))
        print(f"object fields: {self.model._meta.fields}")
        return super().get_context_data(**kwargs)

class Create_Semester_Object(LoginRequiredMixin, generic.CreateView):
    pass



