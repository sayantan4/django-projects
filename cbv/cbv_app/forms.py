from django import forms
from cbv_app.models import School
from cbv_app.models import Student

class school_form(forms.ModelForm):
    class Meta():
        model=School
        fields=('name','principal','location')

class student_form(forms.ModelForm):
    class Meta():
      model=Student
      fields=('name','age','school')
