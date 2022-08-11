from django.urls import path
from .views import LoginView, LogoutUserView, MainView

urlpatterns = [
    path('', MainView.as_view(), name="main"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutUserView.as_view(), name="logout"),
]
