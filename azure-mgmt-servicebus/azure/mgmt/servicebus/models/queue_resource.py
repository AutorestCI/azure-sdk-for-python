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


class QueueResource(Resource):
    """Description of queue Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param lock_duration: The duration of a peek-lock; that is, the amount of
     time that the message is locked for other receivers. The maximum value for
     LockDuration is 5 minutes; the default value is 1 minute.
    :type lock_duration: str
    :ivar accessed_at: Last time a message was sent, or the last time there
     was a receive request to this queue.
    :vartype accessed_at: datetime
    :param auto_delete_on_idle: the TimeSpan idle interval after which the
     queue is automatically deleted. The minimum duration is 5 minutes.
    :type auto_delete_on_idle: str
    :param entity_availability_status: Entity availability status for the
     queue. Possible values include: 'Available', 'Limited', 'Renaming',
     'Restoring', 'Unknown'
    :type entity_availability_status: str or :class:`EntityAvailabilityStatus
     <azure.mgmt.servicebus.models.EntityAvailabilityStatus>`
    :ivar created_at: The exact time the message was created.
    :vartype created_at: datetime
    :param default_message_time_to_live: The default message time to live
     value. This is the duration after which the message expires, starting from
     when the message is sent to Service Bus. This is the default value used
     when TimeToLive is not set on a message itself.
    :type default_message_time_to_live: str
    :param duplicate_detection_history_time_window: TimeSpan structure that
     defines the duration of the duplicate detection history. The default value
     is 10 minutes.
    :type duplicate_detection_history_time_window: str
    :param enable_batched_operations: A value that indicates whether
     server-side batched operations are enabled.
    :type enable_batched_operations: bool
    :param dead_lettering_on_message_expiration: A value that indicates
     whether this queue has dead letter support when a message expires.
    :type dead_lettering_on_message_expiration: bool
    :param enable_express: A value that indicates whether Express Entities are
     enabled. An express queue holds a message in memory temporarily before
     writing it to persistent storage.
    :type enable_express: bool
    :param enable_partitioning: A value that indicates whether the queue is to
     be partitioned across multiple message brokers.
    :type enable_partitioning: bool
    :param is_anonymous_accessible: A value that indicates whether the message
     is accessible anonymously.
    :type is_anonymous_accessible: bool
    :param max_delivery_count: The maximum delivery count. A message is
     automatically deadlettered after this number of deliveries.
    :type max_delivery_count: int
    :param max_size_in_megabytes: The maximum size of the queue in megabytes,
     which is the size of memory allocated for the queue.
    :type max_size_in_megabytes: long
    :ivar message_count: The number of messages in the queue.
    :vartype message_count: long
    :ivar count_details:
    :vartype count_details: :class:`MessageCountDetails
     <azure.mgmt.servicebus.models.MessageCountDetails>`
    :param requires_duplicate_detection: A value indicating if this queue
     requires duplicate detection.
    :type requires_duplicate_detection: bool
    :param requires_session: A value that indicates whether the queue supports
     the concept of sessions.
    :type requires_session: bool
    :ivar size_in_bytes: The size of the queue, in bytes.
    :vartype size_in_bytes: long
    :param status: Enumerates the possible values for the status of a
     messaging entity. Possible values include: 'Active', 'Creating',
     'Deleting', 'Disabled', 'ReceiveDisabled', 'Renaming', 'Restoring',
     'SendDisabled', 'Unknown'
    :type status: str or :class:`EntityStatus
     <azure.mgmt.servicebus.models.EntityStatus>`
    :param support_ordering: A value that indicates whether the queue supports
     ordering.
    :type support_ordering: bool
    :ivar updated_at: The exact time the message was updated.
    :vartype updated_at: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'accessed_at': {'readonly': True},
        'created_at': {'readonly': True},
        'message_count': {'readonly': True},
        'count_details': {'readonly': True},
        'size_in_bytes': {'readonly': True},
        'updated_at': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'lock_duration': {'key': 'properties.lockDuration', 'type': 'str'},
        'accessed_at': {'key': 'properties.accessedAt', 'type': 'iso-8601'},
        'auto_delete_on_idle': {'key': 'properties.autoDeleteOnIdle', 'type': 'str'},
        'entity_availability_status': {'key': 'properties.entityAvailabilityStatus', 'type': 'EntityAvailabilityStatus'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'default_message_time_to_live': {'key': 'properties.defaultMessageTimeToLive', 'type': 'str'},
        'duplicate_detection_history_time_window': {'key': 'properties.duplicateDetectionHistoryTimeWindow', 'type': 'str'},
        'enable_batched_operations': {'key': 'properties.enableBatchedOperations', 'type': 'bool'},
        'dead_lettering_on_message_expiration': {'key': 'properties.deadLetteringOnMessageExpiration', 'type': 'bool'},
        'enable_express': {'key': 'properties.enableExpress', 'type': 'bool'},
        'enable_partitioning': {'key': 'properties.enablePartitioning', 'type': 'bool'},
        'is_anonymous_accessible': {'key': 'properties.isAnonymousAccessible', 'type': 'bool'},
        'max_delivery_count': {'key': 'properties.maxDeliveryCount', 'type': 'int'},
        'max_size_in_megabytes': {'key': 'properties.maxSizeInMegabytes', 'type': 'long'},
        'message_count': {'key': 'properties.messageCount', 'type': 'long'},
        'count_details': {'key': 'properties.countDetails', 'type': 'MessageCountDetails'},
        'requires_duplicate_detection': {'key': 'properties.requiresDuplicateDetection', 'type': 'bool'},
        'requires_session': {'key': 'properties.requiresSession', 'type': 'bool'},
        'size_in_bytes': {'key': 'properties.sizeInBytes', 'type': 'long'},
        'status': {'key': 'properties.status', 'type': 'EntityStatus'},
        'support_ordering': {'key': 'properties.supportOrdering', 'type': 'bool'},
        'updated_at': {'key': 'properties.updatedAt', 'type': 'iso-8601'},
    }

    def __init__(self, lock_duration=None, auto_delete_on_idle=None, entity_availability_status=None, default_message_time_to_live=None, duplicate_detection_history_time_window=None, enable_batched_operations=None, dead_lettering_on_message_expiration=None, enable_express=None, enable_partitioning=None, is_anonymous_accessible=None, max_delivery_count=None, max_size_in_megabytes=None, requires_duplicate_detection=None, requires_session=None, status=None, support_ordering=None):
        super(QueueResource, self).__init__()
        self.lock_duration = lock_duration
        self.accessed_at = None
        self.auto_delete_on_idle = auto_delete_on_idle
        self.entity_availability_status = entity_availability_status
        self.created_at = None
        self.default_message_time_to_live = default_message_time_to_live
        self.duplicate_detection_history_time_window = duplicate_detection_history_time_window
        self.enable_batched_operations = enable_batched_operations
        self.dead_lettering_on_message_expiration = dead_lettering_on_message_expiration
        self.enable_express = enable_express
        self.enable_partitioning = enable_partitioning
        self.is_anonymous_accessible = is_anonymous_accessible
        self.max_delivery_count = max_delivery_count
        self.max_size_in_megabytes = max_size_in_megabytes
        self.message_count = None
        self.count_details = None
        self.requires_duplicate_detection = requires_duplicate_detection
        self.requires_session = requires_session
        self.size_in_bytes = None
        self.status = status
        self.support_ordering = support_ordering
        self.updated_at = None
