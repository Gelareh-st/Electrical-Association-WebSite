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

def get_initial(model, obj):
    if model.__name__== "Master":
        initial = {"Resume_Link": obj.Resume_Link}
    else:
        initial = {"position": obj.position}
    return initial