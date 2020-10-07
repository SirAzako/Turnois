from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import*



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'userType']

class TournamentForm (ModelForm):
	class Meta:
		model = Tournament

		fields = ['name', 'dateStart', 'dateEnd', 'Tournament_Type', 'location', 'regPrice', 'Prize', 'PpT']


class SimmetoxiForm (ModelForm):
	class Meta:
		model = Simmetoxi

		fields = ['teamName', 'phone']
