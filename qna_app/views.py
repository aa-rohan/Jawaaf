from django.shortcuts import render
from .models import QuestionModel, AnswerModel

# Create your views here.


def questions(request):
    questions = QuestionModel.objects.all()
    questions_dict = {'questions': questions}
    return render(request, 'questions.html', questions_dict)
