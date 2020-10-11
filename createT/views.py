from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import CreateUserForm, TournamentForm, SimmetoxiForm
from .models import *
from django.contrib.auth.decorators import login_required
from .filters import TournamentFilter
from datetime import date
import datetime
# Create your views here.

@login_required(login_url='login')
def index(request):

    currentUser = request.user
    userType = currentUser.userType

    return render(request, 'createT/index.html', {'userType':userType, 'currentUser':currentUser})


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.danger(request, 'Account was created for ' + user +"." )
            return redirect('login')

    context = {'form':form}
    return render(request, 'createT/register.html', context)



@login_required(login_url='login')
def findTournament(request):
    today = date.today()
    dateTournament = Tournament.dateStart
    currentUser = request.user
    userType = currentUser.userType
    if userType == 1:
        messages.info(request, 'Υou are not authorized to access this page..')
        return redirect('index')
    tournaments = Tournament.objects.filter(dateStart__range=[today, "2080-01-31"])
    myFilter = TournamentFilter(request.GET, queryset=tournaments)
    tournaments = myFilter.qs
    context = {'tournaments':tournaments, 'myFilter':myFilter}
    return render(request, 'createT/findTournament.html',context)



@login_required(login_url='login')
def createTournament(request):
    currentUser = request.user
    userType = currentUser.userType
    if userType == 0:
        messages.error(request, 'Υou are not authorized to access this page..')
        return redirect('index')

    form = TournamentForm()

    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Tournament created successfully!!!')
            return redirect('index')
    context = {'form':form, 'currentUser':currentUser}

    return render(request, 'createT/createTournament.html', context)



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'createT/login.html', {})


def logoutPage(request):
    logout(request)
    return redirect('login')
    return render(request, 'createT/logout.html', {})

def tournamentInfo(request, pk_test):
    tournaments = Tournament.objects.get(id=pk_test)
    return render(request, 'createT/tournamentInfo.html', {'tournaments':tournaments})


def tournamentSubmit(request, pk_test):
    tournaments = Tournament.objects.get(id=pk_test)

    form = SimmetoxiForm()

    if request.method == 'POST':
        form = SimmetoxiForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Registration for the tournament was successful!!!')
            return redirect('index')

    return render(request, 'createT/tournamentSubmit.html', {'form:':form, 'tournaments':tournaments})


def trainingPage(request):
    today = date.today()
    context = {'today':today}
    return render(request, 'createT/training.html', context)
