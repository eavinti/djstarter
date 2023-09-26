from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.core.validators import EmailValidator

from apps.resources.enums.input_class_dashboard_enum import Input

from apps.accounts.models import Account


class AccountForm(forms.Form):

    user_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'sr-only', 'type': 'hidden'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': Input.TEXT.value}),
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': Input.TEXT.value}),
        required=True,
        min_length=3,
    )

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': Input.DATE.value, 'type': 'date'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': Input.TEXT.value}),
        validators=[EmailValidator]
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': Input.TEXT_LEFT.value}),
        required=True,
        min_length=3,
    )
    # avatar_image = forms.FileField(
    #     widget=forms.FileInput(attrs={'class': 'sr-only'}),
    #     required=False,
    # )

    # timezone = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': Input.TEXT.value, 'disabled': 'disabled'}),
    #     required=False,
    # )

    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id')
        email = cleaned_data.get('email')
        username = cleaned_data.get('username').lower().strip()

        exists_email = Account.objects.filter(user__email=email).exclude(user__id=user_id).exists()
        exists_username = Account.objects.filter(user__username=username).exclude(user__id=user_id).exists()

        if exists_email:
            self.add_error('email', ValidationError("Email already exists"))

        if exists_username:
            self.add_error('username', ValidationError("username already exists"))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) <= 2:
            raise ValidationError("The username is incorrect")
        return username

    def clean_avatar_image(self):
        avatar_image = self.cleaned_data.get('avatar_image')
        if avatar_image:
            if avatar_image.size > 3 * 1024 * 1024:  # 3MB en bytes
                raise ValidationError("The image cannot be larger than 3MB.")

        allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        allowed_magic_numbers = ['image/jpeg', 'image/png', 'image/gif']

        # file_extension = avatar_image.name.lower().split('.')[-1]
        # if file_extension not in allowed_extensions:
        #     raise ValidationError("The file must be (.jpg, .jpeg, .png, .gif).")
        #
        # mime_type = avatar_image.content_type
        # if mime_type not in allowed_magic_numbers:
        #     raise ValidationError("El archivo no es una imagen válida.")
        return avatar_image
