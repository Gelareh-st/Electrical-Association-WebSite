from . import urls
import re
#Return URl Name
#---------------------------------------------------------------------
def get_urls():
    url_patterns = list(map(lambda x: x.name, urls.urlpatterns))
    regex_checker = re.compile("Manage_+.")
    filtered_patterns = list(filter(regex_checker.match, url_patterns))
    return filtered_patterns
#----------------------------------------------------------------------

#Return Initial Fields as a dictionary for Member and Master Model
from django.forms.models import model_to_dict
def get_initial(model, obj):
    initials = {
                'People': model_to_dict(obj, fields=['name', 'Picture_URL', 'EmailAddress','LinkedIn', 'GitHub']),
                          
                'Master':
                            model_to_dict(obj, fields = ['Resume_Linke', 'About'])
                         ,
                'Members': 
                            model_to_dict(obj, fields = ['position'])
                           ,
                'Courses': 
                            model_to_dict(obj, fields = ['title', 'description', 'tendency', 'Unit',
                                            'Prerequisite', 'Simultaneous'])
                           ,
                'semester_courses':
                            model_to_dict(obj, fields =['master', 'course', 'notes', 'start'])
                           ,
                }
    return initials[model]

            


def choice_Maker(model):
    print(type(list(model.objects.all())[0]))
    choices = list(map(lambda item: (item, item), list(model.objects.all())))
    print('There')
    print(type(choices[0][0]))
    return choices
