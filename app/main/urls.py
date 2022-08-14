from django.urls import path

from .views.login import UserLoginView
from .views import LogoutUserView, MainView


urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("login", UserLoginView.as_view(), name="login"),
    path("logout", LogoutUserView.as_view(), name="logout"),
]
