from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _lazy


class SCIMUser(models.Model):
    """SCIM version of the user model."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    external_id = models.CharField(
        max_length=100,
        help_text=_lazy("ID supplied by the identity provider as 'externalId'."),
    )


class SCIMEvent(models.Model):
    """Event log for SCIM events."""
