from django import forms

class Create_Activities(forms.Form):
    activity_title = forms.CharField(max_length=50, required=True, help_text='Required.')
    location = forms.CharField(required=True, help_text='Required.')