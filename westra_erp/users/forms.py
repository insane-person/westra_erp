from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    patronymic = forms.CharField(max_length=12, min_length=4, required=True, help_text='Patronymic',
                               widget=(forms.TextInput(attrs={'class': 'form-control'})))
    birth_date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'patronymic', 'birth_date', 'password1', 'password2')