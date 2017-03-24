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


class Sku(Model):
    """SKU of the namespace.

    :param name: Name of this SKU. Possible values include: 'Basic',
     'Standard', 'Premium'
    :type name: str or :class:`SkuName <azure.mgmt.servicebus.models.SkuName>`
    :param tier: The billing tier of this particular SKU. Possible values
     include: 'Basic', 'Standard', 'Premium'
    :type tier: str or :class:`SkuTier <azure.mgmt.servicebus.models.SkuTier>`
    :param capacity: The specified messaging units for the tier. For Premium
     tier, capacity are 1,2 and 4.
    :type capacity: int
    """

    _validation = {
        'tier': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(self, tier, name=None, capacity=None):
        self.name = name
        self.tier = tier
        self.capacity = capacity
