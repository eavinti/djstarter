from django.urls import path

from .views.home_view import home_dashboard_view
from .views.settings_view import settings_dashboard_view


urlpatterns = [
    path("", home_dashboard_view, name="home_dashboard"),
    path("settings/", settings_dashboard_view, name="settings_dashboard"),
]
