from django.urls import path
from .views import register, my_login

urlpatterns = [
    path("my_reg/", register, name="signup" ),
    path("my_login/", my_login, name="login")
]