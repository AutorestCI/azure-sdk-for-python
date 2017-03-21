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


class AppServiceCertificateOrder(Resource):
    """SSL certificate purchase order.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :param name: Resource Name.
    :type name: str
    :param kind: Kind of resource.
    :type kind: str
    :param location: Resource Location.
    :type location: str
    :param type: Resource type.
    :type type: str
    :param tags: Resource tags.
    :type tags: dict
    :param certificates: State of the Key Vault secret.
    :type certificates: dict
    :param distinguished_name: Certificate distinguished name.
    :type distinguished_name: str
    :ivar domain_verification_token: Domain verification token.
    :vartype domain_verification_token: str
    :param validity_in_years: Duration in years (must be between 1 and 3).
     Default value: 1 .
    :type validity_in_years: int
    :param key_size: Certificate key size. Default value: 2048 .
    :type key_size: int
    :param product_type: Certificate product type. Possible values include:
     'StandardDomainValidatedSsl', 'StandardDomainValidatedWildCardSsl'
    :type product_type: str or :class:`CertificateProductType
     <azure.mgmt.web.models.CertificateProductType>`
    :param auto_renew: <code>true</code> if the certificate should be
     automatically renewed when it expires; otherwise, <code>false</code>.
     Default value: True .
    :type auto_renew: bool
    :ivar provisioning_state: Status of certificate order. Possible values
     include: 'Succeeded', 'Failed', 'Canceled', 'InProgress', 'Deleting'
    :vartype provisioning_state: str or :class:`ProvisioningState
     <azure.mgmt.web.models.ProvisioningState>`
    :ivar status: Current order status. Possible values include:
     'Pendingissuance', 'Issued', 'Revoked', 'Canceled', 'Denied',
     'Pendingrevocation', 'PendingRekey', 'Unused', 'Expired', 'NotSubmitted'
    :vartype status: str or :class:`CertificateOrderStatus
     <azure.mgmt.web.models.CertificateOrderStatus>`
    :ivar signed_certificate: Signed certificate.
    :vartype signed_certificate: :class:`CertificateDetails
     <azure.mgmt.web.models.CertificateDetails>`
    :param csr: Last CSR that was created for this order.
    :type csr: str
    :ivar intermediate: Intermediate certificate.
    :vartype intermediate: :class:`CertificateDetails
     <azure.mgmt.web.models.CertificateDetails>`
    :ivar root: Root certificate.
    :vartype root: :class:`CertificateDetails
     <azure.mgmt.web.models.CertificateDetails>`
    :ivar serial_number: Current serial number of the certificate.
    :vartype serial_number: str
    :ivar last_certificate_issuance_time: Certificate last issuance time.
    :vartype last_certificate_issuance_time: datetime
    :ivar expiration_time: Certificate expiration time.
    :vartype expiration_time: datetime
    :param is_private_key_external: <code>true</code> if private key is
     external; otherwise, <code>false</code>.
    :type is_private_key_external: bool
    :param app_service_certificate_not_renewable_reasons: Reasons why App
     Service Certificate is not renewable at the current moment.
    :type app_service_certificate_not_renewable_reasons: list of str
    """

    _validation = {
        'id': {'readonly': True},
        'location': {'required': True},
        'domain_verification_token': {'readonly': True},
        'validity_in_years': {'maximum': 3, 'minimum': 1},
        'provisioning_state': {'readonly': True},
        'status': {'readonly': True},
        'signed_certificate': {'readonly': True},
        'intermediate': {'readonly': True},
        'root': {'readonly': True},
        'serial_number': {'readonly': True},
        'last_certificate_issuance_time': {'readonly': True},
        'expiration_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'certificates': {'key': 'properties.certificates', 'type': '{AppServiceCertificate}'},
        'distinguished_name': {'key': 'properties.distinguishedName', 'type': 'str'},
        'domain_verification_token': {'key': 'properties.domainVerificationToken', 'type': 'str'},
        'validity_in_years': {'key': 'properties.validityInYears', 'type': 'int'},
        'key_size': {'key': 'properties.keySize', 'type': 'int'},
        'product_type': {'key': 'properties.productType', 'type': 'CertificateProductType'},
        'auto_renew': {'key': 'properties.autoRenew', 'type': 'bool'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
        'status': {'key': 'properties.status', 'type': 'CertificateOrderStatus'},
        'signed_certificate': {'key': 'properties.signedCertificate', 'type': 'CertificateDetails'},
        'csr': {'key': 'properties.csr', 'type': 'str'},
        'intermediate': {'key': 'properties.intermediate', 'type': 'CertificateDetails'},
        'root': {'key': 'properties.root', 'type': 'CertificateDetails'},
        'serial_number': {'key': 'properties.serialNumber', 'type': 'str'},
        'last_certificate_issuance_time': {'key': 'properties.lastCertificateIssuanceTime', 'type': 'iso-8601'},
        'expiration_time': {'key': 'properties.expirationTime', 'type': 'iso-8601'},
        'is_private_key_external': {'key': 'properties.isPrivateKeyExternal', 'type': 'bool'},
        'app_service_certificate_not_renewable_reasons': {'key': 'properties.appServiceCertificateNotRenewableReasons', 'type': '[str]'},
    }

    def __init__(self, location, name=None, kind=None, type=None, tags=None, certificates=None, distinguished_name=None, validity_in_years=1, key_size=2048, product_type=None, auto_renew=True, csr=None, is_private_key_external=None, app_service_certificate_not_renewable_reasons=None):
        super(AppServiceCertificateOrder, self).__init__(name=name, kind=kind, location=location, type=type, tags=tags)
        self.certificates = certificates
        self.distinguished_name = distinguished_name
        self.domain_verification_token = None
        self.validity_in_years = validity_in_years
        self.key_size = key_size
        self.product_type = product_type
        self.auto_renew = auto_renew
        self.provisioning_state = None
        self.status = None
        self.signed_certificate = None
        self.csr = csr
        self.intermediate = None
        self.root = None
        self.serial_number = None
        self.last_certificate_issuance_time = None
        self.expiration_time = None
        self.is_private_key_external = is_private_key_external
        self.app_service_certificate_not_renewable_reasons = app_service_certificate_not_renewable_reasons
