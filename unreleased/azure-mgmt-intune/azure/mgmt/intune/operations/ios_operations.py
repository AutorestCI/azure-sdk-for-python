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


class IosOperations(object):
    """IosOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An objec model deserializer.
    :ivar api_version: Service Api Version. Constant value: "2015-01-14-preview".
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2015-01-14-preview"

        self.config = config

    def get_mam_policies(
            self, host_name, filter=None, top=None, select=None, custom_headers=None, raw=False, **operation_config):
        """Returns Intune iOSPolicies.

        :param host_name: Location hostName for the tenant
        :type host_name: str
        :param filter: The filter to apply on the operation.
        :type filter: str
        :param top:
        :type top: int
        :param select: select specific fields in entity.
        :type select: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`IOSMAMPolicyPaged
         <azure.mgmt.intune.models.IOSMAMPolicyPaged>`
        :raises:
         :class:`ErrorException<azure.mgmt.intune.models.ErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/providers/Microsoft.Intune/locations/{hostName}/iosPolicies'
                path_format_arguments = {
                    'hostName': self._serialize.url("host_name", host_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, 'str')

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
                raise models.ErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.IOSMAMPolicyPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.IOSMAMPolicyPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def get_mam_policy_by_name(
            self, host_name, policy_name, select=None, custom_headers=None, raw=False, **operation_config):
        """Returns Intune iOS policies.

        :param host_name: Location hostName for the tenant
        :type host_name: str
        :param policy_name: Unique name for the policy
        :type policy_name: str
        :param select: select specific fields in entity.
        :type select: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`IOSMAMPolicy <azure.mgmt.intune.models.IOSMAMPolicy>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.intune.models.ErrorException>`
        """
        # Construct URL
        url = '/providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}'
        path_format_arguments = {
            'hostName': self._serialize.url("host_name", host_name, 'str'),
            'policyName': self._serialize.url("policy_name", policy_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, 'str')

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
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('IOSMAMPolicy', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create_or_update_mam_policy(
            self, host_name, policy_name, parameters, custom_headers=None, raw=False, **operation_config):
        """Creates or updates iOSMAMPolicy.

        :param host_name: Location hostName for the tenant
        :type host_name: str
        :param policy_name: Unique name for the policy
        :type policy_name: str
        :param parameters: Parameters supplied to the Create or update an
         android policy operation.
        :type parameters: :class:`IOSMAMPolicy
         <azure.mgmt.intune.models.IOSMAMPolicy>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`IOSMAMPolicy <azure.mgmt.intune.models.IOSMAMPolicy>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.intune.models.ErrorException>`
        """
        # Construct URL
        url = '/providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}'
        path_format_arguments = {
            'hostName': self._serialize.url("host_name", host_name, 'str'),
            'policyName': self._serialize.url("policy_name", policy_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
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

        # Construct body
        body_content = self._serialize.body(parameters, 'IOSMAMPolicy')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('IOSMAMPolicy', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def patch_mam_policy(
            self, host_name, policy_name, parameters, custom_headers=None, raw=False, **operation_config):
        """patch an iOSMAMPolicy.

        :param host_name: Location hostName for the tenant
        :type host_name: str
        :param policy_name: Unique name for the policy
        :type policy_name: str
        :param parameters: Parameters supplied to the Create or update an
         android policy operation.
        :type parameters: :class:`IOSMAMPolicy
         <azure.mgmt.intune.models.IOSMAMPolicy>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`IOSMAMPolicy <azure.mgmt.intune.models.IOSMAMPolicy>`
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.intune.models.ErrorException>`
        """
        # Construct URL
        url = '/providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}'
        path_format_arguments = {
            'hostName': self._serialize.url("host_name", host_name, 'str'),
            'policyName': self._serialize.url("policy_name", policy_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
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

        # Construct body
        body_content = self._serialize.body(parameters, 'IOSMAMPolicy')

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('IOSMAMPolicy', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def delete_mam_policy(
            self, host_name, policy_name, custom_headers=None, raw=False, **operation_config):
        """Delete Ios Policy.

        :param host_name: Location hostName for the tenant
        :type host_name: str
        :param policy_name: Unique name for the policy
        :type policy_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.intune.models.ErrorException>`
        """
        # Construct URL
        url = '/providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}'
        path_format_arguments = {
            'hostName': self._serialize.url("host_name", host_name, 'str'),
            'policyName': self._serialize.url("policy_name", policy_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
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
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def get_app_for_mam_policy(
            self, host_name, policy_name, filter=None, top=None, select=None, custom_headers=None, raw=False, **operation_config):
        """Get apps for an iOSMAMPolicy.

        :param host_name: Location hostName for the tenant
        :type host_name: str
        :param policy_name: Unique name for the policy
        :type policy_name: str
        :param filter: The filter to apply on the operation.
        :type filter: str
        :param top:
        :type top: int
        :param select: select specific fields in entity.
        :type select: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`ApplicationPaged
         <azure.mgmt.intune.models.ApplicationPaged>`
        :raises:
         :class:`ErrorException<azure.mgmt.intune.models.ErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/apps'
                path_format_arguments = {
                    'hostName': self._serialize.url("host_name", host_name, 'str'),
                    'policyName': self._serialize.url("policy_name", policy_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, 'str')

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
                raise models.ErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.ApplicationPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ApplicationPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def add_app_for_mam_policy(
            self, host_name, policy_name, app_name, properties=None, custom_headers=None, raw=False, **operation_config):
        """Add app to an iOSMAMPolicy.

        :param host_name: Location hostName for the tenant
        :type host_name: str
        :param policy_name: Unique name for the policy
        :type policy_name: str
        :param app_name: application unique Name
        :type app_name: str
        :param properties:
        :type properties: :class:`MAMPolicyAppOrGroupIdProperties
         <azure.mgmt.intune.models.MAMPolicyAppOrGroupIdProperties>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.intune.models.ErrorException>`
        """
        parameters = models.MAMPolicyAppIdOrGroupIdPayload(properties=properties)

        # Construct URL
        url = '/providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/apps/{appName}'
        path_format_arguments = {
            'hostName': self._serialize.url("host_name", host_name, 'str'),
            'policyName': self._serialize.url("policy_name", policy_name, 'str'),
            'appName': self._serialize.url("app_name", app_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
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

        # Construct body
        body_content = self._serialize.body(parameters, 'MAMPolicyAppIdOrGroupIdPayload')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def delete_app_for_mam_policy(
            self, host_name, policy_name, app_name, custom_headers=None, raw=False, **operation_config):
        """Delete App for Ios Policy.

        :param host_name: Location hostName for the tenant
        :type host_name: str
        :param policy_name: Unique name for the policy
        :type policy_name: str
        :param app_name: application unique Name
        :type app_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.intune.models.ErrorException>`
        """
        # Construct URL
        url = '/providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/apps/{appName}'
        path_format_arguments = {
            'hostName': self._serialize.url("host_name", host_name, 'str'),
            'policyName': self._serialize.url("policy_name", policy_name, 'str'),
            'appName': self._serialize.url("app_name", app_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
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
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def get_groups_for_mam_policy(
            self, host_name, policy_name, custom_headers=None, raw=False, **operation_config):
        """Returns groups for a given iOSMAMPolicy.

        :param host_name: Location hostName for the tenant
        :type host_name: str
        :param policy_name: policy name for the tenant
        :type policy_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: :class:`GroupItemPaged
         <azure.mgmt.intune.models.GroupItemPaged>`
        :raises:
         :class:`ErrorException<azure.mgmt.intune.models.ErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/groups'
                path_format_arguments = {
                    'hostName': self._serialize.url("host_name", host_name, 'str'),
                    'policyName': self._serialize.url("policy_name", policy_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

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
                raise models.ErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.GroupItemPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.GroupItemPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def add_group_for_mam_policy(
            self, host_name, policy_name, group_id, properties=None, custom_headers=None, raw=False, **operation_config):
        """Add group to an iOSMAMPolicy.

        :param host_name: Location hostName for the tenant
        :type host_name: str
        :param policy_name: Unique name for the policy
        :type policy_name: str
        :param group_id: group Id
        :type group_id: str
        :param properties:
        :type properties: :class:`MAMPolicyAppOrGroupIdProperties
         <azure.mgmt.intune.models.MAMPolicyAppOrGroupIdProperties>`
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.intune.models.ErrorException>`
        """
        parameters = models.MAMPolicyAppIdOrGroupIdPayload(properties=properties)

        # Construct URL
        url = '/providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/groups/{groupId}'
        path_format_arguments = {
            'hostName': self._serialize.url("host_name", host_name, 'str'),
            'policyName': self._serialize.url("policy_name", policy_name, 'str'),
            'groupId': self._serialize.url("group_id", group_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
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

        # Construct body
        body_content = self._serialize.body(parameters, 'MAMPolicyAppIdOrGroupIdPayload')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def delete_group_for_mam_policy(
            self, host_name, policy_name, group_id, custom_headers=None, raw=False, **operation_config):
        """Delete Group for iOS Policy.

        :param host_name: Location hostName for the tenant
        :type host_name: str
        :param policy_name: Unique name for the policy
        :type policy_name: str
        :param group_id: application unique Name
        :type group_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :rtype: None
        :rtype: :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
         if raw=true
        :raises:
         :class:`ErrorException<azure.mgmt.intune.models.ErrorException>`
        """
        # Construct URL
        url = '/providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/groups/{groupId}'
        path_format_arguments = {
            'hostName': self._serialize.url("host_name", host_name, 'str'),
            'policyName': self._serialize.url("policy_name", policy_name, 'str'),
            'groupId': self._serialize.url("group_id", group_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
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
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200, 204]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
