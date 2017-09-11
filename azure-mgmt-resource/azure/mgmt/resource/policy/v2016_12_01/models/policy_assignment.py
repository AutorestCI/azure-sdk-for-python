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


class PolicyAssignment(Model):
    """The policy assignment.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param display_name: The display name of the policy assignment.
    :type display_name: str
    :param policy_definition_id: The ID of the policy definition.
    :type policy_definition_id: str
    :param scope: The scope for the policy assignment.
    :type scope: str
    :param not_scopes: The policy's excluded scopes.
    :type not_scopes: list of str
    :param parameters: Required if a parameter is used in policy rule.
    :type parameters: object
    :param metadata: The policy assignment metadata.
    :type metadata: object
    :param description: This message will be part of response in case of
     policy violation.
    :type description: str
    :ivar id: The ID of the policy assignment.
    :vartype id: str
    :param type: The type of the policy assignment.
    :type type: str
    :param name: The name of the policy assignment.
    :type name: str
    :param sku: The policy sku.
    :type sku: :class:`PolicySku
     <azure.mgmt.resource.policy.v2016_12_01.models.PolicySku>`
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'policy_definition_id': {'key': 'properties.policyDefinitionId', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'not_scopes': {'key': 'properties.notScopes', 'type': '[str]'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'PolicySku'},
    }

    def __init__(self, display_name=None, policy_definition_id=None, scope=None, not_scopes=None, parameters=None, metadata=None, description=None, type=None, name=None, sku=None):
        self.display_name = display_name
        self.policy_definition_id = policy_definition_id
        self.scope = scope
        self.not_scopes = not_scopes
        self.parameters = parameters
        self.metadata = metadata
        self.description = description
        self.id = None
        self.type = type
        self.name = name
        self.sku = sku
