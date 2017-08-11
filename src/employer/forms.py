from django import forms
from .models import Employer, User
from django.core.exceptions import ValidationError


def uniqueEmailValidator(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('A user with this email already exists.')


def uniqueNameValidator(value):
    if Employer.objects.filter(name__iexact=value).exists():
        raise ValidationError('A company with this name already exists.')


class RegisterEmployer(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Company Name',
        validators=[uniqueNameValidator]
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        validators=[uniqueEmailValidator]
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    web_url = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Website'
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class LoginEmployer(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class EditEmployer(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Company Name',
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    web_url = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Website'
    )
