from django.db import models

class Assignment(models.Model):
    ASSIGNMENT_TYPES = [
        ('fill_in_blank', 'Fill in the Blank'),
        ('matching', 'Matching'),
        ('multiple_choice', 'Multiple Choice'),
        ('audio_question', 'Audio Question'),
    ]
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=ASSIGNMENT_TYPES)
    question = models.TextField()
    correct_answer = models.JSONField()  # Stores structured answers
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def check_answer(self, user_answer):
        if self.type == 'fill_in_blank':
            return user_answer.strip() == self.correct_answer.get('text', '').strip()
        elif self.type == 'matching':
            return user_answer == self.correct_answer.get('pairs', [])
        elif self.type == 'multiple_choice':
            return user_answer == self.correct_answer.get('option', None)
        elif self.type == 'audio_question':
            return user_answer == self.correct_answer.get('response', None)
        return False
