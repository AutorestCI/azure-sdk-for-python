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


class NodeParameters(Model):
    """Parameter collection for operations on arm node resource.

    :param location: Location of the resource.
    :type location: str
    :param tags: Resource tags.
    :type tags: object
    :param gateway_id: Gateway ID which will manage this node.
    :type gateway_id: str
    :param connection_name: myhost.domain.com
    :type connection_name: str
    :param user_name: User name to be used to connect to node.
    :type user_name: str
    :param password: Password associated with user name.
    :type password: str
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'object'},
        'gateway_id': {'key': 'properties.gatewayId', 'type': 'str'},
        'connection_name': {'key': 'properties.connectionName', 'type': 'str'},
        'user_name': {'key': 'properties.userName', 'type': 'str'},
        'password': {'key': 'properties.password', 'type': 'str'},
    }

    def __init__(self, location=None, tags=None, gateway_id=None, connection_name=None, user_name=None, password=None):
        self.location = location
        self.tags = tags
        self.gateway_id = gateway_id
        self.connection_name = connection_name
        self.user_name = user_name
        self.password = password
