from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.hashers import make_password

from apps.accounts.models import Account
from apps.dashboard.forms.password_form import PasswordForm


@login_required(login_url="/auth/login/", redirect_field_name="next")
def password_view(request):
    template = 'dashboard/account/password.html'
    user = request.user
    account = user.account

    password_form = PasswordForm(
        initial={
            'user_id': user.id,
        },
    )
    if request.method == 'POST':
        password_form = PasswordForm(request.POST)
        if password_form.is_valid():
            new_password = password_form.cleaned_data['new_password']
            user.password = make_password(new_password)
            user.save()
            messages.add_message(request, messages.INFO, "The password is updated.")

    context = {
        'password_form': password_form,
        'page_settings': page_settings(),
    }
    return render(request, template, context)


def page_settings():
    return {
        'code': 'account_dashboard',
        'sub_code': 'password',
    }
