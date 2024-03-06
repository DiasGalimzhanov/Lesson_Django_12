from django import forms
from .models import Person

class Forms(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'birth_date', 'work_place', 'salary', 'gender']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control','id': 'validationCustom01', 'required': 'true', 'placeholder': 'Name'}),
            'work_place' : forms.TextInput(attrs={'class': 'form-control','id': 'validationCustom01', 'required': 'true', 'placeholder': 'Work place'}),
            'salary' : forms.NumberInput(attrs={'class': 'form-control','id': 'validationCustom01', 'required': 'true', 'placeholder': 'Salary'}),
            'gender' : forms.Select(attrs={'class': 'form-control','id': 'validationCustom01', 'required': 'true', 'placeholder': 'Gender'}),
            'birth_date' : forms.DateInput(attrs={'type': 'date', 'class': 'form-control','id': 'validationCustom01', 'required': 'true', 'placeholder': 'Birth date'}),
        }


