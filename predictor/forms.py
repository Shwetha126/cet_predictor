from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Marks

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['cet_marks', 'puc_marks']
