
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin


class MainView(LoginRequiredMixin, TemplateView):
    template_name = "main/main.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        return context
