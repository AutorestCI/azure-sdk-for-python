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


class PipelineRun(Model):
    """Information about a pipeline run.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :ivar run_id: Identifier of a run.
    :vartype run_id: str
    :ivar pipeline_name: The pipeline name.
    :vartype pipeline_name: str
    :ivar parameters: The full or partial list of parameter name, value pair
     used in the pipeline run.
    :vartype parameters: dict[str, str]
    :ivar invoked_by: Entity that started the pipeline run.
    :vartype invoked_by: ~azure.mgmt.datafactory.models.PipelineRunInvokedBy
    :ivar last_updated: The last updated timestamp for the pipeline run event
     in ISO8601 format.
    :vartype last_updated: datetime
    :ivar run_start: The start time of a pipeline run in ISO8601 format.
    :vartype run_start: datetime
    :ivar run_end: The end time of a pipeline run in ISO8601 format.
    :vartype run_end: datetime
    :ivar duration_in_ms: The duration of a pipeline run.
    :vartype duration_in_ms: int
    :ivar status: The status of a pipeline run.
    :vartype status: str
    :ivar message: The message from a pipeline run.
    :vartype message: str
    """

    _validation = {
        'run_id': {'readonly': True},
        'pipeline_name': {'readonly': True},
        'parameters': {'readonly': True},
        'invoked_by': {'readonly': True},
        'last_updated': {'readonly': True},
        'run_start': {'readonly': True},
        'run_end': {'readonly': True},
        'duration_in_ms': {'readonly': True},
        'status': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'run_id': {'key': 'runId', 'type': 'str'},
        'pipeline_name': {'key': 'pipelineName', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'invoked_by': {'key': 'invokedBy', 'type': 'PipelineRunInvokedBy'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'run_start': {'key': 'runStart', 'type': 'iso-8601'},
        'run_end': {'key': 'runEnd', 'type': 'iso-8601'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'int'},
        'status': {'key': 'status', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, additional_properties=None):
        self.additional_properties = additional_properties
        self.run_id = None
        self.pipeline_name = None
        self.parameters = None
        self.invoked_by = None
        self.last_updated = None
        self.run_start = None
        self.run_end = None
        self.duration_in_ms = None
        self.status = None
        self.message = None