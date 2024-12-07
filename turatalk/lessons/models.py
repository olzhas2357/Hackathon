from django.db import models
from content.models import Content
from assignments.models import Assignment

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    contents = models.ManyToManyField(Content)
    assignments = models.ManyToManyField(Assignment)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
