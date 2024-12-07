from rest_framework import viewsets
from .models import Lesson
from .serializers import LessonSerializer
from users.permissions import IsTeacher  # Import the custom permission
from rest_framework.permissions import IsAuthenticated

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:  # Only teachers can create, update, or destroy
            permission_classes = [IsAuthenticated, IsTeacher]
        else:  # Students can only view
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    

