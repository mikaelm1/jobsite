from django import forms
from .models import Seeker, User


class SeekerLoginForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,
        max_length=100,
        label='Enter your email',
        help_text='Enter your email'
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password')