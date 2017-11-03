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


class DirectoryObject(Model):
    """Represents an Azure Active Directory object.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Application, ADGroup, ServicePrincipal, User

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar object_id: The object ID.
    :vartype object_id: str
    :ivar deletion_timestamp: The time at which the directory object was
     deleted.
    :vartype deletion_timestamp: datetime
    :param object_type: Constant filled by server.
    :type object_type: str
    """

    _validation = {
        'object_id': {'readonly': True},
        'deletion_timestamp': {'readonly': True},
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
        'deletion_timestamp': {'key': 'deletionTimestamp', 'type': 'iso-8601'},
        'object_type': {'key': 'objectType', 'type': 'str'},
    }

    _subtype_map = {
        'object_type': {'Application': 'Application', 'Group': 'ADGroup', 'ServicePrincipal': 'ServicePrincipal', 'User': 'User'}
    }

    def __init__(self):
        self.object_id = None
        self.deletion_timestamp = None
        self.object_type = None