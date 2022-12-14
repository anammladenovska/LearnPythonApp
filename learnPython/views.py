from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUsersForm


def firstPage(request):
    context = {}
    return render(request, 'firstPage.html', context)


def registerPage(request):
    form = CreateUsersForm

    if request.method == 'POST':
        form = CreateUsersForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Профилот е креиран за ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Внесените податоци се погрешни')
            context = {}
            return render(request, 'login.html', context)
    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def homePage(request):
    context = {}
    return render(request, 'home.html', context)


@login_required(login_url='login')
def materialsPage(request):
    all_lessons = Lesson.objects.filter(user=request.user).all()
    context = {'all_lessons': all_lessons}
    return render(request, 'materials.html', context=context)


@login_required(login_url='login')
def lessonX(request):
    all_lessons = Lesson.objects.filter(user=request.user).all()
    context = {'all_lessons': all_lessons}
    return render(request, 'lessonX.html', context=context)