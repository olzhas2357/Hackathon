from argparse import Action
from rest_framework import viewsets
from .models import Assignment
from .serializers import AssignmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    
    @action(detail=True, methods=['post'])
    def check(self, request, pk=None):
        assignment = self.get_object()
        user_answer = request.data.get('answer')
        is_correct = assignment.check_answer(user_answer)
        return Response({'is_correct': is_correct})
