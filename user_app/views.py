from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse


def loginauth(request):
    if request.method == "POST":
        email = request.POST.get('email')
        code = request.POST.get('pass')
        user = UserModel.objects.filter(email=email, password=code)
        if user.count() > 0:
            validuser = user[0]
            request.session['email'] = validuser.email
            request.session['id'] = validuser.id
            request.session['name'] = validuser.name
            return redirect('qna:read')
        else:
            return HttpResponse("Wrong Credentials.")

    else:
        return render(request, 'login.html')


def logout(request):
    request.session.flush()
    return redirect('user:login')
