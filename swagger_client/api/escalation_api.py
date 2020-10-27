# coding: utf-8

"""
    Opsgenie REST API

    Opsgenie OpenAPI Specification  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class EscalationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_escalation(self, body, **kwargs):  # noqa: E501
        """Create Escalation  # noqa: E501

        Creates a new escalation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_escalation(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateEscalationPayload body: Request payload of created escalation (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_escalation_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_escalation_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_escalation_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Escalation  # noqa: E501

        Creates a new escalation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_escalation_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateEscalationPayload body: Request payload of created escalation (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_escalation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_escalation`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/escalations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_escalation(self, identifier, **kwargs):  # noqa: E501
        """Delete Escalation  # noqa: E501

        Deletes an escalation using escalation 'id' or 'name'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_escalation(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of escalation which could be escalation 'id' or 'name' (required)
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_escalation_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_escalation_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def delete_escalation_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Delete Escalation  # noqa: E501

        Deletes an escalation using escalation 'id' or 'name'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_escalation_with_http_info(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of escalation which could be escalation 'id' or 'name' (required)
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'identifier_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_escalation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `delete_escalation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'identifier_type' in params:
            query_params.append(('identifierType', params['identifier_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/escalations/{identifier}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_escalation(self, identifier, **kwargs):  # noqa: E501
        """Get Escalation  # noqa: E501

        Returns escalation with given 'id' or 'name'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_escalation(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of escalation which could be escalation 'id' or 'name' (required)
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: GetEscalationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_escalation_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.get_escalation_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def get_escalation_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Get Escalation  # noqa: E501

        Returns escalation with given 'id' or 'name'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_escalation_with_http_info(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of escalation which could be escalation 'id' or 'name' (required)
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :return: GetEscalationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'identifier_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_escalation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_escalation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'identifier_type' in params:
            query_params.append(('identifierType', params['identifier_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/escalations/{identifier}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetEscalationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_escalations(self, **kwargs):  # noqa: E501
        """List Escalations  # noqa: E501

        Returns list of escalations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_escalations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ListEscalationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_escalations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_escalations_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_escalations_with_http_info(self, **kwargs):  # noqa: E501
        """List Escalations  # noqa: E501

        Returns list of escalations  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_escalations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ListEscalationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_escalations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/escalations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListEscalationsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_escalation(self, identifier, **kwargs):  # noqa: E501
        """Update Escalation (Partial)  # noqa: E501

        Updates the escalation using escalation 'id' or 'name'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_escalation(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of escalation which could be escalation 'id' or 'name' (required)
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :param UpdateEscalationPayload body: Request payload of update escalation
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_escalation_with_http_info(identifier, **kwargs)  # noqa: E501
        else:
            (data) = self.update_escalation_with_http_info(identifier, **kwargs)  # noqa: E501
            return data

    def update_escalation_with_http_info(self, identifier, **kwargs):  # noqa: E501
        """Update Escalation (Partial)  # noqa: E501

        Updates the escalation using escalation 'id' or 'name'  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_escalation_with_http_info(identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of escalation which could be escalation 'id' or 'name' (required)
        :param str identifier_type: Type of the identifier that is provided as an in-line parameter. Possible values are 'id' or 'name'
        :param UpdateEscalationPayload body: Request payload of update escalation
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'identifier_type', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_escalation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `update_escalation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501

        query_params = []
        if 'identifier_type' in params:
            query_params.append(('identifierType', params['identifier_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['GenieKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/escalations/{identifier}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)