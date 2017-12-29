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


class ImageStorageProfile(Model):
    """Describes a storage profile.

    :param os_disk: Specifies information about the operating system disk used
     by the virtual machine. <br><br> For more information about disks, see
     [About disks and VHDs for Azure virtual
     machines](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json).
    :type os_disk: :class:`ImageOSDisk
     <azure.mgmt.compute.compute.v2017_03_30.models.ImageOSDisk>`
    :param data_disks: Specifies the parameters that are used to add a data
     disk to a virtual machine. <br><br> For more information about disks, see
     [About disks and VHDs for Azure virtual
     machines](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-about-disks-vhds?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json).
    :type data_disks: list of :class:`ImageDataDisk
     <azure.mgmt.compute.compute.v2017_03_30.models.ImageDataDisk>`
    """

    _validation = {
        'os_disk': {'required': True},
    }

    _attribute_map = {
        'os_disk': {'key': 'osDisk', 'type': 'ImageOSDisk'},
        'data_disks': {'key': 'dataDisks', 'type': '[ImageDataDisk]'},
    }

    def __init__(self, os_disk, data_disks=None):
        self.os_disk = os_disk
        self.data_disks = data_disks