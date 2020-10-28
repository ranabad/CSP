from django.conf import settings
from django.db import models


class Quiz(models.Model):
	ageGroup = models.CharField(max_length=100)
	roll_out = models.BooleanField(default=False)

class Question(models.Model):
    quiz = models.ForeignKey('Quiz',related_name='quiz' ,on_delete=models.CASCADE, default=0)
    question = models.CharField(max_length=50, unique=True)
    order = models.IntegerField(default=0,null=False)
        
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