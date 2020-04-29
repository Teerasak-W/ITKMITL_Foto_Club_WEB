from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from account.models import Equipment, suggestion


class Sign_Up(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=50, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254,required=True, help_text='Required. Inform a valid email address.')
    student_id = forms.CharField(max_length=8, required=True, help_text='Required.')
    pass_code = forms.CharField(max_length=5,required=True, help_text='Required 5 digit.')
    picture = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','student_id', 'email', 'password1', 'password2', 'pass_code', 'picture')

class suggestionForm(ModelForm):
    class Meta:
        model = suggestion
        fields = '__all__'


type_for = (
    ('0', 'camera'),
    ('1', 'lens'),
    ('2', 'light'),
    ('3', 'other')
    )

class EquipmentForm(ModelForm): 
    equipment_type = forms.ChoiceField(choices=type_for)
    equipment_title = forms.CharField(max_length=50, required=False)
    equipment_detail = forms.CharField(required=False)
    del_flag = forms.BooleanField(initial=False, required=False)
    equip_id = forms.CharField(widget = forms.HiddenInput, required=False)
    class Meta:
        model = Equipment
        exclude = ['user_id']