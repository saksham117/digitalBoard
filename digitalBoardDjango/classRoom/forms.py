from django import forms

class CreateClassRoom(forms.Form):
    class_Name = forms.CharField(max_length=100, required=True)
    course_ID = forms.CharField(max_length=50, required=True)


