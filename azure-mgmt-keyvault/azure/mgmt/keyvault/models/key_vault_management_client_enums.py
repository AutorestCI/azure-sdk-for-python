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

    standard = "standard"
    premium = "premium"


class KeyPermissions(Enum):

    all = "all"
    encrypt = "encrypt"
    decrypt = "decrypt"
    wrap_key = "wrapKey"
    unwrap_key = "unwrapKey"
    sign = "sign"
    verify = "verify"
    get = "get"
    list = "list"
    create = "create"
    update = "update"
    import_enum = "import"
    delete = "delete"
    backup = "backup"
    restore = "restore"
    recover = "recover"
    purge = "purge"


class SecretPermissions(Enum):

    all = "all"
    get = "get"
    list = "list"
    set = "set"
    delete = "delete"
    backup = "backup"
    restore = "restore"
    recover = "recover"
    purge = "purge"


class CertificatePermissions(Enum):

    all = "all"
    get = "get"
    list = "list"
    delete = "delete"
    create = "create"
    import_enum = "import"
    update = "update"
    managecontacts = "managecontacts"
    getissuers = "getissuers"
    listissuers = "listissuers"
    setissuers = "setissuers"
    deleteissuers = "deleteissuers"
    manageissuers = "manageissuers"
    recover = "recover"
    purge = "purge"
