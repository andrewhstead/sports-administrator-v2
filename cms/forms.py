from django import forms
from data.models import Competition


# Simple username and password login.
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# Form to create a new competition.
class NewCompetitionForm(forms.ModelForm):

    class Meta:
        model = Competition
        fields = ['name', 'sport', 'country']
        labels = {
            'name': 'Competition Name',
            'sport': 'Sport',
            'country': 'Primary Country',
        }
