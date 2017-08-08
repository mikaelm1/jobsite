from django import forms
from django.core.exceptions import ValidationError
from .models import SeekerEducation, Education


def year_validator(value):
    if len(str(value)) != 4 or value < 0:
        raise ValidationError('Year must be a four digit number.')


class NewEducationForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    degree = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    major = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    year_started = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        validators=[year_validator]
    )
    year_ended = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        validators=[year_validator],
        help_text='Type expected year if not graduated yet.'
    )
    graduated = forms.Select()

    class Meta:
        model = SeekerEducation
        fields = ('name', 'city', 'state', 'degree', 'major', 'year_started', 'year_ended', 'graduated')
