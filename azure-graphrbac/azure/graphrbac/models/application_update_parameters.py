# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApplicationUpdateParameters(Model):
    """Request parameters for updating an existing application.

    :param available_to_other_tenants: Whether the application is available to
     other tenants
    :type available_to_other_tenants: bool
    :param display_name: The display name of the application.
    :type display_name: str
    :param homepage: The home page of the application.
    :type homepage: str
    :param identifier_uris: A collection of URIs for the application.
    :type identifier_uris: list of str
    :param reply_urls: A collection of reply URLs for the application.
    :type reply_urls: list of str
    :param key_credentials: The list of KeyCredential objects.
    :type key_credentials: list of :class:`KeyCredential
     <azure.graphrbac.models.KeyCredential>`
    :param password_credentials: The list of PasswordCredential objects.
    :type password_credentials: list of :class:`PasswordCredential
     <azure.graphrbac.models.PasswordCredential>`
    :param oauth2_allow_implicit_flow: Whether to allow implicit grant flow
     for OAuth2
    :type oauth2_allow_implicit_flow: bool
    :param required_resource_access: Specifies resources that this application
     requires access to and the set of OAuth permission scopes and application
     roles that it needs under each of those resources. This pre-configuration
     of required resource access drives the consent experience.
    :type required_resource_access: list of :class:`RequiredResourceAccess
     <azure.graphrbac.models.RequiredResourceAccess>`
    """

    _attribute_map = {
        'available_to_other_tenants': {'key': 'availableToOtherTenants', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'homepage': {'key': 'homepage', 'type': 'str'},
        'identifier_uris': {'key': 'identifierUris', 'type': '[str]'},
        'reply_urls': {'key': 'replyUrls', 'type': '[str]'},
        'key_credentials': {'key': 'keyCredentials', 'type': '[KeyCredential]'},
        'password_credentials': {'key': 'passwordCredentials', 'type': '[PasswordCredential]'},
        'oauth2_allow_implicit_flow': {'key': 'oauth2AllowImplicitFlow', 'type': 'bool'},
        'required_resource_access': {'key': 'requiredResourceAccess', 'type': '[RequiredResourceAccess]'},
    }

    def __init__(self, available_to_other_tenants=None, display_name=None, homepage=None, identifier_uris=None, reply_urls=None, key_credentials=None, password_credentials=None, oauth2_allow_implicit_flow=None, required_resource_access=None):
        self.available_to_other_tenants = available_to_other_tenants
        self.display_name = display_name
        self.homepage = homepage
        self.identifier_uris = identifier_uris
        self.reply_urls = reply_urls
        self.key_credentials = key_credentials
        self.password_credentials = password_credentials
        self.oauth2_allow_implicit_flow = oauth2_allow_implicit_flow
        self.required_resource_access = required_resource_access
