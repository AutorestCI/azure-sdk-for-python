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


class NodeDisableSchedulingParameter(Model):
    """Options for disabling scheduling on a compute node.

    :param node_disable_scheduling_option: What to do with currently running
     tasks when disabling task scheduling on the compute node. The default
     value is requeue. Possible values include: 'requeue', 'terminate',
     'taskCompletion'
    :type node_disable_scheduling_option: str or
     ~azure.batch.models.DisableComputeNodeSchedulingOption
    """

    _attribute_map = {
        'node_disable_scheduling_option': {'key': 'nodeDisableSchedulingOption', 'type': 'DisableComputeNodeSchedulingOption'},
    }

    def __init__(self, node_disable_scheduling_option=None):
        self.node_disable_scheduling_option = node_disable_scheduling_option
