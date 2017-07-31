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


class ResourceMetricDefinition(Resource):
    """Metadata for the metrics.

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
    :ivar resource_metric_definition_name: Name of the metric.
    :vartype resource_metric_definition_name: :class:`ResourceMetricName
     <azure.mgmt.web.models.ResourceMetricName>`
    :ivar unit: Unit of the metric.
    :vartype unit: str
    :ivar primary_aggregation_type: Primary aggregation type.
    :vartype primary_aggregation_type: str
    :ivar metric_availabilities: List of time grains supported for the metric
     together with retention period.
    :vartype metric_availabilities: list of :class:`ResourceMetricAvailability
     <azure.mgmt.web.models.ResourceMetricAvailability>`
    :ivar resource_uri: Resource URI.
    :vartype resource_uri: str
    :ivar resource_metric_definition_id: Resource ID.
    :vartype resource_metric_definition_id: str
    :ivar properties: Properties.
    :vartype properties: dict
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'location': {'required': True},
        'type': {'readonly': True},
        'resource_metric_definition_name': {'readonly': True},
        'unit': {'readonly': True},
        'primary_aggregation_type': {'readonly': True},
        'metric_availabilities': {'readonly': True},
        'resource_uri': {'readonly': True},
        'resource_metric_definition_id': {'readonly': True},
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'resource_metric_definition_name': {'key': 'properties.name', 'type': 'ResourceMetricName'},
        'unit': {'key': 'properties.unit', 'type': 'str'},
        'primary_aggregation_type': {'key': 'properties.primaryAggregationType', 'type': 'str'},
        'metric_availabilities': {'key': 'properties.metricAvailabilities', 'type': '[ResourceMetricAvailability]'},
        'resource_uri': {'key': 'properties.resourceUri', 'type': 'str'},
        'resource_metric_definition_id': {'key': 'properties.id', 'type': 'str'},
        'properties': {'key': 'properties.properties', 'type': '{str}'},
    }

    def __init__(self, location, kind=None, tags=None):
        super(ResourceMetricDefinition, self).__init__(kind=kind, location=location, tags=tags)
        self.resource_metric_definition_name = None
        self.unit = None
        self.primary_aggregation_type = None
        self.metric_availabilities = None
        self.resource_uri = None
        self.resource_metric_definition_id = None
        self.properties = None
