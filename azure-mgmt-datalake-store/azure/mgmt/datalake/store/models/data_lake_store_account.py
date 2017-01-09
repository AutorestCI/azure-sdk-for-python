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


class DataLakeStoreAccount(Resource):
    """Data Lake Store account information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict
    :param identity: The Key vault encryption identity, if any.
    :type identity: :class:`EncryptionIdentity
     <azure.mgmt.datalake.store.models.EncryptionIdentity>`
    :ivar provisioning_state: the status of the Data Lake Store account while
     being provisioned. Possible values include: 'Failed', 'Creating',
     'Running', 'Succeeded', 'Patching', 'Suspending', 'Resuming', 'Deleting',
     'Deleted'
    :vartype provisioning_state: str or :class:`DataLakeStoreAccountStatus
     <azure.mgmt.datalake.store.models.DataLakeStoreAccountStatus>`
    :ivar state: the status of the Data Lake Store account after provisioning
     has completed. Possible values include: 'Active', 'Suspended'
    :vartype state: str or :class:`DataLakeStoreAccountState
     <azure.mgmt.datalake.store.models.DataLakeStoreAccountState>`
    :ivar creation_time: the account creation time.
    :vartype creation_time: datetime
    :param encryption_state: The current state of encryption for this Data
     Lake store account. Possible values include: 'Enabled', 'Disabled'
    :type encryption_state: str or :class:`EncryptionState
     <azure.mgmt.datalake.store.models.EncryptionState>`
    :ivar encryption_provisioning_state: The current state of encryption
     provisioning for this Data Lake store account. Possible values include:
     'Creating', 'Succeeded'
    :vartype encryption_provisioning_state: str or
     :class:`EncryptionProvisioningState
     <azure.mgmt.datalake.store.models.EncryptionProvisioningState>`
    :param encryption_config: The Key vault encryption configuration.
    :type encryption_config: :class:`EncryptionConfig
     <azure.mgmt.datalake.store.models.EncryptionConfig>`
    :param firewall_state: The current state of the IP address firewall for
     this Data Lake store account. Possible values include: 'Enabled',
     'Disabled'
    :type firewall_state: str or :class:`FirewallState
     <azure.mgmt.datalake.store.models.FirewallState>`
    :param firewall_rules: The list of firewall rules associated with this
     Data Lake store account.
    :type firewall_rules: list of :class:`FirewallRule
     <azure.mgmt.datalake.store.models.FirewallRule>`
    :param trusted_id_provider_state: The current state of the trusted
     identity provider feature for this Data Lake store account. Possible
     values include: 'Enabled', 'Disabled'
    :type trusted_id_provider_state: str or :class:`TrustedIdProviderState
     <azure.mgmt.datalake.store.models.TrustedIdProviderState>`
    :param trusted_id_providers: The list of trusted identity providers
     associated with this Data Lake store account.
    :type trusted_id_providers: list of :class:`TrustedIdProvider
     <azure.mgmt.datalake.store.models.TrustedIdProvider>`
    :ivar last_modified_time: the account last modified time.
    :vartype last_modified_time: datetime
    :ivar endpoint: the gateway host.
    :vartype endpoint: str
    :param default_group: the default owner group for all new folders and
     files created in the Data Lake Store account.
    :type default_group: str
    :param new_tier: the commitment tier to use for next month. Possible
     values include: 'Consumption', 'Commitment_1TB', 'Commitment_10TB',
     'Commitment_100TB', 'Commitment_500TB', 'Commitment_1PB', 'Commitment_5PB'
    :type new_tier: str or :class:`TierType
     <azure.mgmt.datalake.store.models.TierType>`
    :ivar current_tier: the commitment tier in use for the current month.
     Possible values include: 'Consumption', 'Commitment_1TB',
     'Commitment_10TB', 'Commitment_100TB', 'Commitment_500TB',
     'Commitment_1PB', 'Commitment_5PB'
    :vartype current_tier: str or :class:`TierType
     <azure.mgmt.datalake.store.models.TierType>`
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'state': {'readonly': True},
        'creation_time': {'readonly': True},
        'encryption_provisioning_state': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'endpoint': {'readonly': True},
        'current_tier': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'EncryptionIdentity'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'DataLakeStoreAccountStatus'},
        'state': {'key': 'properties.state', 'type': 'DataLakeStoreAccountState'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'encryption_state': {'key': 'properties.encryptionState', 'type': 'EncryptionState'},
        'encryption_provisioning_state': {'key': 'properties.encryptionProvisioningState', 'type': 'EncryptionProvisioningState'},
        'encryption_config': {'key': 'properties.encryptionConfig', 'type': 'EncryptionConfig'},
        'firewall_state': {'key': 'properties.firewallState', 'type': 'FirewallState'},
        'firewall_rules': {'key': 'properties.firewallRules', 'type': '[FirewallRule]'},
        'trusted_id_provider_state': {'key': 'properties.trustedIdProviderState', 'type': 'TrustedIdProviderState'},
        'trusted_id_providers': {'key': 'properties.trustedIdProviders', 'type': '[TrustedIdProvider]'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'endpoint': {'key': 'properties.endpoint', 'type': 'str'},
        'default_group': {'key': 'properties.defaultGroup', 'type': 'str'},
        'new_tier': {'key': 'properties.newTier', 'type': 'TierType'},
        'current_tier': {'key': 'properties.currentTier', 'type': 'TierType'},
    }

    def __init__(self, location, tags=None, identity=None, encryption_state=None, encryption_config=None, firewall_state=None, firewall_rules=None, trusted_id_provider_state=None, trusted_id_providers=None, default_group=None, new_tier=None):
        super(DataLakeStoreAccount, self).__init__(location=location, tags=tags)
        self.identity = identity
        self.provisioning_state = None
        self.state = None
        self.creation_time = None
        self.encryption_state = encryption_state
        self.encryption_provisioning_state = None
        self.encryption_config = encryption_config
        self.firewall_state = firewall_state
        self.firewall_rules = firewall_rules
        self.trusted_id_provider_state = trusted_id_provider_state
        self.trusted_id_providers = trusted_id_providers
        self.last_modified_time = None
        self.endpoint = None
        self.default_group = default_group
        self.new_tier = new_tier
        self.current_tier = None
