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


class RuleDataSource(Model):
    """The resource from which the rule collects its data.

    :param resource_uri: the resource identifier of the resource the rule
     monitors. **NOTE**: this property cannot be updated for an existing rule.
    :type resource_uri: str
    :param odatatype: Polymorphic Discriminator
    :type odatatype: str
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'resource_uri': {'key': 'resourceUri', 'type': 'str'},
        'odatatype': {'key': 'odata\\.type', 'type': 'str'},
    }

    _subtype_map = {
        'odatatype': {'Microsoft.Azure.Management.Insights.Models.RuleMetricDataSource': 'RuleMetricDataSource', 'Microsoft.Azure.Management.Insights.Models.RuleManagementEventDataSource': 'RuleManagementEventDataSource'}
    }

    def __init__(self, resource_uri=None):
        self.resource_uri = resource_uri
        self.odatatype = None
