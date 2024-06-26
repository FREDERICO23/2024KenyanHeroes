from django import forms
from .models import Hero

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['name', 'alias', 'photo', 'dob', 'killed', 'familynumber']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'alias': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'killed': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'familynumber': forms.NumberInput(attrs={'class': 'form-control'}),
        }