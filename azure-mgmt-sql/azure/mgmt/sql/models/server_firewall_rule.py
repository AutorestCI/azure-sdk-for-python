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

from .sql_sub_resource import SqlSubResource


class ServerFirewallRule(SqlSubResource):
    """Represents an Azure SQL server firewall rule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Resource name
    :vartype name: str
    :ivar id: The resource ID.
    :vartype id: str
    :ivar kind: Kind of server that contains this firewall rule.
    :vartype kind: str
    :ivar location: Location of the server that contains this firewall rule.
    :vartype location: str
    :param start_ip_address: The start IP address of the Azure SQL server
     firewall rule. Must be IPv4 format.
    :type start_ip_address: str
    :param end_ip_address: The end IP address of the Azure SQL server firewall
     rule. Must be IPv4 format.
    :type end_ip_address: str
    """ 

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'kind': {'readonly': True},
        'location': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'start_ip_address': {'key': 'properties.startIpAddress', 'type': 'str'},
        'end_ip_address': {'key': 'properties.endIpAddress', 'type': 'str'},
    }

    def __init__(self, start_ip_address=None, end_ip_address=None):
        super(ServerFirewallRule, self).__init__()
        self.kind = None
        self.location = None
        self.start_ip_address = start_ip_address
        self.end_ip_address = end_ip_address
