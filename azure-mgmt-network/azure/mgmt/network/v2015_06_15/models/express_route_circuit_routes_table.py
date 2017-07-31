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


class ExpressRouteCircuitRoutesTable(Model):
    """The routes table associated with the ExpressRouteCircuit.

    :param address_prefix: Gets AddressPrefix.
    :type address_prefix: str
    :param next_hop_type: Gets NextHopType. Possible values include:
     'VirtualNetworkGateway', 'VnetLocal', 'Internet', 'VirtualAppliance',
     'None'
    :type next_hop_type: str or :class:`RouteNextHopType
     <azure.mgmt.network.v2015_06_15.models.RouteNextHopType>`
    :param next_hop_ip: Gets NextHopIP.
    :type next_hop_ip: str
    :param as_path: Gets AsPath.
    :type as_path: str
    """

    _validation = {
        'next_hop_type': {'required': True},
    }

    _attribute_map = {
        'address_prefix': {'key': 'addressPrefix', 'type': 'str'},
        'next_hop_type': {'key': 'nextHopType', 'type': 'str'},
        'next_hop_ip': {'key': 'nextHopIP', 'type': 'str'},
        'as_path': {'key': 'asPath', 'type': 'str'},
    }

    def __init__(self, next_hop_type, address_prefix=None, next_hop_ip=None, as_path=None):
        self.address_prefix = address_prefix
        self.next_hop_type = next_hop_type
        self.next_hop_ip = next_hop_ip
        self.as_path = as_path
