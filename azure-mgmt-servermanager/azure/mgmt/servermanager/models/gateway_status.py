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


class GatewayStatus(Model):
    """Expanded gateway status information.

    :param available_memory_mbyte: The available memory on the gateway host
     machine in megabytes.
    :type available_memory_mbyte: float
    :param gateway_cpu_utilization_percent: The CPU utilization of the gateway
     process (numeric value between 0 and 100).
    :type gateway_cpu_utilization_percent: float
    :param total_cpu_utilization_percent: CPU Utilization of the whole system.
    :type total_cpu_utilization_percent: float
    :param gateway_version: The version of the gateway that is installed on
     the system.
    :type gateway_version: str
    :param friendly_os_name: The Plaintext description of the OS on the
     gateway.
    :type friendly_os_name: str
    :param installed_date: The date the gateway was installed.
    :type installed_date: datetime
    :param logical_processor_count: Number of logical processors in the
     gateway system.
    :type logical_processor_count: int
    :param name: The computer name of the gateway system.
    :type name: str
    :param gateway_id: The gateway resource ID.
    :type gateway_id: str
    :param gateway_working_set_mbyte: The working set size of the gateway
     process in megabytes.
    :type gateway_working_set_mbyte: float
    :param status_updated: UTC date and time when gateway status was last
     updated.
    :type status_updated: datetime
    :param group_policy_error: The group policy error.
    :type group_policy_error: str
    :param allow_gateway_group_policy_status: Status of the
     allowGatewayGroupPolicy setting.
    :type allow_gateway_group_policy_status: bool
    :param require_mfa_group_policy_status: Status of the
     requireMfaGroupPolicy setting.
    :type require_mfa_group_policy_status: bool
    :param encryption_certificate_thumbprint: Thumbprint of the encryption
     certificate.
    :type encryption_certificate_thumbprint: str
    :param secondary_encryption_certificate_thumbprint: Secondary thumbprint
     of the encryption certificate.
    :type secondary_encryption_certificate_thumbprint: str
    :param encryption_jwk: The encryption certificate key.
    :type encryption_jwk: :class:`EncryptionJwkResource
     <azure.mgmt.servermanager.models.EncryptionJwkResource>`
    :param secondary_encryption_jwk: The secondary encryption certificate key.
    :type secondary_encryption_jwk: :class:`EncryptionJwkResource
     <azure.mgmt.servermanager.models.EncryptionJwkResource>`
    :param active_message_count: Active message count.
    :type active_message_count: int
    :param latest_published_msi_version: Latest published version of the
     gateway install MSI.
    :type latest_published_msi_version: str
    :param published_time_utc: Gateway install MSI published time.
    :type published_time_utc: datetime
    """

    _validation = {
        'gateway_cpu_utilization_percent': {'maximum': 100, 'minimum': 0},
    }

    _attribute_map = {
        'available_memory_mbyte': {'key': 'availableMemoryMByte', 'type': 'float'},
        'gateway_cpu_utilization_percent': {'key': 'gatewayCpuUtilizationPercent', 'type': 'float'},
        'total_cpu_utilization_percent': {'key': 'totalCpuUtilizationPercent', 'type': 'float'},
        'gateway_version': {'key': 'gatewayVersion', 'type': 'str'},
        'friendly_os_name': {'key': 'friendlyOsName', 'type': 'str'},
        'installed_date': {'key': 'installedDate', 'type': 'iso-8601'},
        'logical_processor_count': {'key': 'logicalProcessorCount', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'gateway_id': {'key': 'gatewayId', 'type': 'str'},
        'gateway_working_set_mbyte': {'key': 'gatewayWorkingSetMByte', 'type': 'float'},
        'status_updated': {'key': 'statusUpdated', 'type': 'iso-8601'},
        'group_policy_error': {'key': 'groupPolicyError', 'type': 'str'},
        'allow_gateway_group_policy_status': {'key': 'allowGatewayGroupPolicyStatus', 'type': 'bool'},
        'require_mfa_group_policy_status': {'key': 'requireMfaGroupPolicyStatus', 'type': 'bool'},
        'encryption_certificate_thumbprint': {'key': 'encryptionCertificateThumbprint', 'type': 'str'},
        'secondary_encryption_certificate_thumbprint': {'key': 'secondaryEncryptionCertificateThumbprint', 'type': 'str'},
        'encryption_jwk': {'key': 'encryptionJwk', 'type': 'EncryptionJwkResource'},
        'secondary_encryption_jwk': {'key': 'secondaryEncryptionJwk', 'type': 'EncryptionJwkResource'},
        'active_message_count': {'key': 'activeMessageCount', 'type': 'int'},
        'latest_published_msi_version': {'key': 'latestPublishedMsiVersion', 'type': 'str'},
        'published_time_utc': {'key': 'publishedTimeUtc', 'type': 'iso-8601'},
    }

    def __init__(self, available_memory_mbyte=None, gateway_cpu_utilization_percent=None, total_cpu_utilization_percent=None, gateway_version=None, friendly_os_name=None, installed_date=None, logical_processor_count=None, name=None, gateway_id=None, gateway_working_set_mbyte=None, status_updated=None, group_policy_error=None, allow_gateway_group_policy_status=None, require_mfa_group_policy_status=None, encryption_certificate_thumbprint=None, secondary_encryption_certificate_thumbprint=None, encryption_jwk=None, secondary_encryption_jwk=None, active_message_count=None, latest_published_msi_version=None, published_time_utc=None):
        self.available_memory_mbyte = available_memory_mbyte
        self.gateway_cpu_utilization_percent = gateway_cpu_utilization_percent
        self.total_cpu_utilization_percent = total_cpu_utilization_percent
        self.gateway_version = gateway_version
        self.friendly_os_name = friendly_os_name
        self.installed_date = installed_date
        self.logical_processor_count = logical_processor_count
        self.name = name
        self.gateway_id = gateway_id
        self.gateway_working_set_mbyte = gateway_working_set_mbyte
        self.status_updated = status_updated
        self.group_policy_error = group_policy_error
        self.allow_gateway_group_policy_status = allow_gateway_group_policy_status
        self.require_mfa_group_policy_status = require_mfa_group_policy_status
        self.encryption_certificate_thumbprint = encryption_certificate_thumbprint
        self.secondary_encryption_certificate_thumbprint = secondary_encryption_certificate_thumbprint
        self.encryption_jwk = encryption_jwk
        self.secondary_encryption_jwk = secondary_encryption_jwk
        self.active_message_count = active_message_count
        self.latest_published_msi_version = latest_published_msi_version
        self.published_time_utc = published_time_utc
