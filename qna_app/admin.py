from django.contrib import admin
from .models import AnswerModel, QuestionModel


# Register your models here.
admin.site.register(QuestionModel)
admin.site.register(AnswerModel)
