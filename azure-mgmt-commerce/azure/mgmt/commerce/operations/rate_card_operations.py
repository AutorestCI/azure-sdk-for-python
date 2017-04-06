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

from msrest.pipeline import ClientRawResponse
import uuid

from .. import models


class RateCardOperations(object):
    """RateCardOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    :ivar api_version: Client Api Version. Constant value: "2015-06-01-preview".
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2015-06-01-preview"

        self.config = config

    def get(
            self, filter, custom_headers=None, raw=False, **operation_config):
        """Enables you to query for the resource/meter metadata and related prices
        used in a given subscription by Offer ID, Currency, Locale and Region.
        The metadata associated with the billing meters, including but not
        limited to service names, types, resources, units of measure, and
        regions, is subject to change at any time and without notice. If you
        intend to use this billing data in an automated fashion, please use the
        billing meter GUID to uniquely identify each billable item. If the
        billing meter GUID is scheduled to change due to a new billing model,
        you will be notified in advance of the change. .

        :param filter: The filter to apply on the operation. It ONLY supports
         the 'eq' and 'and' logical operators at this time. All the 4 query
         parameters 'OfferDurableId',  'Currency', 'Locale', 'Region' are
         required to be a part of the $filter.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`ResourceRateCardInfo
         <azure.mgmt.commerce.models.ResourceRateCardInfo>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorResponseException<azure.mgmt.commerce.models.ErrorResponseException>`
        """
        # Construct URL
        url = '/subscriptions/{subscriptionId}/providers/Microsoft.Commerce/RateCard'
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

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
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceRateCardInfo', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
