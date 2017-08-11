from django import forms
from .models import Employer


class RegisterEmployer(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
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

    class Meta:
        model = Employer
        fields = ('name', 'city', 'state', 'web_url')