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


class OperationDisplay(Model):
    """The object that represents the operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provider: Service provider: Microsoft Devices
    :vartype provider: str
    :ivar resource: Resource Type: IotHubs
    :vartype resource: str
    :ivar operation: Name of the operation
    :vartype operation: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
    }

    def __init__(self):
        self.provider = None
        self.resource = None
        self.operation = None
