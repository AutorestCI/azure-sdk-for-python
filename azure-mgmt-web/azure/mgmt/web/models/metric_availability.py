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


class MetricAvailability(Model):
    """MetricAvailability.

    :param time_grain:
    :type time_grain: str
    :param blob_duration:
    :type blob_duration: str
    """

    _attribute_map = {
        'time_grain': {'key': 'timeGrain', 'type': 'str'},
        'blob_duration': {'key': 'blobDuration', 'type': 'str'},
    }

    def __init__(self, time_grain=None, blob_duration=None):
        super(MetricAvailability, self).__init__()
        self.time_grain = time_grain
        self.blob_duration = blob_duration
