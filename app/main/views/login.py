from django.shortcuts import render, redirect
from django.views.generic.edit import View
from django.contrib.auth.views import RedirectURLMixin
from django.urls import reverse

from main.forms import LoginForm

from data import AirtableUsers

users = AirtableUsers()


class UserLoginView(RedirectURLMixin, View):
    template = "main/login.html"
    form = LoginForm

    def get(self, request):
        return render(request, self.template, {"form": self.form, "title": "Login"})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            if users.user_is_created(username):
                if users.auth(username, password):
                    request.session["is_login"] = True
                    request.session["username"] = users.get_username(username)
                    return redirect(reverse("main"))
            return render(request, "main/login.html", {"form": form})
        return render(request, "main/login.html", {"form": form})
