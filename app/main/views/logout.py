from django.contrib.auth.views import LogoutView


class LogoutUserView(LogoutView):
    next_page = "login"

    def get_default_redirect_url(self):
        self.request.session["is_login"] = False
        return super().get_default_redirect_url()
