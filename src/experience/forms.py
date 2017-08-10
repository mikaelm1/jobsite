from django import forms
from .models import Experience


def year_choices():
    years = []
    for i in range(2017, 1900, -1):
        years.append((i, i))
    return years


class AddExperience(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    company_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Company Name'
    )
    job_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        label='Job Description',
        required=False
    )
    start_month = forms.ChoiceField(
        choices=Experience.MONTHS,
        widget=forms.Select(attrs={'class': 'form-control',
                                   'style': 'width: 20%;'}),
        label='Start Month'
    )
    start_year = forms.ChoiceField(
        choices=year_choices,
        widget=forms.Select(attrs={'class': 'form-control',
                                   'style': 'width: 20%;'}),
        label='Start Year'
    )
    end_month = forms.ChoiceField(
        choices=Experience.MONTHS,
        widget=forms.Select(attrs={'class': 'form-control',
                                   'style': 'width: 20%;'}),
        label='End Month'
    )
    end_year = forms.ChoiceField(
        choices=year_choices,
        widget=forms.Select(attrs={'class': 'form-control',
                                   'style': 'width: 20%;'}),
        label='End Year'
    )
    present = forms.BooleanField(
        label='Currently work here',
        widget=forms.CheckboxInput(),
        required=False,
    )

    class Meta:
        model = Experience
        fields = ('title', 'company_name', 'job_description', 'start_month',
                  'start_year', 'end_month', 'end_year', 'present')
