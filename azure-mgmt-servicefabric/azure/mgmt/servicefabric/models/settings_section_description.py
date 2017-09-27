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


class SettingsSectionDescription(Model):
    """Describes a section in the fabric settings of the cluster.

    :param name: The section name of the fabric settings.
    :type name: str
    :param parameters: The collection of parameters in the section.
    :type parameters: list of :class:`SettingsParameterDescription
     <azure.mgmt.servicefabric.models.SettingsParameterDescription>`
    """

    _validation = {
        'name': {'required': True},
        'parameters': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '[SettingsParameterDescription]'},
    }

    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters
