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

from .resource import Resource


class VnetRoute(Resource):
    """Virtual Network route contract used to pass routing information for a
    Virtual Network.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :param location: Resource Location.
    :type location: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict
    :param vnet_route_name: The name of this route. This is only returned by
     the server and does not need to be set by the client.
    :type vnet_route_name: str
    :param start_address: The starting address for this route. This may also
     include a CIDR notation, in which case the end address must not be
     specified.
    :type start_address: str
    :param end_address: The ending address for this route. If the start
     address is specified in CIDR notation, this must be omitted.
    :type end_address: str
    :param route_type: The type of route this is:
     DEFAULT - By default, every app has routes to the local address ranges
     specified by RFC1918
     INHERITED - Routes inherited from the real Virtual Network routes
     STATIC - Static route set on the app only
     These values will be used for syncing an app's routes with those from a
     Virtual Network. Possible values include: 'DEFAULT', 'INHERITED', 'STATIC'
    :type route_type: str or :class:`RouteType
     <azure.mgmt.web.models.RouteType>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'location': {'required': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'vnet_route_name': {'key': 'properties.name', 'type': 'str'},
        'start_address': {'key': 'properties.startAddress', 'type': 'str'},
        'end_address': {'key': 'properties.endAddress', 'type': 'str'},
        'route_type': {'key': 'properties.routeType', 'type': 'str'},
    }

    def __init__(self, location, kind=None, tags=None, vnet_route_name=None, start_address=None, end_address=None, route_type=None):
        super(VnetRoute, self).__init__(kind=kind, location=location, tags=tags)
        self.vnet_route_name = vnet_route_name
        self.start_address = start_address
        self.end_address = end_address
        self.route_type = route_type
