# urls.py
from django.urls import path

from .views import SCIMUserView, resource_types, schemas, service_provider_config

app_name = "scim"
urlpatterns = [
    # handles the create request (POST, no user_id)
    path("Users/", SCIMUserView.as_view(), name="scim-user"),
    # handles the update, delete and fetch requests (PUT, PATCH, DELETE, GET)
    path("Users/<str:user_id>/", SCIMUserView.as_view(), name="scim-user"),
    path("ServiceProviderConfig", service_provider_config, name="scim-config"),
    path("ResourceTypes", resource_types, name="scim-resource-types"),
    path("Schemas", schemas, name="scim-schemas"),
]
