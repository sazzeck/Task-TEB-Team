from django.views.generic import TemplateView
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import resolve_url
from django.contrib.auth.views import redirect_to_login
from urllib.parse import urlparse

from data import AirtableUsers

users = AirtableUsers()


class CustomLoginRequired(AccessMixin):
    def handle_no_permission(self):
        path = self.request.build_absolute_uri()
        resolved_login_url = resolve_url(self.get_login_url())
        login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
        current_scheme, current_netloc = urlparse(path)[:2]
        if (not login_scheme or login_scheme == current_scheme) and (
            not login_netloc or login_netloc == current_netloc
        ):
            path = self.request.get_full_path()
        return redirect_to_login(
            path,
            resolved_login_url,
            self.get_redirect_field_name(),
        )

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get("is_login"):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class MainView(CustomLoginRequired, TemplateView):
    template_name = "main/main.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        user = self.request.session.get("username")
        context = super().get_context_data(**kwargs)
        context["title"] = "Telegram User Info"
        context["user_id"] = users.get_user_id(user)
        context["username"] = users.get_username(user)
        context["firstname"] = users.get_firstname(user)
        return context
