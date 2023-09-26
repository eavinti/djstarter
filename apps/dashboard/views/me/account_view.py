from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages

from apps.accounts.models import Account
from apps.dashboard.forms.account_form import AccountForm


@login_required(login_url="/auth/login/", redirect_field_name="next")
def account_view(request):
    template = 'dashboard/account/account.html'
    user = request.user
    account = user.account

    date_of_birth = account.date_of_birth.strftime('%Y-%m-%d') if account.date_of_birth else None
    account_form = AccountForm(
        initial={
            'user_id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'username': user.username,
            'date_of_birth': date_of_birth,
        },
    )
    if request.method == 'POST':
        account_form = AccountForm(request.POST)
        if account_form.is_valid():
            first_name = account_form.cleaned_data['first_name']
            last_name = account_form.cleaned_data['last_name']
            email = account_form.cleaned_data['email']
            username = account_form.cleaned_data['username']
            date_of_birth = account_form.cleaned_data['date_of_birth']

            account.date_of_birth = date_of_birth
            account.save()

            user = account.user
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.add_message(request, messages.INFO, "The profile is updated.")

    context = {
        'account_form': account_form,
        'account': account,
        'page_settings': page_settings(),
    }
    return render(request, template, context)


def page_settings():
    return {
        'code': 'account_dashboard',
        'sub_code': 'account',
    }
