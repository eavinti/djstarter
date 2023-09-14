from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['email']
        user.save()
        return user

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')

        exists_email = User.objects.filter(email=email).exists()

        if exists_email:
            self.add_error('email', ValidationError("Email already exists."))
