from django.shortcuts import render
from .models import Question, Choice
# Create your views here.
def mcq(request):
 question=Question.objects.all()
 choice=Choice.objects.all()
 
 return render(request, 'CSPpopUpWebsite/testView.html', {'question':question, 'choice':choice})

 