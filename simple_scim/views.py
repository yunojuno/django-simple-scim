# views.py
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SCIMUserSerializer


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = SCIMUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SCIMUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get(self, request: Request, user_id: str) -> Response:
        user = self.get_object(user_id)
        serializer = SCIMUserSerializer(user)
        data = serializer.data
        data["id"] = user.id
        data["schemas"] = ["urn:ietf:params:scim:schemas:core:2.0:User"]
        return Response(
            data,
            status=status.HTTP_200_OK,
            content_type="application/scim+json",
        )

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = SCIMUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, user_id: str) -> User:
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Http404


class ServiceProviderConfig(APIView):
    """Provide service config as per RFC 7643."""

    def get(self, request: Request) -> Response:
        data = {
            "schemas": ["urn:ietf:params:scim:schemas:core:2.0:ServiceProviderConfig"],
            "documentationUri": "http://example.com/help/scim.html",
            "patch": {"supported": False},
            "bulk": {"supported": False},
            "filter": {"supported": False},
            "changePassword": {"supported": False},
            "sort": {"supported": False},
            "etag": {"supported": False},
            "authenticationSchemes": [
                {
                    "name": "OAuth Bearer Token",
                    "description": "Authentication scheme using the OAuth Bearer Token Standard",
                    "specUri": "http://www.rfc-editor.org/info/rfc6750",
                    "documentationUri": "http://example.com/help/oauth.html",
                    "type": "oauthbearertoken",
                    "primary": True,
                },
                {
                    "name": "HTTP Basic",
                    "description": "Authentication scheme using the HTTP Basic Standard",
                    "specUri": "http://www.rfc-editor.org/info/rfc2617",
                    "documentationUri": "http://example.com/help/httpBasic.html",
                    "type": "httpbasic",
                },
            ],
            "meta": {
                "location": "https://example.com/v2/ServiceProviderConfig",
                "resourceType": "ServiceProviderConfig",
                "created": "2010-01-23T04:56:22Z",
                "lastModified": "2011-05-13T04:42:34Z",
                "version": 'W\/"3694e05e9dff594"',
            },
        }
        return Response(data=data, status=status.HTTP_200_OK)
