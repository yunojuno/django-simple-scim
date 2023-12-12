# # serializers.py
# from django.contrib.auth.models import User
# from django.urls import reverse
# from rest_framework import serializers

# schema = {
#     "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
#     "id": "2819c223-7f76-453a-413861904646",
#     "externalId": "701984",
#     "userName": "bjensen@example.com",
#     "name": {
#         "formatted": "Ms. Barbara J Jensen, III",
#         "familyName": "Jensen",
#         "givenName": "Barbara",
#         "middleName": "Jane",
#         "honorificPrefix": "Ms.",
#         "honorificSuffix": "III",
#     },
#     "meta": {
#         "resourceType": "User",
#         "created": "2010-01-23T04:56:22Z",
#         "lastModified": "2011-05-13T04:42:34Z",
#         "version": 'W\/"3694e05e9dff591"',
#         "location": "https://example.com/v2/Users/2819c223-7f76-453a-413861904646",
#     },
# }


# class SCIMUserSerializer(serializers.ModelSerializer):
#     userName = serializers.CharField(source="username")
#     name = serializers.SerializerMethodField()
#     meta = serializers.SerializerMethodField()

#     def get_name(self, obj: User) -> dict:
#         return {
#             "formatted": obj.get_full_name(),
#             "givenName": obj.first_name,
#             "familyName": obj.last_name,
#         }

#     def get_meta(self, obj: User) -> dict:
#         return {
#             "resourceType": "User",
#             "created": obj.date_joined.isoformat(),
#             "location": reverse("simple_scim:user-detail", kwargs={"pk": obj.id}),
#         }

#     class Meta:
#         model = User
#         fields = ("name", "userName", "meta")
