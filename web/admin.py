from django.contrib import admin
from web.models import Courses, Master, Members, People
class PeopleAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'EmailAddress',
                    'LinkedIn', 'GitHub', 'created_date', 'created_date'
                    , 'Picture_URL']
    search_fields = ["category", 'name', 'EmailAddress']
admin.site.register(People, PeopleAdmin)

class CoursesAdmin(admin.ModelAdmin):
    list_display = ['title', 'Unit', 'Prerequisite',
                    'Simultaneous' , 'created_date', 'updated_date']
    search_fields = ['title', 'Unit']
admin.site.register(Courses, CoursesAdmin)

class MasterAdmin(admin.ModelAdmin):
    list_display = ['Info', 'Performance_result', 'get_Courses']
    def get_Courses(Self, instance):
        return [course.title for course in instance.courses.all()]
admin.site.register(Master, MasterAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ['get_Info', 'position']
    def get_Info(self, instance):
        return f"{instance.Info.name}, {instance.Info.created_date}"
admin.site.register(Members, MemberAdmin)
