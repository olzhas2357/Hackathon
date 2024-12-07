from rest_framework import viewsets
from .models import Category, Content
from .serializers import CategorySerializer, ContentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from users.permissions import IsTeacher
from rest_framework.permissions import IsAuthenticated

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsTeacher]  # Apply the custom permission
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

    @action(detail=True, methods=['get'])
    def preview(self, request, pk=None):
        content = self.get_object()
        if content.file:
            return Response({'preview_url': content.file.url})
        return Response({'error': 'No file available for preview'}, status=400)

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:  # Only teachers can create, update, or destroy
            permission_classes = [IsAuthenticated, IsTeacher]
        else:  # Students can only view
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]



