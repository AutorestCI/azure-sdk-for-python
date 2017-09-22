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


class ExpressRouteConnector(Resource):
    """Express Route Connector Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict
    :param circuits: List of Express Route Circuits.
    :type circuits: list of :class:`SubResource
     <azure.mgmt.network.v2017_06_01.models.SubResource>`
    :param authorization_keys: List of Circuit Authorization Keys.
    :type authorization_keys: list of str
    :param address_prefix: The reference of the addressPrefix resource.
    :type address_prefix: str
    :ivar provisioning_state: The provisioning state of the Express Route
     Connector Resource. Possible Values 'Updating', 'Deleting', and 'Failed'.
    :vartype provisioning_state: str
    :ivar etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :vartype etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'circuits': {'required': True},
        'address_prefix': {'required': True},
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'circuits': {'key': 'properties.circuits', 'type': '[SubResource]'},
        'authorization_keys': {'key': 'properties.authorizationKeys', 'type': '[str]'},
        'address_prefix': {'key': 'properties.addressPrefix', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, circuits, address_prefix, id=None, location=None, tags=None, authorization_keys=None):
        super(ExpressRouteConnector, self).__init__(id=id, location=location, tags=tags)
        self.circuits = circuits
        self.authorization_keys = authorization_keys
        self.address_prefix = address_prefix
        self.provisioning_state = None
        self.etag = None
