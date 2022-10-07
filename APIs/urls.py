from django.urls import(
                        include,
                        path,
                        )
from rest_framework import(
                        routers,
                        )
from . import(
              views,
              )
#Wire Up the Api`s using routers
router = routers.DefaultRouter()
router.register(r'Events', views.EventViewSet, basename="Events")

urlpatterns =[
    path('', include(router.urls), name = 'Events'),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('message/', views.message.as_view(), name = 'message')
]