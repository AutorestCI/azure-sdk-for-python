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


class ContainerServiceAgentPoolProfile(Model):
    """Profile for the container service agent pool.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: Unique name of the agent pool profile in the context of the
     subscription and resource group.
    :type name: str
    :param count: Number of agents (VMs) to host docker containers. Allowed
     values must be in the range of 1 to 100 (inclusive). The default value is
     1. . Default value: 1 .
    :type count: int
    :param vm_size: Size of agent VMs. Possible values include: 'Standard_A0',
     'Standard_A1', 'Standard_A2', 'Standard_A3', 'Standard_A4', 'Standard_A5',
     'Standard_A6', 'Standard_A7', 'Standard_A8', 'Standard_A9',
     'Standard_A10', 'Standard_A11', 'Standard_D1', 'Standard_D2',
     'Standard_D3', 'Standard_D4', 'Standard_D11', 'Standard_D12',
     'Standard_D13', 'Standard_D14', 'Standard_D1_v2', 'Standard_D2_v2',
     'Standard_D3_v2', 'Standard_D4_v2', 'Standard_D5_v2', 'Standard_D11_v2',
     'Standard_D12_v2', 'Standard_D13_v2', 'Standard_D14_v2', 'Standard_G1',
     'Standard_G2', 'Standard_G3', 'Standard_G4', 'Standard_G5',
     'Standard_DS1', 'Standard_DS2', 'Standard_DS3', 'Standard_DS4',
     'Standard_DS11', 'Standard_DS12', 'Standard_DS13', 'Standard_DS14',
     'Standard_GS1', 'Standard_GS2', 'Standard_GS3', 'Standard_GS4',
     'Standard_GS5'
    :type vm_size: str or :class:`ContainerServiceVMSizeTypes
     <azure.mgmt.compute.models.ContainerServiceVMSizeTypes>`
    :param dns_prefix: DNS prefix to be used to create the FQDN for the agent
     pool.
    :type dns_prefix: str
    :ivar fqdn: FDQN for the agent pool.
    :vartype fqdn: str
    """

    _validation = {
        'name': {'required': True},
        'count': {'required': True, 'maximum': 100, 'minimum': 1},
        'vm_size': {'required': True},
        'dns_prefix': {'required': True},
        'fqdn': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'dns_prefix': {'key': 'dnsPrefix', 'type': 'str'},
        'fqdn': {'key': 'fqdn', 'type': 'str'},
    }

    def __init__(self, name, vm_size, dns_prefix, count=1):
        self.name = name
        self.count = count
        self.vm_size = vm_size
        self.dns_prefix = dns_prefix
        self.fqdn = None
