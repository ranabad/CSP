from django.contrib import admin
from .models import Question,Choice,Quiz
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
