from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Exam, Question, Choice, Result

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Result)
