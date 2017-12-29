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


class PerfMonResponse(Model):
    """Performance monitor API response.

    :param code: The response code.
    :type code: str
    :param message: The message.
    :type message: str
    :param data: The performance monitor counters.
    :type data: ~azure.mgmt.web.models.PerfMonSet
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'data': {'key': 'data', 'type': 'PerfMonSet'},
    }

    def __init__(self, code=None, message=None, data=None):
        super(PerfMonResponse, self).__init__()
        self.code = code
        self.message = message
        self.data = data
