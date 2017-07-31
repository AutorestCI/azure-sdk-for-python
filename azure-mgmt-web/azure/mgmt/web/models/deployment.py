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


class Deployment(Resource):
    """User crendentials used for publishing activity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :param location: Resource Location.
    :type location: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict
    :param deployment_id: ID.
    :type deployment_id: str
    :param status: Status.
    :type status: int
    :param message: Message.
    :type message: str
    :param author: Author.
    :type author: str
    :param deployer: Deployer.
    :type deployer: str
    :param author_email: Author email.
    :type author_email: str
    :param start_time: Start time.
    :type start_time: datetime
    :param end_time: End time.
    :type end_time: datetime
    :param active: Active.
    :type active: bool
    :param details: Detail.
    :type details: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'location': {'required': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'deployment_id': {'key': 'properties.id', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'int'},
        'message': {'key': 'properties.message', 'type': 'str'},
        'author': {'key': 'properties.author', 'type': 'str'},
        'deployer': {'key': 'properties.deployer', 'type': 'str'},
        'author_email': {'key': 'properties.authorEmail', 'type': 'str'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.endTime', 'type': 'iso-8601'},
        'active': {'key': 'properties.active', 'type': 'bool'},
        'details': {'key': 'properties.details', 'type': 'str'},
    }

    def __init__(self, location, kind=None, tags=None, deployment_id=None, status=None, message=None, author=None, deployer=None, author_email=None, start_time=None, end_time=None, active=None, details=None):
        super(Deployment, self).__init__(kind=kind, location=location, tags=tags)
        self.deployment_id = deployment_id
        self.status = status
        self.message = message
        self.author = author
        self.deployer = deployer
        self.author_email = author_email
        self.start_time = start_time
        self.end_time = end_time
        self.active = active
        self.details = details
