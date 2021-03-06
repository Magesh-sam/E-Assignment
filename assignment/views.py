from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
from .forms import CreateUserForm, AssignmentForm, DocumentForm
from .models import *
from .decorators import unauthenticated_user, allowed_users


@unauthenticated_user
def registerpage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'assignment/register.html', context)


@unauthenticated_user
def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('faculty')
            elif user.is_active:
                login(request, user)
                return redirect('home')
        else:
            messages.success(request, 'Username or Password is Incorrect!')

    return render(request, 'assignment/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def home(request):
    assignments = Assignment.objects.all()
    documents = Document.objects.all()
    context = {'assignments': assignments, 'documents': documents}
    return render(request, 'assignment/dashboard.html', context)


@login_required(login_url='login')
def about(request):
    return render(request, 'assignment/about.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def faculty(request):
    assignments = Assignment.objects.all()
    documents = Document.objects.all()
    context = {'assignments': assignments, 'documents': documents, }
    if User.is_superuser:
        return render(request, 'assignment/faculty.html', context)
    else:
        return HttpResponse('You are not authorized to view this page')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createassignment(request):
    form = AssignmentForm()
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty')
    context = {'form': form}
    return render(request, 'assignment/create_assignment.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateassignment(request, pk):
    assignment = Assignment.objects.get(id=pk)
    form = AssignmentForm(instance=assignment)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('faculty')
    context = {'form': form}
    return render(request, 'assignment/create_assignment.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteassignment(request, pk):
    assignment = Assignment.objects.get(id=pk)
    if request.method == 'POST':
        assignment.delete()
        return redirect('faculty')
    context = {'item': assignment}
    return render(request, 'assignment/delete.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = DocumentForm()
    return render(request, 'assignment/simple_upload.html', {
        'form': form
    })
