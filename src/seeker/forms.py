from django import forms
from .models import Seeker, User
from django.contrib.auth.views import LoginView


class SeekerLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )

    # class Meta:
    #     model = User
    #     fields = ('username', 'password')