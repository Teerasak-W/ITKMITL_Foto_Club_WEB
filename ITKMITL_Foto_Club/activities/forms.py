from django import forms

class Request_Activities(forms.Form):
    request_title = forms.CharField(max_length=50)
    location = forms.CharField()
    # picture_path = forms.URLField(max_length = 500) 
    detail = forms.CharField(widget=forms.Textarea)

class Request_Contact(forms.Form):
    contact_person = forms.CharField(max_length=50)
    contact_number = forms.CharField(max_length=10)

class Request_Datetime(forms.Form):
    start_time = forms.DateTimeField()
    finish_time = forms.DateTimeField()