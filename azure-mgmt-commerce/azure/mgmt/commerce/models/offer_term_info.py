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


class OfferTermInfo(Model):
    """Describes the offer term.

    :param effective_date: Indicates the date from which the offer term is
     effective.
    :type effective_date: datetime
    :param name: Polymorphic Discriminator
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'effective_date': {'key': 'EffectiveDate', 'type': 'iso-8601'},
        'name': {'key': 'Name', 'type': 'str'},
    }

    _subtype_map = {
        'name': {'Monetary Credit': 'MonetaryCredit', 'Monetary Commitment': 'MonetaryCommitment', 'Recurring Charge': 'RecurringCharge'}
    }

    def __init__(self, effective_date=None):
        self.effective_date = effective_date
        self.name = None
