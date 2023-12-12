"""
Use these signals to hook into the user creation, update and deletion process.

These are provided as an alternative to subclassing the views and overriding
the methods. The signals are fired before and after the user is created,
updated or deleted.

If you want to abort the user creation, update or deletion process, raise an
exception in the pre-signal handler.

"""
import django.dispatch

# kwargs: user: User, user_data: dict
pre_create_scim_user = django.dispatch.Signal()
# kwargs: user: User, user_data: dict
post_create_scim_user = django.dispatch.Signal()

# kwargs: user: User, user_data: dict
pre_update_scim_user = django.dispatch.Signal()
# kwargs: user: User, user_data: dict
post_update_scim_user = django.dispatch.Signal()

# kwargs: user: User
pre_delete_scim_user = django.dispatch.Signal()
# kwargs: user: User
post_delete_scim_user = django.dispatch.Signal()
