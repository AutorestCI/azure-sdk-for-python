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


class SubscriptionPolicies(Model):
    """Subscription policies.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar location_placement_id: The subscription location placement ID. The
     ID indicates which regions are visible for a subscription. For example, a
     subscription with a location placement Id of Public_2014-09-01 has access
     to Azure public regions.
    :vartype location_placement_id: str
    :ivar quota_id: The subscription quota ID.
    :vartype quota_id: str
    :ivar spending_limit: The subscription spending limit. Possible values
     include: 'On', 'Off', 'CurrentPeriodOff'
    :vartype spending_limit: str or :class:`SpendingLimit
     <azure.mgmt.resource.subscriptions.models.SpendingLimit>`
    """

    _validation = {
        'location_placement_id': {'readonly': True},
        'quota_id': {'readonly': True},
        'spending_limit': {'readonly': True},
    }

    _attribute_map = {
        'location_placement_id': {'key': 'locationPlacementId', 'type': 'str'},
        'quota_id': {'key': 'quotaId', 'type': 'str'},
        'spending_limit': {'key': 'spendingLimit', 'type': 'SpendingLimit'},
    }

    def __init__(self):
        self.location_placement_id = None
        self.quota_id = None
        self.spending_limit = None
