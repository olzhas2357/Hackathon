from rest_framework import serializers
from .models import Lesson
from content.serializers import ContentSerializer
from assignments.serializers import AssignmentSerializer

class LessonSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)
    assignments = AssignmentSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'
