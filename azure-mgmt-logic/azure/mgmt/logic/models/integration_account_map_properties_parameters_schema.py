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


class IntegrationAccountMapPropertiesParametersSchema(Model):
    """The parameters schema of integration account map.

    :param ref: The reference name.
    :type ref: str
    """

    _attribute_map = {
        'ref': {'key': 'ref', 'type': 'str'},
    }

    def __init__(self, ref=None):
        self.ref = ref
