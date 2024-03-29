from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Sport, Country, State
from django.core.exceptions import ValidationError


# Form to add a new user.
class NewUserForm(UserCreationForm):
    password1 = forms.CharField(
        label='Choose a Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_superuser',
            'is_staff',
            'is_active',
            'organisation',
            'site_name',
            'site_type',
            'primary_color',
            'secondary_color',
            'primary_text',
            'secondary_text',
            'profile_picture',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            password_error = "Your passwords do not match. Please try again."
            raise ValidationError(password_error)

        return password2

    def save(self, commit=True):
        instance = super(NewUserForm, self).save()

        return instance


# Form to edit a user's details.
class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_superuser',
            'is_staff',
            'is_active',
            'organisation',
            'site_name',
            'site_type',
            'primary_color',
            'secondary_color',
            'primary_text',
            'secondary_text',
            'profile_picture',
        ]


# Form to edit a sport's details.
class SportForm(forms.ModelForm):

    class Meta:
        model = Sport
        fields = [
            'name',
            'icon',
        ]


# Form to edit a country's details.
class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = [
            'name',
            'short_name',
            'continent',
            'abbreviation',
            'flag',
            'is_active',
            'is_independent',
            'is_recognised',
        ]
        labels = {
            'is_active': 'Active',
            'is_independent': 'Independent',
            'is_recognised': 'Recognised',
        }


# Form to edit a country's details.
class StateForm(forms.ModelForm):

    class Meta:
        model = State
        fields = [
            'name',
            'country',
            'abbreviation',
            'flag',
        ]
