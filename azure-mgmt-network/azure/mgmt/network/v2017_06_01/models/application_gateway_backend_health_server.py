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


class ApplicationGatewayBackendHealthServer(Model):
    """Application gateway backendhealth http settings.

    :param address: IP address or FQDN of backend server.
    :type address: str
    :param ip_configuration: Reference of IP configuration of backend server.
    :type ip_configuration:
     ~azure.mgmt.network.v2017_06_01.models.NetworkInterfaceIPConfiguration
    :param health: Health of backend server. Possible values include:
     'Unknown', 'Up', 'Down', 'Partial', 'Draining'
    :type health: str or
     ~azure.mgmt.network.v2017_06_01.models.ApplicationGatewayBackendHealthServerHealth
    """

    _attribute_map = {
        'address': {'key': 'address', 'type': 'str'},
        'ip_configuration': {'key': 'ipConfiguration', 'type': 'NetworkInterfaceIPConfiguration'},
        'health': {'key': 'health', 'type': 'str'},
    }

    def __init__(self, address=None, ip_configuration=None, health=None):
        self.address = address
        self.ip_configuration = ip_configuration
        self.health = health
