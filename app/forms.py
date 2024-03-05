from django import forms
from .models import Person

class Forms(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'birth_date', 'work_place', 'salary', 'gender']
        widgets = {
            'birth_date' : forms.DateInput(attrs={'type': 'date'}),
        }


