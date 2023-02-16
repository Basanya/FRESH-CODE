from django.urls import path
from .views import api_home,api_detail,api_create, api_update, api_delete

urlpatterns = [
path("home_view/", api_home, name="home_ap"),
path("post_view/<slug:slug>/",api_detail, name="home_detail"),
path("create_view/", api_create, name="create"),
path("update_view/<slug:slug>/", api_update, name="update"),
path("delete_view/<slug:slug>/", api_delete, name="delete")
]