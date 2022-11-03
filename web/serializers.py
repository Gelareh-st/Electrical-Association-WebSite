from rest_framework import (
                            serializers,
                            )
from .models import (
                     Courses,
                     )

class Courses_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = [
            'title', 'description', 'Unit', 
            'Prerequisite', 'Simultaneous'
                  ]