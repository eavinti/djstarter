from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="/accounts/login/", redirect_field_name="next")
def home_dashboard_view(request):
    template = 'dashboard/index.html'

    context = {
        'page_settings': page_settings()
    }
    return render(request, template, context)


def page_settings():
    return {
        'code': 'index_dashboard',
        'sub_code': '',
    }
