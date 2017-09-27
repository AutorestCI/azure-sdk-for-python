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

from .rule_action import RuleAction


class RuleEmailAction(RuleAction):
    """Specifies the action to send email when the rule condition is evaluated.
    The discriminator is always RuleEmailAction in this case.

    :param odatatype: Polymorphic Discriminator
    :type odatatype: str
    :param send_to_service_owners: Whether the administrators (service and
     co-administrators) of the service should be notified when the alert is
     activated.
    :type send_to_service_owners: bool
    :param custom_emails: the list of administrator's custom email addresses
     to notify of the activation of the alert.
    :type custom_emails: list of str
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': 'odata\\.type', 'type': 'str'},
        'send_to_service_owners': {'key': 'sendToServiceOwners', 'type': 'bool'},
        'custom_emails': {'key': 'customEmails', 'type': '[str]'},
    }

    def __init__(self, send_to_service_owners=None, custom_emails=None):
        super(RuleEmailAction, self).__init__()
        self.send_to_service_owners = send_to_service_owners
        self.custom_emails = custom_emails
        self.odatatype = 'Microsoft.Azure.Management.Insights.Models.RuleEmailAction'
