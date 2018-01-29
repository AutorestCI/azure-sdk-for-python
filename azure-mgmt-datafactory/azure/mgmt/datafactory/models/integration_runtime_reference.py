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


class IntegrationRuntimeReference(Model):
    """Integration runtime reference type.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: Type of integration runtime. Default value:
     "IntegrationRuntimeReference" .
    :vartype type: str
    :param reference_name: Reference integration runtime name.
    :type reference_name: str
    :param parameters: Arguments for integration runtime.
    :type parameters: dict[str, object]
    """

    _validation = {
        'type': {'required': True, 'constant': True},
        'reference_name': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'reference_name': {'key': 'referenceName', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{object}'},
    }

    type = "IntegrationRuntimeReference"

    def __init__(self, reference_name, parameters=None):
        self.reference_name = reference_name
        self.parameters = parameters