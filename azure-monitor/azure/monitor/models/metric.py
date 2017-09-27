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


class Metric(Model):
    """The result data of a query.

    :param id: the metric Id.
    :type id: str
    :param type: the resource type of the metric resource.
    :type type: str
    :param name: the name and the display name of the metric, i.e. it is
     localizable string.
    :type name: :class:`LocalizableString
     <azure.monitor.models.LocalizableString>`
    :param unit: the unit of the metric. Possible values include: 'Count',
     'Bytes', 'Seconds', 'CountPerSecond', 'BytesPerSecond', 'Percent',
     'MilliSeconds', 'ByteSeconds', 'Unspecified'
    :type unit: str or :class:`Unit <azure.monitor.models.Unit>`
    :param timeseries: the time series returned when a data query is
     performed.
    :type timeseries: list of :class:`TimeSeriesElement
     <azure.monitor.models.TimeSeriesElement>`
    """

    _validation = {
        'id': {'required': True},
        'type': {'required': True},
        'name': {'required': True},
        'unit': {'required': True},
        'timeseries': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'LocalizableString'},
        'unit': {'key': 'unit', 'type': 'Unit'},
        'timeseries': {'key': 'timeseries', 'type': '[TimeSeriesElement]'},
    }

    def __init__(self, id, type, name, unit, timeseries):
        self.id = id
        self.type = type
        self.name = name
        self.unit = unit
        self.timeseries = timeseries
