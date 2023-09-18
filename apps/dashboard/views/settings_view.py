from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="/accounts/login/", redirect_field_name="next")
def settings_dashboard_view(request):
    template = 'dashboard/settings.html'

    context = {
        'page_settings': page_settings()
    }
    return render(request, template, context)


def page_settings():
    return {
        'code': 'settings_dashboard',
        'sub_code': '',
    }
