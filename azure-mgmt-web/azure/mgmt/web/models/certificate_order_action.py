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

from .proxy_only_resource import ProxyOnlyResource


class CertificateOrderAction(ProxyOnlyResource):
    """Certificate order action.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param certificate_order_action_type: Action type. Possible values
     include: 'CertificateIssued', 'CertificateOrderCanceled',
     'CertificateOrderCreated', 'CertificateRevoked',
     'DomainValidationComplete', 'FraudDetected', 'OrgNameChange',
     'OrgValidationComplete', 'SanDrop', 'FraudCleared', 'CertificateExpired',
     'CertificateExpirationWarning', 'FraudDocumentationRequired', 'Unknown'
    :type certificate_order_action_type: str or
     ~azure.mgmt.web.models.CertificateOrderActionType
    :param created_at: Time at which the certificate action was performed.
    :type created_at: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'certificate_order_action_type': {'key': 'properties.type', 'type': 'CertificateOrderActionType'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
    }

    def __init__(self, kind=None, certificate_order_action_type=None, created_at=None):
        super(CertificateOrderAction, self).__init__(kind=kind)
        self.certificate_order_action_type = certificate_order_action_type
        self.created_at = created_at
