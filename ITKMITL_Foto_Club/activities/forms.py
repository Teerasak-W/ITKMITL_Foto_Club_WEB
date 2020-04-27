from django import forms

class Request_Activities(forms.Form):
    request_title = forms.CharField(max_length=50)
    location = forms.CharField()
    picture_path = forms.FileField(required=False)
    detail = forms.CharField(widget=forms.Textarea)

class Request_Contact(forms.Form):
    contact_person = forms.CharField(max_length=50,required=True, help_text='Name')
    contact_number = forms.CharField(max_length=10,required=True, help_text='Phone number')

class Request_Datetime(forms.Form):
    start_time = forms.DateTimeField(input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT%H:%M')
    )
    finish_time = forms.DateTimeField(input_formats = ['%Y-%m-%dT%H:%M'],
        widget = forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'},
            format='%Y-%m-%dT%H:%M')
    )
