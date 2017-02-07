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
from .operations.servers_operations import ServersOperations
from .operations.databases_operations import DatabasesOperations
from .operations.elastic_pools_operations import ElasticPoolsOperations
from .operations.recommended_elastic_pools_operations import RecommendedElasticPoolsOperations
from . import models


class SqlManagementClientConfiguration(AzureConfiguration):
    """Configuration for SqlManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription ID that identifies an Azure
     subscription.
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

        super(SqlManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('sqlmanagementclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class SqlManagementClient(object):
    """The Azure SQL Database management API provides a RESTful set of web services that interact with Azure SQL Database services to manage your databases. The API enables you to create, retrieve, update, and delete databases.

    :ivar config: Configuration for client.
    :vartype config: SqlManagementClientConfiguration

    :ivar servers: Servers operations
    :vartype servers: .operations.ServersOperations
    :ivar databases: Databases operations
    :vartype databases: .operations.DatabasesOperations
    :ivar elastic_pools: ElasticPools operations
    :vartype elastic_pools: .operations.ElasticPoolsOperations
    :ivar recommended_elastic_pools: RecommendedElasticPools operations
    :vartype recommended_elastic_pools: .operations.RecommendedElasticPoolsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription ID that identifies an Azure
     subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = SqlManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.servers = ServersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.databases = DatabasesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.elastic_pools = ElasticPoolsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.recommended_elastic_pools = RecommendedElasticPoolsOperations(
            self._client, self.config, self._serialize, self._deserialize)
