from rest_framework import serializers
from .models import Event

class Event_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["Title", "Decription", "Poster", "Proposal",
                "registry_start", "registry_end",
                 ]