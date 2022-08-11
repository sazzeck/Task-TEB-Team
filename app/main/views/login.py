from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

from main.forms import LoginForm


class LoginView(LoginView):
    form_class = LoginForm
    template_name = "main/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Login"
        return context

    def get_success_url(self):
        return reverse_lazy("main")
