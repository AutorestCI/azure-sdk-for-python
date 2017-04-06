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


class BackupSchedule(Model):
    """Description of a backup schedule. Describes how often should be the backup
    performed and what should be the retention policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param frequency_interval: How often should be the backup executed (e.g.
     for weekly backup, this should be set to 7 and FrequencyUnit should be set
     to Day). Default value: 7 .
    :type frequency_interval: int
    :param frequency_unit: The unit of time for how often should be the backup
     executed (e.g. for weekly backup, this should be set to Day and
     FrequencyInterval should be set to 7). Possible values include: 'Day',
     'Hour'. Default value: "Day" .
    :type frequency_unit: str or :class:`FrequencyUnit
     <azure.mgmt.web.models.FrequencyUnit>`
    :param keep_at_least_one_backup: True if the retention policy should
     always keep at least one backup in the storage account, regardless how old
     it is; false otherwise. Default value: True .
    :type keep_at_least_one_backup: bool
    :param retention_period_in_days: After how many days backups should be
     deleted. Default value: 90 .
    :type retention_period_in_days: int
    :param start_time: When the schedule should start working.
    :type start_time: datetime
    :ivar last_execution_time: Last time when this schedule was triggered.
    :vartype last_execution_time: datetime
    """

    _validation = {
        'frequency_interval': {'required': True},
        'frequency_unit': {'required': True},
        'keep_at_least_one_backup': {'required': True},
        'retention_period_in_days': {'required': True},
        'last_execution_time': {'readonly': True},
    }

    _attribute_map = {
        'frequency_interval': {'key': 'frequencyInterval', 'type': 'int'},
        'frequency_unit': {'key': 'frequencyUnit', 'type': 'FrequencyUnit'},
        'keep_at_least_one_backup': {'key': 'keepAtLeastOneBackup', 'type': 'bool'},
        'retention_period_in_days': {'key': 'retentionPeriodInDays', 'type': 'int'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'last_execution_time': {'key': 'lastExecutionTime', 'type': 'iso-8601'},
    }

    def __init__(self, frequency_interval=7, frequency_unit="Day", keep_at_least_one_backup=True, retention_period_in_days=90, start_time=None):
        self.frequency_interval = frequency_interval
        self.frequency_unit = frequency_unit
        self.keep_at_least_one_backup = keep_at_least_one_backup
        self.retention_period_in_days = retention_period_in_days
        self.start_time = start_time
        self.last_execution_time = None
