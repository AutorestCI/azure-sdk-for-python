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


class TopicCreateOrUpdateParameters(Model):
    """Parameters supplied to the Create Or Update Topic operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: Topic name.
    :type name: str
    :param location: Location of the resource.
    :type location: str
    :ivar accessed_at: Last time the message was sent, or a request was
     received, for this topic.
    :vartype accessed_at: datetime
    :param auto_delete_on_idle: TimeSpan idle interval after which the topic
     is automatically deleted. The minimum duration is 5 minutes.
    :type auto_delete_on_idle: str
    :ivar created_at: Exact time the message was created.
    :vartype created_at: datetime
    :ivar count_details:
    :vartype count_details: :class:`MessageCountDetails
     <azure.mgmt.servicebus.models.MessageCountDetails>`
    :param default_message_time_to_live: Default message time to live value.
     This is the duration after which the message expires, starting from when
     the message is sent to Service Bus. This is the default value used when
     TimeToLive is not set on a message itself.
    :type default_message_time_to_live: str
    :param duplicate_detection_history_time_window: TimeSpan structure that
     defines the duration of the duplicate detection history. The default value
     is 10 minutes.
    :type duplicate_detection_history_time_window: str
    :param enable_batched_operations: Value that indicates whether server-side
     batched operations are enabled.
    :type enable_batched_operations: bool
    :param enable_express: Value that indicates whether Express Entities are
     enabled. An express topic holds a message in memory temporarily before
     writing it to persistent storage.
    :type enable_express: bool
    :param enable_partitioning: Value that indicates whether the topic to be
     partitioned across multiple message brokers is enabled.
    :type enable_partitioning: bool
    :param max_size_in_megabytes: Maximum size of the topic in megabytes,
     which is the size of the memory allocated for the topic.
    :type max_size_in_megabytes: long
    :param requires_duplicate_detection: Value indicating if this topic
     requires duplicate detection.
    :type requires_duplicate_detection: bool
    :ivar size_in_bytes: Size of the topic, in bytes.
    :vartype size_in_bytes: long
    :param status: Enumerates the possible values for the status of a
     messaging entity. Possible values include: 'Active', 'Creating',
     'Deleting', 'Disabled', 'ReceiveDisabled', 'Renaming', 'Restoring',
     'SendDisabled', 'Unknown'
    :type status: str or :class:`EntityStatus
     <azure.mgmt.servicebus.models.EntityStatus>`
    :ivar subscription_count: Number of subscriptions.
    :vartype subscription_count: int
    :param support_ordering: Value that indicates whether the topic supports
     ordering.
    :type support_ordering: bool
    :ivar updated_at: The exact time the message was updated.
    :vartype updated_at: datetime
    """

    _validation = {
        'location': {'required': True},
        'accessed_at': {'readonly': True},
        'created_at': {'readonly': True},
        'count_details': {'readonly': True},
        'size_in_bytes': {'readonly': True},
        'subscription_count': {'readonly': True},
        'updated_at': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'accessed_at': {'key': 'properties.accessedAt', 'type': 'iso-8601'},
        'auto_delete_on_idle': {'key': 'properties.autoDeleteOnIdle', 'type': 'str'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'count_details': {'key': 'properties.countDetails', 'type': 'MessageCountDetails'},
        'default_message_time_to_live': {'key': 'properties.defaultMessageTimeToLive', 'type': 'str'},
        'duplicate_detection_history_time_window': {'key': 'properties.duplicateDetectionHistoryTimeWindow', 'type': 'str'},
        'enable_batched_operations': {'key': 'properties.enableBatchedOperations', 'type': 'bool'},
        'enable_express': {'key': 'properties.enableExpress', 'type': 'bool'},
        'enable_partitioning': {'key': 'properties.enablePartitioning', 'type': 'bool'},
        'max_size_in_megabytes': {'key': 'properties.maxSizeInMegabytes', 'type': 'long'},
        'requires_duplicate_detection': {'key': 'properties.requiresDuplicateDetection', 'type': 'bool'},
        'size_in_bytes': {'key': 'properties.sizeInBytes', 'type': 'long'},
        'status': {'key': 'properties.status', 'type': 'EntityStatus'},
        'subscription_count': {'key': 'properties.subscriptionCount', 'type': 'int'},
        'support_ordering': {'key': 'properties.supportOrdering', 'type': 'bool'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
    }

    def __init__(self, location, name=None, auto_delete_on_idle=None, default_message_time_to_live=None, duplicate_detection_history_time_window=None, enable_batched_operations=None, enable_express=None, enable_partitioning=None, max_size_in_megabytes=None, requires_duplicate_detection=None, status=None, support_ordering=None):
        self.name = name
        self.location = location
        self.accessed_at = None
        self.auto_delete_on_idle = auto_delete_on_idle
        self.created_at = None
        self.count_details = None
        self.default_message_time_to_live = default_message_time_to_live
        self.duplicate_detection_history_time_window = duplicate_detection_history_time_window
        self.enable_batched_operations = enable_batched_operations
        self.enable_express = enable_express
        self.enable_partitioning = enable_partitioning
        self.max_size_in_megabytes = max_size_in_megabytes
        self.requires_duplicate_detection = requires_duplicate_detection
        self.size_in_bytes = None
        self.status = status
        self.subscription_count = None
        self.support_ordering = support_ordering
        self.updated_at = None
