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


class SkuName(Enum):

    basic = "Basic"
    standard = "Standard"


class SkuTier(Enum):

    basic = "Basic"
    standard = "Standard"


class AccessRights(Enum):

    manage = "Manage"
    send = "Send"
    listen = "Listen"


class KeyType(Enum):

    primary_key = "PrimaryKey"
    secondary_key = "SecondaryKey"


class EntityStatus(Enum):

    active = "Active"
    disabled = "Disabled"
    restoring = "Restoring"
    send_disabled = "SendDisabled"
    receive_disabled = "ReceiveDisabled"
    creating = "Creating"
    deleting = "Deleting"
    renaming = "Renaming"
    unknown = "Unknown"


class EncodingCaptureDescription(Enum):

    avro = "Avro"
    avro_deflate = "AvroDeflate"


class UnavailableReason(Enum):

    none = "None"
    invalid_name = "InvalidName"
    subscription_is_disabled = "SubscriptionIsDisabled"
    name_in_use = "NameInUse"
    name_in_lockdown = "NameInLockdown"
    too_many_namespace_in_current_subscription = "TooManyNamespaceInCurrentSubscription"
