# urls.py
from django.urls import path

from .views import ServiceProviderConfig, UserDetail, UserList

app_name = "simple_scim"
urlpatterns = [
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<str:user_id>/", UserDetail.as_view(), name="user-detail"),
    path("config/", ServiceProviderConfig.as_view(), name="service-provider-config"),
]
