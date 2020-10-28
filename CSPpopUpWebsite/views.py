from django.shortcuts import render
from .models import Question, Choice,Quiz
# Create your views here.
def mcq(request):
 quiz=Quiz.objects.all()
 question=Question.objects.all()
 choice=Choice.objects.all()
 
 return render(request, 'CSPpopUpWebsite/testView.html', {'question':question, 'choice':choice,'quiz':quiz})

 