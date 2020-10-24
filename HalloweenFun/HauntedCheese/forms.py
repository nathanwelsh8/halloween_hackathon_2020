
from django import forms
from django.contrib.auth.models import User, Todo
from django.forms import widgets
from HauntedCheese.models import Todo

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=150,
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'id': 'register_username', 'class':'form-control'}),
                               label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'id': 'register_password','class':'form-control'}),
                               label='')

    class Meta:
        model = User
        fields = ('username', 'password',)


class AddItem(forms.ModelForm):

    title = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'placeholder':"List Item Name", 'class':'form-control'}))
    description = forms.CharField(max_length=512, widget=forms.Textarea(attrs={'placeholder':'What spooky stuff do you need to do?', 'class':'form-control'}))  
    start = forms.DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"], widgets=forms.DateTimeInput(attrs={'class':'form-control'}))
    due = forms.DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"], widgets=forms.DateTimeInput(attrs={'class':'form-control'}))