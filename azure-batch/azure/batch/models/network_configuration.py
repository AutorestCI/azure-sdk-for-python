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


class NetworkConfiguration(Model):
    """The network configuration for a pool.

    :param subnet_id: The ARM resource identifier of the virtual network
     subnet which the compute nodes of the pool will join. This is of the form
     /subscriptions/{subscription}/resourceGroups/{group}/providers/{provider}/virtualNetworks/{network}/subnets/{subnet}.
     The virtual network must be in the same region and subscription as the
     Azure Batch account. The specified subnet should have enough free IP
     addresses to accommodate the number of nodes in the pool. If the subnet
     doesn't have enough free IP addresses, the pool will partially allocate
     compute nodes, and a resize error will occur. The 'MicrosoftAzureBatch'
     service principal must have the 'Classic Virtual Machine Contributor'
     Role-Based Access Control (RBAC) role for the specified VNet. The
     specified subnet must allow communication from the Azure Batch service to
     be able to schedule tasks on the compute nodes. This can be verified by
     checking if the specified VNet has any associated Network Security Groups
     (NSG). If communication to the compute nodes in the specified subnet is
     denied by an NSG, then the Batch service will set the state of the compute
     nodes to unusable. This property can only be specified for pools created
     with a cloudServiceConfiguration.
    :type subnet_id: str
    """

    _attribute_map = {
        'subnet_id': {'key': 'subnetId', 'type': 'str'},
    }

    def __init__(self, subnet_id=None):
        self.subnet_id = subnet_id
