from django import forms

class Create_Activities(forms.Form):
    activity_title = forms.CharField(max_length=50, required=True, help_text='Required.')
    location = forms.CharField(required=True, help_text='Required.')

class Request_Activities(forms.Form):
    request_title = forms.CharField(max_length=50)
    location = forms.CharField()
    # picture_path = forms.URLField(max_length = 500) 
    detail = forms.CharField(widget=forms.Textarea)