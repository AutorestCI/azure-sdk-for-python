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


class Address(Model):
    """Address information for domain registration.

    :param address1: Address 1.
    :type address1: str
    :param address2: Address 2.
    :type address2: str
    :param city: City.
    :type city: str
    :param country: Country.
    :type country: str
    :param postal_code: Postal code.
    :type postal_code: str
    :param state: State.
    :type state: str
    """

    _validation = {
        'address1': {'required': True},
        'city': {'required': True},
        'country': {'required': True},
        'postal_code': {'required': True},
        'state': {'required': True},
    }

    _attribute_map = {
        'address1': {'key': 'address1', 'type': 'str'},
        'address2': {'key': 'address2', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
        'country': {'key': 'country', 'type': 'str'},
        'postal_code': {'key': 'postalCode', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
    }

    def __init__(self, address1, city, country, postal_code, state, address2=None):
        super(Address, self).__init__()
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.country = country
        self.postal_code = postal_code
        self.state = state
