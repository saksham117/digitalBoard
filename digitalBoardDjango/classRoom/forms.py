from django import forms
from django.forms.widgets import NumberInput # for displaying calendar

# form for creating class using form api
class CreateClassRoom(forms.Form):
    class_Name = forms.CharField(max_length=100, required=True)
    course_ID = forms.CharField(max_length=50, required=True)

# form for joining class using form api
class JoinClassRoom(forms.Form):
    class_Code = forms.CharField(max_length=6, required=True)


class CreateAssignmentForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        }
    ))
    description = forms.CharField(required=False,widget=forms.TextInput( 
        attrs={
            'class':'form-control',
            }
    ))
    submission_date = forms.DateField(widget=NumberInput(
        attrs={
            'type': 'date',
            'class':'form-control',
            }
    ))
    attachments = forms.FileField(required=False, widget=forms.ClearableFileInput(
        attrs={
        'class':'form-control-file',
        }
    ))
    pin_item = forms.BooleanField(required=False, widget=forms.CheckboxInput(

    ))


class SubmitAssignmentForm(forms.Form):
    
    attachments = forms.FileField(required=True, widget=forms.ClearableFileInput(
        attrs={
        'class':'form-control-file',
        }
    ))

    comment = forms.CharField(required=False,widget=forms.TextInput( 
        attrs={
            'class':'form-control',
            }
    ))
