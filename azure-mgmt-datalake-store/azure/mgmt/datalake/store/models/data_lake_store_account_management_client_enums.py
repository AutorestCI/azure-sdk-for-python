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

from enum import Enum


class EncryptionConfigType(Enum):

    user_managed = "UserManaged"
    service_managed = "ServiceManaged"


class EncryptionState(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class EncryptionProvisioningState(Enum):

    creating = "Creating"
    succeeded = "Succeeded"


class FirewallState(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class TrustedIdProviderState(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class TierType(Enum):

    consumption = "Consumption"
    commitment_1_tb = "Commitment_1TB"
    commitment_10_tb = "Commitment_10TB"
    commitment_100_tb = "Commitment_100TB"
    commitment_500_tb = "Commitment_500TB"
    commitment_1_pb = "Commitment_1PB"
    commitment_5_pb = "Commitment_5PB"


class FirewallAllowAzureIpsState(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class DataLakeStoreAccountStatus(Enum):

    failed = "Failed"
    creating = "Creating"
    running = "Running"
    succeeded = "Succeeded"
    patching = "Patching"
    suspending = "Suspending"
    resuming = "Resuming"
    deleting = "Deleting"
    deleted = "Deleted"


class DataLakeStoreAccountState(Enum):

    active = "Active"
    suspended = "Suspended"
