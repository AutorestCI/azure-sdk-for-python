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


class Operation(Model):
    """Operation.

    :param id: Operation ID.
    :type id: str
    :param name: Operation name.
    :type name: str
    :param status: The current status of the operation. Possible values
     include: 'InProgress', 'Failed', 'Succeeded', 'TimedOut', 'Created'
    :type status: str or ~azure.mgmt.web.models.OperationStatus
    :param errors: Any errors associate with the operation.
    :type errors: list[~azure.mgmt.web.models.ErrorEntity]
    :param created_time: Time when operation has started.
    :type created_time: datetime
    :param modified_time: Time when operation has been updated.
    :type modified_time: datetime
    :param expiration_time: Time when operation will expire.
    :type expiration_time: datetime
    :param geo_master_operation_id: Applicable only for stamp operation ids.
    :type geo_master_operation_id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'OperationStatus'},
        'errors': {'key': 'errors', 'type': '[ErrorEntity]'},
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'modified_time': {'key': 'modifiedTime', 'type': 'iso-8601'},
        'expiration_time': {'key': 'expirationTime', 'type': 'iso-8601'},
        'geo_master_operation_id': {'key': 'geoMasterOperationId', 'type': 'str'},
    }

    def __init__(self, id=None, name=None, status=None, errors=None, created_time=None, modified_time=None, expiration_time=None, geo_master_operation_id=None):
        self.id = id
        self.name = name
        self.status = status
        self.errors = errors
        self.created_time = created_time
        self.modified_time = modified_time
        self.expiration_time = expiration_time
        self.geo_master_operation_id = geo_master_operation_id
