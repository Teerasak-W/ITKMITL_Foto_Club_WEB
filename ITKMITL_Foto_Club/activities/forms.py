from django import forms

class Create_Activities(forms.Form):
    activity_title = forms.CharField(max_length=50, required=True, help_text='Required.')
    location = forms.CharField(required=True, help_text='Required.')

class Request_Activities(forms.Form):
    request_title = forms.CharField(max_length=50)
    location = forms.CharField()
    # picture_path = forms.URLField(max_length = 500) 
    detail = forms.CharField(widget=forms.Textarea)

class Request_Contact(forms.Form):
    contact_person = forms.CharField(max_length=50)
    contact_number = forms.CharField(max_length=10)

class Request_Datetime(forms.Form):
    start_time = forms.DateTimeField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    finish_time = forms.DateTimeField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))