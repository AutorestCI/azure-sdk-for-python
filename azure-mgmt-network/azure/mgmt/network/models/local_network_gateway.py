# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class LocalNetworkGateway(Resource):
    """A common class for general resource information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource Id
    :type id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param local_network_address_space: Local network site Address space
    :type local_network_address_space: :class:`AddressSpace
     <azure.mgmt.network.models.AddressSpace>`
    :param gateway_ip_address: IP address of local network gateway.
    :type gateway_ip_address: str
    :param bgp_settings: Local network gateway's BGP speaker settings
    :type bgp_settings: :class:`BgpSettings
     <azure.mgmt.network.models.BgpSettings>`
    :param resource_guid: Gets or sets resource guid property of the
     LocalNetworkGateway resource
    :type resource_guid: str
    :param provisioning_state: Gets or sets Provisioning state of the
     LocalNetworkGateway resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param etag: Gets a unique read-only string that changes whenever the
     resource is updated
    :type etag: str
    """ 

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'local_network_address_space': {'key': 'properties.localNetworkAddressSpace', 'type': 'AddressSpace'},
        'gateway_ip_address': {'key': 'properties.gatewayIpAddress', 'type': 'str'},
        'bgp_settings': {'key': 'properties.bgpSettings', 'type': 'BgpSettings'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, location=None, tags=None, local_network_address_space=None, gateway_ip_address=None, bgp_settings=None, resource_guid=None, provisioning_state=None, etag=None):
        super(LocalNetworkGateway, self).__init__(id=id, location=location, tags=tags)
        self.local_network_address_space = local_network_address_space
        self.gateway_ip_address = gateway_ip_address
        self.bgp_settings = bgp_settings
        self.resource_guid = resource_guid
        self.provisioning_state = provisioning_state
        self.etag = etag
