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


class ApplicationGatewaySslPolicy(Model):
    """Application gateway SSL policy.

    :param disabled_ssl_protocols: SSL protocols to be disabled on application
     gateway.
    :type disabled_ssl_protocols: list[str or
     ~azure.mgmt.network.v2017_03_01.models.ApplicationGatewaySslProtocol]
    """

    _attribute_map = {
        'disabled_ssl_protocols': {'key': 'disabledSslProtocols', 'type': '[str]'},
    }

    def __init__(self, disabled_ssl_protocols=None):
        self.disabled_ssl_protocols = disabled_ssl_protocols
