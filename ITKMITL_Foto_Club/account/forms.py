from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Sign_Up(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=50, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254,required=True, help_text='Required. Inform a valid email address.')
    student_id = forms.CharField(max_length=8, required=True, help_text='Required.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','student_id', 'email', 'password1', 'password2', )