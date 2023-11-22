from django.contrib import admin
from django.urls import include, path
from django.views import debug

admin.autodiscover()

urlpatterns = [
    path("", debug.default_urlconf),
    path("admin/", admin.site.urls),
    path("scim/v2/", include("simple_scim.urls")),
]
