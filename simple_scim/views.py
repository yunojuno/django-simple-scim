from django.http import HttpRequest, JsonResponse
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_http_methods, require_POST


@require_GET
def get_user(request: HttpRequest, user_id: str) -> JsonResponse:
    """Return a user by ID."""
    pass


@csrf_exempt
@require_POST
def create_user(request: HttpRequest) -> JsonResponse:
    """Create a user."""
    pass


@csrf_exempt
@require_http_methods(["PUT", "PATCH"])
def update_user(request: HttpRequest, user_id: str) -> JsonResponse:
    """Update a user by ID."""
    pass


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_user(request: HttpRequest, user_id: str) -> JsonResponse:
    """Delete a user by ID."""
    pass


@require_GET
def list_users(request: HttpRequest) -> JsonResponse:
    """List users."""
    pass


@require_GET
def service_provider_config(request: HttpRequest) -> JsonResponse:
    """
    Provide service config as per RFC 7643.

    Attributes defined in RFC 7643:
    https://datatracker.ietf.org/doc/html/rfc7643#section-5

        The service provider configuration resource enables a service
        provider to discover SCIM specification features in a standardized
        form as well as provide additional implementation details to clients.
        All attributes have a mutability of "readOnly".  Unlike other core
        resources, the "id" attribute is not required for the service
        provider configuration resource.

    """
    data = {
        # "documentationUri": "http://example.com/help/scim.html",
        "schemas": ["urn:ietf:params:scim:schemas:core:2.0:ServiceProviderConfig"],
        "patch": {"supported": False},
        "bulk": {"supported": False},
        "filter": {"supported": False},
        "changePassword": {"supported": False},
        "sort": {"supported": False},
        "etag": {"supported": False},
        "authenticationSchemes": [
            {
                "name": "OAuth Bearer Token",
                "description": (
                    "Authentication scheme using the OAuth Bearer Token Standard"
                ),
                # "specUri": "http://www.rfc-editor.org/info/rfc6750",
                # "documentationUri": "http://example.com/help/oauth.html",
                "type": "oauthbearertoken",
                "primary": True,
            },
        ],
        "meta": {
            "location": reverse("scim:scim-config"),
            "resourceType": "ServiceProviderConfig",
            # "created": "2010-01-23T04:56:22Z",
            # "lastModified": "2011-05-13T04:42:34Z",
            # "version": 'W\/"3694e05e9dff594"',
        },
    }
    return JsonResponse(data=data, status=200)


@require_GET
def resource_types(request: HttpRequest) -> JsonResponse:
    """Provide resource types as per RFC 7643."""
    pass


@require_GET
def schemas(request: HttpRequest) -> JsonResponse:
    """Provide schemas as per RFC 7643."""
    pass


class SCIMUserView(View):
    """Handle core CRUD operations on a SCIM user."""

    def get(self, request: HttpRequest, user_id: str) -> JsonResponse:
        """Fetch a user by ID."""
        return get_user(request, user_id)

    def post(self, request: HttpRequest) -> JsonResponse:
        """Create a user."""
        return create_user(request)

    def put(self, request: HttpRequest, user_id: str) -> JsonResponse:
        return update_user(request, user_id)

    def patch(self, request: HttpRequest, user_id: str) -> JsonResponse:
        return update_user(request, user_id)

    def delete(self, request: HttpRequest, user_id: str) -> JsonResponse:
        return delete_user(request, user_id)
