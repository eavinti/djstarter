from datetime import date, timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from apps.resources.enums.input_class_dashboard_enum import Input

from apps.accounts.models import Account


class PasswordForm(forms.Form):
    user_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'sr-only', 'type': 'hidden'}))
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': Input.TEXT.value}))
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': Input.TEXT.value}),
        validators=[validate_password],
    )
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': Input.TEXT.value}))

    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id')

        current_password = cleaned_data.get('current_password')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        account = Account.objects.select_related('user').get(user__id=user_id)
        password_matched = account.user.check_password(current_password)

        if not password_matched:
            self.add_error('current_password', ValidationError("The password is not correct"))

        if new_password != confirm_password:
            self.add_error('confirm_password', ValidationError("New password and Confirm password must match"))


