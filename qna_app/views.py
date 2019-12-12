from django.shortcuts import render
from .models import QuestionModel

# Create your views here.


def questions(request):
    questions = QuestionModel.objects.all()
    questions_dict = {'questions': questions}
    return render(request, 'questions.html', questions_dict)


def popular(request):
    questions = QuestionModel.objects.filter(question_votes__gt=2)
    questions_dict = {'questions': questions}
    return render(request, 'popular.html', questions_dict)
