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


class SubnetOverride(Model):
    """Property overrides on a subnet of a virtual network.

    :param resource_id: The resource identifier of the subnet.
    :type resource_id: str
    :param lab_subnet_name: The name given to the subnet within the lab.
    :type lab_subnet_name: str
    :param use_in_vm_creation_permission: Indicates whether this subnet can be
     used during virtual machine creation. Possible values include: 'Default',
     'Deny', 'Allow'
    :type use_in_vm_creation_permission: str or :class:`UsagePermissionType
     <azure.mgmt.devtestlabs.models.UsagePermissionType>`
    :param use_public_ip_address_permission: Indicates whether public IP
     addresses can be assigned to virtual machines on this subnet. Possible
     values include: 'Default', 'Deny', 'Allow'
    :type use_public_ip_address_permission: str or :class:`UsagePermissionType
     <azure.mgmt.devtestlabs.models.UsagePermissionType>`
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'lab_subnet_name': {'key': 'labSubnetName', 'type': 'str'},
        'use_in_vm_creation_permission': {'key': 'useInVmCreationPermission', 'type': 'str'},
        'use_public_ip_address_permission': {'key': 'usePublicIpAddressPermission', 'type': 'str'},
    }

    def __init__(self, resource_id=None, lab_subnet_name=None, use_in_vm_creation_permission=None, use_public_ip_address_permission=None):
        self.resource_id = resource_id
        self.lab_subnet_name = lab_subnet_name
        self.use_in_vm_creation_permission = use_in_vm_creation_permission
        self.use_public_ip_address_permission = use_public_ip_address_permission
