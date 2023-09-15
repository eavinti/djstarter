from django.urls import path

from .views.home_view import HomePageView
from .views.about_view import AboutPageView
from .views.contact_view import ContactPageView
from .views.features_view import FeaturesPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("features/", FeaturesPageView.as_view(), name="features"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
]
