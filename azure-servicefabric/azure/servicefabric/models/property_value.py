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


class PropertyValue(Model):
    """Describes a Service Fabric property value.

    :param kind: Polymorphic Discriminator
    :type kind: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'Kind', 'type': 'str'},
    }

    _subtype_map = {
        'kind': {'Binary': 'BinaryPropertyValue', 'Int64': 'Int64PropertyValue', 'Double': 'DoublePropertyValue', 'String': 'StringPropertyValue', 'Guid': 'GuidPropertyValue'}
    }

    def __init__(self):
        self.kind = None
