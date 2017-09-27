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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class Operations(object):
    """Operations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def list(
            self, api_version, custom_headers=None, raw=False, **operation_config):
        """Lists all of the available ServiceFabric Resource Manager REST API
        operations.

        :param api_version: The version of the ServiceFabric resouce provider
         api
        :type api_version: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of :class:`OperationResult
         <azure.mgmt.servicefabric.models.OperationResult>`
        :rtype: :class:`OperationResultPaged
         <azure.mgmt.servicefabric.models.OperationResultPaged>`
        :raises:
         :class:`ErrorModelException<azure.mgmt.servicefabric.models.ErrorModelException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/providers/Microsoft.ServiceFabric/operations'

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorModelException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.OperationResultPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.OperationResultPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
