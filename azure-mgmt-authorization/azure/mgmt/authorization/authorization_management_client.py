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

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.classic_administrators_operations import ClassicAdministratorsOperations
from .operations.permissions_operations import PermissionsOperations
from .operations.provider_operations_metadata_operations import ProviderOperationsMetadataOperations
from .operations.role_assignments_operations import RoleAssignmentsOperations
from .operations.role_definitions_operations import RoleDefinitionsOperations
from . import models


class AuthorizationManagementClientConfiguration(AzureConfiguration):
    """Configuration for AuthorizationManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not isinstance(subscription_id, str):
            raise TypeError("Parameter 'subscription_id' must be str.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(AuthorizationManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('authorizationmanagementclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class AuthorizationManagementClient(object):
    """Role based access control provides you a way to apply granular level policy administration down to individual resources or resource groups. These operations enable you to manage role definitions and role assignments. A role definition describes the set of actions that can be performed on resources. A role assignment grants access to Azure Active Directory users.

    :ivar config: Configuration for client.
    :vartype config: AuthorizationManagementClientConfiguration

    :ivar classic_administrators: ClassicAdministrators operations
    :vartype classic_administrators: azure.mgmt.authorization.operations.ClassicAdministratorsOperations
    :ivar permissions: Permissions operations
    :vartype permissions: azure.mgmt.authorization.operations.PermissionsOperations
    :ivar provider_operations_metadata: ProviderOperationsMetadata operations
    :vartype provider_operations_metadata: azure.mgmt.authorization.operations.ProviderOperationsMetadataOperations
    :ivar role_assignments: RoleAssignments operations
    :vartype role_assignments: azure.mgmt.authorization.operations.RoleAssignmentsOperations
    :ivar role_definitions: RoleDefinitions operations
    :vartype role_definitions: azure.mgmt.authorization.operations.RoleDefinitionsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = AuthorizationManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2015-07-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.classic_administrators = ClassicAdministratorsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.permissions = PermissionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.provider_operations_metadata = ProviderOperationsMetadataOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.role_assignments = RoleAssignmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.role_definitions = RoleDefinitionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
