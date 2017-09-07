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

from .resource import Resource


class ActionGroupResource(Resource):
    """An action group resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param group_short_name: The short name of the action group. This will be
     used in SMS messages.
    :type group_short_name: str
    :param enabled: Indicates whether this action group is enabled. If an
     action group is not enabled, then none of its receivers will receive
     communications. Default value: True .
    :type enabled: bool
    :param email_receivers: The list of email receivers that are part of this
     action group.
    :type email_receivers: list of :class:`EmailReceiver
     <azure.mgmt.monitor.models.EmailReceiver>`
    :param sms_receivers: The list of SMS receivers that are part of this
     action group.
    :type sms_receivers: list of :class:`SmsReceiver
     <azure.mgmt.monitor.models.SmsReceiver>`
    :param webhook_receivers: The list of webhook receivers that are part of
     this action group.
    :type webhook_receivers: list of :class:`WebhookReceiver
     <azure.mgmt.monitor.models.WebhookReceiver>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'group_short_name': {'required': True, 'max_length': 15},
        'enabled': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'group_short_name': {'key': 'properties.groupShortName', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'email_receivers': {'key': 'properties.emailReceivers', 'type': '[EmailReceiver]'},
        'sms_receivers': {'key': 'properties.smsReceivers', 'type': '[SmsReceiver]'},
        'webhook_receivers': {'key': 'properties.webhookReceivers', 'type': '[WebhookReceiver]'},
    }

    def __init__(self, location, group_short_name, tags=None, enabled=True, email_receivers=None, sms_receivers=None, webhook_receivers=None):
        super(ActionGroupResource, self).__init__(location=location, tags=tags)
        self.group_short_name = group_short_name
        self.enabled = enabled
        self.email_receivers = email_receivers
        self.sms_receivers = sms_receivers
        self.webhook_receivers = webhook_receivers
