from django import forms

from .models import database


class SignUpForm(forms.ModelForm):
    class Meta:
        model=database
        fields="__all__"
        widgets={
            'user_name':forms.TextInput(attrs={'class': 'form-control'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'Email':forms.EmailInput(attrs={'class': 'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }