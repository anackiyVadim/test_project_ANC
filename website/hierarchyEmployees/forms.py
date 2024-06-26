from django import forms

from .models import Employee


class OptionsEmploeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'surname', 'surname_patronymic', 'data_admission', 'email', 'position', 'supervisor']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'surname_patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'data_admission': forms.DateInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'supervisor': forms.Select(attrs={'class': 'form-control'}),
        }
