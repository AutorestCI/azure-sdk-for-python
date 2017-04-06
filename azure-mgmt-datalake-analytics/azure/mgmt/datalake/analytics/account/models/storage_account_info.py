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

from .sub_resource import SubResource


class StorageAccountInfo(SubResource):
    """Azure Storage account information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :param name: Resource name
    :type name: str
    :ivar type: Resource type
    :vartype type: str
    :param access_key: the access key associated with this Azure Storage
     account that will be used to connect to it.
    :type access_key: str
    :param suffix: the optional suffix for the storage account.
    :type suffix: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'required': True},
        'type': {'readonly': True},
        'access_key': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'access_key': {'key': 'properties.accessKey', 'type': 'str'},
        'suffix': {'key': 'properties.suffix', 'type': 'str'},
    }

    def __init__(self, name, access_key, suffix=None):
        super(StorageAccountInfo, self).__init__(name=name)
        self.access_key = access_key
        self.suffix = suffix
