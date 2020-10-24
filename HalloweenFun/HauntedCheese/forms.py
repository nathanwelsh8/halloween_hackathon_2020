
from django import forms
from django.contrib.auth.models import User
from spatulaApp.models import Todo, TodoIterator

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=150,
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'id': 'register_username', 'class':'form-control'}),
                               label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'id': 'register_password','class':'form-control'}),
                               label='')

    class Meta:
        model = User
        fields = ('username', 'password',)

