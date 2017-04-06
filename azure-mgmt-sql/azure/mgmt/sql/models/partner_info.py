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


class PartnerInfo(Model):
    """PartnerInfo.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource identifier of the partner server.
    :type id: str
    :ivar location: Geo location of the partner server.
    :vartype location: str
    :ivar replication_role: Replication role of the partner server. Possible
     values include: 'Primary', 'Secondary'
    :vartype replication_role: str or :class:`FailoverGroupReplicationRole
     <azure.mgmt.sql.models.FailoverGroupReplicationRole>`
    """

    _validation = {
        'location': {'readonly': True},
        'replication_role': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'replication_role': {'key': 'replicationRole', 'type': 'str'},
    }

    def __init__(self, id=None):
        self.id = id
        self.location = None
        self.replication_role = None