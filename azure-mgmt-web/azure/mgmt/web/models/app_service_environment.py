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


class AppServiceEnvironment(Model):
    """Description of an App Service Environment.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: Name of the App Service Environment.
    :type name: str
    :param location: Location of the App Service Environment, e.g. "West US".
    :type location: str
    :ivar provisioning_state: Provisioning state of the App Service
     Environment. Possible values include: 'Succeeded', 'Failed', 'Canceled',
     'InProgress', 'Deleting'
    :vartype provisioning_state: str or :class:`ProvisioningState
     <azure.mgmt.web.models.ProvisioningState>`
    :ivar status: Current status of the App Service Environment. Possible
     values include: 'Preparing', 'Ready', 'Scaling', 'Deleting'
    :vartype status: str or :class:`HostingEnvironmentStatus
     <azure.mgmt.web.models.HostingEnvironmentStatus>`
    :param vnet_name: Name of the Virtual Network for the App Service
     Environment.
    :type vnet_name: str
    :param vnet_resource_group_name: Resource group of the Virtual Network.
    :type vnet_resource_group_name: str
    :param vnet_subnet_name: Subnet of the Virtual Network.
    :type vnet_subnet_name: str
    :param virtual_network: Description of the Virtual Network.
    :type virtual_network: :class:`VirtualNetworkProfile
     <azure.mgmt.web.models.VirtualNetworkProfile>`
    :param internal_load_balancing_mode: Specifies which endpoints to serve
     internally in the Virtual Network for the App Service Environment.
     Possible values include: 'None', 'Web', 'Publishing'
    :type internal_load_balancing_mode: str or
     :class:`InternalLoadBalancingMode
     <azure.mgmt.web.models.InternalLoadBalancingMode>`
    :param multi_size: Front-end VM size, e.g. "Medium", "Large".
    :type multi_size: str
    :param multi_role_count: Number of front-end instances.
    :type multi_role_count: int
    :param worker_pools: Description of worker pools with worker size IDs, VM
     sizes, and number of workers in each pool.
    :type worker_pools: list of :class:`WorkerPool
     <azure.mgmt.web.models.WorkerPool>`
    :param ipssl_address_count: Number of IP SSL addresses reserved for the
     App Service Environment.
    :type ipssl_address_count: int
    :ivar database_edition: Edition of the metadata database for the App
     Service Environment, e.g. "Standard".
    :vartype database_edition: str
    :ivar database_service_objective: Service objective of the metadata
     database for the App Service Environment, e.g. "S0".
    :vartype database_service_objective: str
    :ivar upgrade_domains: Number of upgrade domains of the App Service
     Environment.
    :vartype upgrade_domains: int
    :ivar subscription_id: Subscription of the App Service Environment.
    :vartype subscription_id: str
    :param dns_suffix: DNS suffix of the App Service Environment.
    :type dns_suffix: str
    :ivar last_action: Last deployment action on the App Service Environment.
    :vartype last_action: str
    :ivar last_action_result: Result of the last deployment action on the App
     Service Environment.
    :vartype last_action_result: str
    :ivar allowed_multi_sizes: List of comma separated strings describing
     which VM sizes are allowed for front-ends.
    :vartype allowed_multi_sizes: str
    :ivar allowed_worker_sizes: List of comma separated strings describing
     which VM sizes are allowed for workers.
    :vartype allowed_worker_sizes: str
    :ivar maximum_number_of_machines: Maximum number of VMs in the App Service
     Environment.
    :vartype maximum_number_of_machines: int
    :ivar vip_mappings: Description of IP SSL mapping for the App Service
     Environment.
    :vartype vip_mappings: list of :class:`VirtualIPMapping
     <azure.mgmt.web.models.VirtualIPMapping>`
    :ivar environment_capacities: Current total, used, and available worker
     capacities.
    :vartype environment_capacities: list of :class:`StampCapacity
     <azure.mgmt.web.models.StampCapacity>`
    :param network_access_control_list: Access control list for controlling
     traffic to the App Service Environment.
    :type network_access_control_list: list of
     :class:`NetworkAccessControlEntry
     <azure.mgmt.web.models.NetworkAccessControlEntry>`
    :ivar environment_is_healthy: True/false indicating whether the App
     Service Environment is healthy.
    :vartype environment_is_healthy: bool
    :ivar environment_status: Detailed message about with results of the last
     check of the App Service Environment.
    :vartype environment_status: str
    :param kind: Kind of the app service environment
    :type kind: str
    :ivar resource_group: Resource group of the App Service Environment.
    :vartype resource_group: str
    :param front_end_scale_factor: Scale factor for front-ends.
    :type front_end_scale_factor: int
    :ivar default_front_end_scale_factor: Default Scale Factor for FrontEnds.
    :vartype default_front_end_scale_factor: int
    :param api_management_account_id: API Management Account associated with
     the App Service Environment.
    :type api_management_account_id: str
    :param suspended: <code>true</code> if the App Service Environment is
     suspended; otherwise, <code>false</code>. The environment can be
     suspended, e.g. when the management endpoint is no longer available
     (most likely because NSG blocked the incoming traffic).
    :type suspended: bool
    :param dynamic_cache_enabled: True/false indicating whether the App
     Service Environment is suspended. The environment can be suspended e.g.
     when the management endpoint is no longer available
     (most likely because NSG blocked the incoming traffic).
    :type dynamic_cache_enabled: bool
    :param cluster_settings: Custom settings for changing the behavior of the
     App Service Environment.
    :type cluster_settings: list of :class:`NameValuePair
     <azure.mgmt.web.models.NameValuePair>`
    """

    _validation = {
        'name': {'required': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'status': {'readonly': True},
        'virtual_network': {'required': True},
        'worker_pools': {'required': True},
        'database_edition': {'readonly': True},
        'database_service_objective': {'readonly': True},
        'upgrade_domains': {'readonly': True},
        'subscription_id': {'readonly': True},
        'last_action': {'readonly': True},
        'last_action_result': {'readonly': True},
        'allowed_multi_sizes': {'readonly': True},
        'allowed_worker_sizes': {'readonly': True},
        'maximum_number_of_machines': {'readonly': True},
        'vip_mappings': {'readonly': True},
        'environment_capacities': {'readonly': True},
        'environment_is_healthy': {'readonly': True},
        'environment_status': {'readonly': True},
        'resource_group': {'readonly': True},
        'default_front_end_scale_factor': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'ProvisioningState'},
        'status': {'key': 'status', 'type': 'HostingEnvironmentStatus'},
        'vnet_name': {'key': 'vnetName', 'type': 'str'},
        'vnet_resource_group_name': {'key': 'vnetResourceGroupName', 'type': 'str'},
        'vnet_subnet_name': {'key': 'vnetSubnetName', 'type': 'str'},
        'virtual_network': {'key': 'virtualNetwork', 'type': 'VirtualNetworkProfile'},
        'internal_load_balancing_mode': {'key': 'internalLoadBalancingMode', 'type': 'InternalLoadBalancingMode'},
        'multi_size': {'key': 'multiSize', 'type': 'str'},
        'multi_role_count': {'key': 'multiRoleCount', 'type': 'int'},
        'worker_pools': {'key': 'workerPools', 'type': '[WorkerPool]'},
        'ipssl_address_count': {'key': 'ipsslAddressCount', 'type': 'int'},
        'database_edition': {'key': 'databaseEdition', 'type': 'str'},
        'database_service_objective': {'key': 'databaseServiceObjective', 'type': 'str'},
        'upgrade_domains': {'key': 'upgradeDomains', 'type': 'int'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'dns_suffix': {'key': 'dnsSuffix', 'type': 'str'},
        'last_action': {'key': 'lastAction', 'type': 'str'},
        'last_action_result': {'key': 'lastActionResult', 'type': 'str'},
        'allowed_multi_sizes': {'key': 'allowedMultiSizes', 'type': 'str'},
        'allowed_worker_sizes': {'key': 'allowedWorkerSizes', 'type': 'str'},
        'maximum_number_of_machines': {'key': 'maximumNumberOfMachines', 'type': 'int'},
        'vip_mappings': {'key': 'vipMappings', 'type': '[VirtualIPMapping]'},
        'environment_capacities': {'key': 'environmentCapacities', 'type': '[StampCapacity]'},
        'network_access_control_list': {'key': 'networkAccessControlList', 'type': '[NetworkAccessControlEntry]'},
        'environment_is_healthy': {'key': 'environmentIsHealthy', 'type': 'bool'},
        'environment_status': {'key': 'environmentStatus', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'resource_group': {'key': 'resourceGroup', 'type': 'str'},
        'front_end_scale_factor': {'key': 'frontEndScaleFactor', 'type': 'int'},
        'default_front_end_scale_factor': {'key': 'defaultFrontEndScaleFactor', 'type': 'int'},
        'api_management_account_id': {'key': 'apiManagementAccountId', 'type': 'str'},
        'suspended': {'key': 'suspended', 'type': 'bool'},
        'dynamic_cache_enabled': {'key': 'dynamicCacheEnabled', 'type': 'bool'},
        'cluster_settings': {'key': 'clusterSettings', 'type': '[NameValuePair]'},
    }

    def __init__(self, name, location, virtual_network, worker_pools, vnet_name=None, vnet_resource_group_name=None, vnet_subnet_name=None, internal_load_balancing_mode=None, multi_size=None, multi_role_count=None, ipssl_address_count=None, dns_suffix=None, network_access_control_list=None, kind=None, front_end_scale_factor=None, api_management_account_id=None, suspended=None, dynamic_cache_enabled=None, cluster_settings=None):
        self.name = name
        self.location = location
        self.provisioning_state = None
        self.status = None
        self.vnet_name = vnet_name
        self.vnet_resource_group_name = vnet_resource_group_name
        self.vnet_subnet_name = vnet_subnet_name
        self.virtual_network = virtual_network
        self.internal_load_balancing_mode = internal_load_balancing_mode
        self.multi_size = multi_size
        self.multi_role_count = multi_role_count
        self.worker_pools = worker_pools
        self.ipssl_address_count = ipssl_address_count
        self.database_edition = None
        self.database_service_objective = None
        self.upgrade_domains = None
        self.subscription_id = None
        self.dns_suffix = dns_suffix
        self.last_action = None
        self.last_action_result = None
        self.allowed_multi_sizes = None
        self.allowed_worker_sizes = None
        self.maximum_number_of_machines = None
        self.vip_mappings = None
        self.environment_capacities = None
        self.network_access_control_list = network_access_control_list
        self.environment_is_healthy = None
        self.environment_status = None
        self.kind = kind
        self.resource_group = None
        self.front_end_scale_factor = front_end_scale_factor
        self.default_front_end_scale_factor = None
        self.api_management_account_id = api_management_account_id
        self.suspended = suspended
        self.dynamic_cache_enabled = dynamic_cache_enabled
        self.cluster_settings = cluster_settings
