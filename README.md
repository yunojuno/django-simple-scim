# Django Simple SCIM

Django app to implement SCIM 2.0 

This package supports basic SCIM integration to enable your project to
act as a SCIM Service Provider. This currently includes:

- User entity CRUD operations

## Version support

This packages supports Django 3.2+, Python 3.8+

## What is SCIM

SCIM stands for System for Cross-domain Identity Management.

> The System for Cross-domain Identity Management (SCIM) specifications are
> designed to make identity management in cloud-based applications and services
> easier. [...] Its intent is to reduce the cost and complexity of user
> management operations by providing a common user schema and extension model as
> well as binding documents to provide patterns for exchanging this schema using
> HTTP.

> This document provides a platform-neutral schema and extension model for
> representing users and groups and other resource types in JSON format.  This
> schema is intended for exchange and use with cloud service providers.

_Citation: 
https://datatracker.ietf.org/doc/html/rfc7643_

From the perspective of a Django application developer, it is implemented as
a set of REST (JSON) endpoints for managing `User` and `Group` objects remotely.

## Why do you need SCIM?

SCIM is used by large enterprises to manage their users' access to external
applications. SCIM integration allows them to provision new user accounts
and deactivate user accounts on remote systems from their existing identity
management solutions (e.g. Google Workspace, MSFT Azure AD, Okta, ...).

If you have enterprise clients signing up to your application, you have 
probably been asked at some point if you support SSO (SAML) and SCIM. This
package can help you to answer "yes" to that question.

## Supported SCIM use cases

1. Create a new User entity
2. Update an existing User entity
3. Deactivate an existing User entity
4. Delete an existing User entity
5. Lookup an existing User entity

This package does not currently support Groups.

## What's in the box?

As well as the API endpoints to support the use cases above, this package
provides endpoints for the following:

* Resource Schema Representation (for User only)
* Service Provider Configuration Schema

It adds a model, `SCIMEvent` that tracks each endpoint event, useful for
auditing / testing / debugging.

It also provides Django signals for the CRUD operations (pre/post) so that
you can hook additional business logic into your application at each event.
The `SCIMEvent` logging uses these signals as a demonstration.

## Related docs

You should read the standards before embarking on a SCIM API project:

1. Definitions, Overview, Concepts, and Requirements: https://datatracker.ietf.org/doc/html/rfc7642
2. Core schema: https://datatracker.ietf.org/doc/html/rfc7643
3. Protocol: https://datatracker.ietf.org/doc/html/rfc7644
