from django.conf import settings
from django.db import models





class Question(models.Model):
    question = models.CharField(max_length=50, unique=True)
    
class Choice(models.Model):
    question = models.ForeignKey('Question', related_name='choices', on_delete=models.CASCADE)
    choice = models.ImageField()
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