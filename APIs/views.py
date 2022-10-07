from urllib import request
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import (
                    views,
                    viewsets,
                    permissions
                            )
from .models import(
                    Event,
                   )
from .serializers import(
                        Event_Serializer,
                        )

class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Show, create, edit or delete the Event Object
    """
    queryset = Event.objects.all().order_by('created_date')
    serializer_class = Event_Serializer
    permission_classes = [permissions.IsAuthenticated]


class message(views.APIView):
    message = []
    def get(self, request):
        response = {"message": self.message[0]}
        return Response(response)
    def post(self, request):
        self.message.insert(0, request.POST["message"])
        return Response({'status_code':200})