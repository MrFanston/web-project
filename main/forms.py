from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# форма создания пользователя
class CreateUserForm(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='подтверждение пароя', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # хз зачем
    class Meta:
        model = User
        fields = ['username', 'email', 'password1' , 'password2']
