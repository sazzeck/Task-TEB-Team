from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from data import AirtableUsers


class MainView(LoginRequiredMixin, TemplateView):
    template_name = "main/main.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        context["user_id"] = AirtableUsers().get_user_id(user.id)
        context["username"] = AirtableUsers().get_username(user.id)
        context["firstname"] = AirtableUsers().get_firstname(user.id)
        return context
