from django import forms
from .models import Job


class NewJob(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    job_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        label='Job Description',
        required=False
    )
    job_type = forms.ChoiceField(
        choices=Job.JOB_TYPES,
        widget=forms.Select(attrs={'class': 'form-control',
                                   'style': 'width: 20%;'}),
        label='Job Types'
    )
    min_salary = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=False
    )
    max_salary = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=False
    )