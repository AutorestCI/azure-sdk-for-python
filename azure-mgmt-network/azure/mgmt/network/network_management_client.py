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
from . import models


class NetworkManagementClientConfiguration(AzureConfiguration):
    """Configuration for NetworkManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription credentials which uniquely
     identify the Microsoft Azure subscription. The subscription ID forms part
     of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, api_version='2016-09-01', base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not isinstance(subscription_id, str):
            raise TypeError("Parameter 'subscription_id' must be str.")
        if api_version is not None and not isinstance(api_version, str):
            raise TypeError("Optional parameter 'api_version' must be str.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(NetworkManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('networkmanagementclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id
        self.api_version = api_version


class NetworkManagementClient(object):
    """The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.

    :ivar config: Configuration for client.
    :vartype config: NetworkManagementClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription credentials which uniquely
     identify the Microsoft Azure subscription. The subscription ID forms part
     of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, api_version='2016-09-01', base_url=None):

        self.config = NetworkManagementClientConfiguration(credentials, subscription_id, api_version, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

