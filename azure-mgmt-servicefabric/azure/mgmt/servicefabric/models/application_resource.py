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

from .proxy_resource import ProxyResource


class ApplicationResource(ProxyResource):
    """The application resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource ID.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param type_version:
    :type type_version: str
    :param parameters:
    :type parameters: list of :class:`ApplicationParameter
     <azure.mgmt.servicefabric.models.ApplicationParameter>`
    :param upgrade_policy:
    :type upgrade_policy: :class:`ApplicationUpgradePolicy
     <azure.mgmt.servicefabric.models.ApplicationUpgradePolicy>`
    :param minimum_nodes: The minimum number of nodes where Service Fabric
     will reserve capacity for this application. Note that this does not mean
     that the services of this application will be placed on all of those
     nodes. If this property is set to zero, no capacity will be reserved. The
     value of this property cannot be more than the value of the MaximumNodes
     property.
    :type minimum_nodes: long
    :param maximum_nodes: The maximum number of nodes where Service Fabric
     will reserve capacity for this application. Note that this does not mean
     that the services of this application will be placed on all of those
     nodes. By default, the value of this property is zero and it means that
     the services can be placed on any node. Default value: 0 .
    :type maximum_nodes: long
    :param remove_application_capacity: The version of the application type
    :type remove_application_capacity: bool
    :param metrics:
    :type metrics: list of :class:`ApplicationMetricDescription
     <azure.mgmt.servicefabric.models.ApplicationMetricDescription>`
    :ivar provisioning_state: The current deployment or provisioning state,
     which only appears in the response
    :vartype provisioning_state: str
    :param type_name:
    :type type_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'minimum_nodes': {'minimum': 0},
        'maximum_nodes': {'minimum': 0},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type_version': {'key': 'properties.typeVersion', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': '[ApplicationParameter]'},
        'upgrade_policy': {'key': 'properties.upgradePolicy', 'type': 'ApplicationUpgradePolicy'},
        'minimum_nodes': {'key': 'properties.minimumNodes', 'type': 'long'},
        'maximum_nodes': {'key': 'properties.maximumNodes', 'type': 'long'},
        'remove_application_capacity': {'key': 'properties.removeApplicationCapacity', 'type': 'bool'},
        'metrics': {'key': 'properties.metrics', 'type': '[ApplicationMetricDescription]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'type_name': {'key': 'properties.typeName', 'type': 'str'},
    }

    def __init__(self, location, type_version=None, parameters=None, upgrade_policy=None, minimum_nodes=None, maximum_nodes=0, remove_application_capacity=None, metrics=None, type_name=None):
        super(ApplicationResource, self).__init__(location=location)
        self.type_version = type_version
        self.parameters = parameters
        self.upgrade_policy = upgrade_policy
        self.minimum_nodes = minimum_nodes
        self.maximum_nodes = maximum_nodes
        self.remove_application_capacity = remove_application_capacity
        self.metrics = metrics
        self.provisioning_state = None
        self.type_name = type_name
