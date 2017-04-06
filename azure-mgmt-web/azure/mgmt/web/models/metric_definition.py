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


class MetricDefinition(Resource):
    """Metadata for a metric.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :param name: Resource Name.
    :type name: str
    :param kind: Kind of resource.
    :type kind: str
    :param location: Resource Location.
    :type location: str
    :param type: Resource type.
    :type type: str
    :param tags: Resource tags.
    :type tags: dict
    :ivar metric_definition_name: Name of the metric.
    :vartype metric_definition_name: str
    :ivar unit: Unit of the metric.
    :vartype unit: str
    :ivar primary_aggregation_type: Primary aggregation type.
    :vartype primary_aggregation_type: str
    :ivar metric_availabilities: List of time grains supported for the metric
     together with retention period.
    :vartype metric_availabilities: list of :class:`MetricAvailabilily
     <azure.mgmt.web.models.MetricAvailabilily>`
    :ivar display_name: Friendly name shown in the UI.
    :vartype display_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'location': {'required': True},
        'metric_definition_name': {'readonly': True},
        'unit': {'readonly': True},
        'primary_aggregation_type': {'readonly': True},
        'metric_availabilities': {'readonly': True},
        'display_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'metric_definition_name': {'key': 'properties.name', 'type': 'str'},
        'unit': {'key': 'properties.unit', 'type': 'str'},
        'primary_aggregation_type': {'key': 'properties.primaryAggregationType', 'type': 'str'},
        'metric_availabilities': {'key': 'properties.metricAvailabilities', 'type': '[MetricAvailabilily]'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
    }

    def __init__(self, location, name=None, kind=None, type=None, tags=None):
        super(MetricDefinition, self).__init__(name=name, kind=kind, location=location, type=type, tags=tags)
        self.metric_definition_name = None
        self.unit = None
        self.primary_aggregation_type = None
        self.metric_availabilities = None
        self.display_name = None
