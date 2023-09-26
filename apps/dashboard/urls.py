from django.urls import path, include

from .views.home_view import home_dashboard_view
from .views.settings_view import settings_dashboard_view

from .views.me.account_view import account_view
from .views.me.password_view import password_view


urlpatterns = [
    path("", home_dashboard_view, name="home_dashboard"),
    path("settings/", settings_dashboard_view, name="settings_dashboard"),

    path('me/', include([
        path('account/', account_view, name='account_view'),
        path('password/', password_view, name='password_view'),
    ])),
]
