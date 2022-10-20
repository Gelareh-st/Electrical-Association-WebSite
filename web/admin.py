from django.contrib import admin
from web.models import Courses, Master, Master_Performance_Vote, Members, People
class PeopleAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'EmailAddress',
                    'LinkedIn', 'GitHub', 'created_date', 'update_date']
    search_fields = ["category", 'name', 'EmailAddress']
admin.site.register(People, PeopleAdmin)

class CoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'Unit', 'Prerequisite',
                    'Simultaneous' , 'created_date', 'updated_date']
    search_fields = ['title', 'Unit']
admin.site.register(Courses, CoursesAdmin)

class MasterAdmin(admin.ModelAdmin):
    list_display = ['name', 'EmailAddress','created_date', 'update_date', 'role', 
                    'votes', 'Performance_result', 'About' , 'get_Courses']
    def get_Courses(Self, instance):
        return [course.title for course in instance.courses.all()]
    def name(Self, instance):
        return f"{instance.Info.name}"
    def EmailAddress(Self, instance):
        return instance.Info.EmailAddress
    def created_date(Self, instance):
        return instance.Info.created_date
    def update_date(Self, instance):
        return instance.Info.update_date
        
admin.site.register(Master, MasterAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'EmailAddress','created_date', 'update_date',
                    'position']
    def name(Self, instance):
        return f"{instance.Info.name}"
    def EmailAddress(Self, instance):
        return instance.Info.EmailAddress
    def created_date(Self, instance):
        return instance.Info.created_date
    def update_date(Self, instance):
        return instance.Info.update_date
admin.site.register(Members, MemberAdmin)

class Master_PVAdmin(admin.ModelAdmin):
    list_display = ['get_master', 'vote']
    def get_master(self, instance):
        return f"{instance.master.Info.name}, {instance.master.Info.created_date}"
admin.site.register(Master_Performance_Vote, Master_PVAdmin)