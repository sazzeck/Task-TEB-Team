from django.contrib.auth.views import LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin


class LogoutUserView(LoginRequiredMixin, LogoutView):
    next_page = "login"
