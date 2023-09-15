from django.views.generic import TemplateView


class ContactPageView(TemplateView):
    template_name = "pages/contact.html"

