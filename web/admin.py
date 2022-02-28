from django.contrib import admin
from web.models import Courses, Master, Members, People
admin.site.register(People)
admin.site.register(Master)
admin.site.register(Courses)
admin.site.register(Members)