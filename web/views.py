import requests
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import (
            render,
            redirect,
            get_object_or_404
            )
from django.contrib.auth.mixins import (
            LoginRequiredMixin,
            PermissionRequiredMixin
            )
from web.forms import (
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
            Master,
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
class Member_Detail(generic.DetailView):
    model = Members
    template_name = "prof.html"
    context_object_name = "prof"
class Course_Detail(generic.DetailView):
    model = Courses
    template_name = "index.html"
    context_object_name = "Courses_Detail"

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
    
    def get_context_data(self):
        context = {"Address": "del_Member"}
        return context


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

"""
Update Performance Result Field Of Master Object Seperately without access any other fields
"""
class Performance_result(generic.UpdateView):
    model = Master

#Procees Required Data For Main Page OF Admin View , Generic, regex

class Manage(LoginRequiredMixin,
             SuccessMessageMixin,
             generic.TemplateView):
    template_name = "manage.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_patterns'] = get_urls()
        return context
# class notfound(generic.TemplateView):
#     template_name = "manage_members.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['picture'] = "Picture"
#         return context
# Manage Cousrses CRUD
class Manage_Courses(LoginRequiredMixin, generic.CreateView):
    model = Courses
    template_name = "manage_members.html"
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)