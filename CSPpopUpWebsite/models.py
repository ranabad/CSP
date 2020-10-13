from django.conf import settings
from django.db import models
from django.utils import timezone



class Question(models.Model):
    question = models.CharField(max_length=50, unique=True)
    timezone
class Choice(models.Model):
    question = models.ForeignKey('Question', related_name='choices', on_delete=models.CASCADE)
    choice = models.ImageField(upload_to = 'example/', default = 'example/')
    position = models.IntegerField('position')
   #StackOverFlow credit
class Meta:
        unique_together = [
            # no duplicated choice per question
            ('question', 'choice'), 
            # no duplicated position per question 
            ("question", "position") 
        ]
        ordering = ("position",)   