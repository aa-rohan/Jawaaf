from django.shortcuts import render, redirect
from .models import QuestionModel, CategoryModel, AnswerModel
from .forms import QuestionForm, AnswerForm
from django.http import HttpResponse

# Create your views here.


def questionlist(request):
    if 'id' in request.session:
        questions = QuestionModel.objects.all()
        questions_dict = {'questions': questions}
        return render(request, 'questionmodel_list.html', questions_dict)
    else:
        return redirect('user:login')


def popular(request):
    questions = QuestionModel.objects.filter(question_votes__gt=2)
    questions_dict = {'questions': questions}
    return render(request, 'popular.html', questions_dict)


def addquestion(request):
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('qna:read')
            except:
                return HttpResponse('Failed')
        else:
            print(form.errors)
            return HttpResponse('Form not Valid!')
    else:
        category = CategoryModel.objects.all
        return render(request, 'questionmodel_create.html', {'categories': category})


def update_question(request, id):
    question = QuestionModel.objects.get(id=id)
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            try:
                form.save()
                return redirect('qna:read')
            except:
                return HttpResponse('Failed')
        else:
            print(form.errors)
            return HttpResponse('Form not Valid!')
    else:
        form = QuestionForm(instance=question)
        return render(request, 'questionmodel_update.html', {'form': form})


def delete_question(request, id):
    question = QuestionModel.objects.get(id=id)
    question.delete()
    return redirect('qna:read')


def vote_question(request, id):
    question = QuestionModel.objects.get(id=id)
    question.question_votes += 1
    question.save()
    return redirect('qna:read')


def answer(request, id):
    if request.method == "POST":
        by = request.POST.get('answered_by')
        desc = request.POST.get('answer_desc')
        answer_img = request.POST.get('answer_img')
        question = QuestionModel.objects.get(id=id)
        Comment = AnswerModel(answered_by=by, answer_desc=desc,
                              answer_img=answer_img, question=question)
        Comment.save()
        return redirect('qna:read')
    else:
        form = AnswerForm
        a = {'form': form}
        b = {'id': id}
        c = {**a, **b}
        return render(request, 'answermodel_create.html', c)


def submit(request, id):
    if request.method == "POST":
        question = QuestionModel.objects.get(id=id)
        answer = request.POST.get('answer_desc')
        Comment = AnswerModel(question=question, answer_desc=answer)
        Comment.save()
        return redirect('qna:read')


def detail(request, id):
    return render(request, 'detail.html')

# class QuestionListViews(ListView):
#     queryset = QuestionModel.objects.all()
