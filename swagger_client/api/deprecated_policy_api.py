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


class DeprecatedPolicyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def change_alert_policy_order(self, policy_id, body, **kwargs):  # noqa: E501
        """Change Alert Policy Order  # noqa: E501

        Change execution order of the alert policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_alert_policy_order(policy_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: Id of the requested policy (required)
        :param DeprecatedChangeAlertPolicyOrderPayload body: Change order payload (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_alert_policy_order_with_http_info(policy_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.change_alert_policy_order_with_http_info(policy_id, body, **kwargs)  # noqa: E501
            return data

    def change_alert_policy_order_with_http_info(self, policy_id, body, **kwargs):  # noqa: E501
        """Change Alert Policy Order  # noqa: E501

        Change execution order of the alert policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_alert_policy_order_with_http_info(policy_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: Id of the requested policy (required)
        :param DeprecatedChangeAlertPolicyOrderPayload body: Change order payload (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_alert_policy_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `change_alert_policy_order`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `change_alert_policy_order`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

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
            '/v1/policies/{policyId}/change-order', 'POST',
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

    def create_alert_policy(self, body, **kwargs):  # noqa: E501
        """Create Alert Policy  # noqa: E501

        Creates a new alert policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_alert_policy(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeprecatedAlertPolicy body: Payload of created alert policy (required)
        :return: DeprecatedCreateAlertPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_alert_policy_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_alert_policy_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_alert_policy_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Alert Policy  # noqa: E501

        Creates a new alert policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_alert_policy_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeprecatedAlertPolicy body: Payload of created alert policy (required)
        :return: DeprecatedCreateAlertPolicyResponse
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
                    " to method create_alert_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_alert_policy`")  # noqa: E501

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
            '/v1/policies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeprecatedCreateAlertPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_alert_policy(self, policy_id, **kwargs):  # noqa: E501
        """Delete Alert Policy  # noqa: E501

        Delete alert policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_alert_policy(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: Id of the requested policy (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_alert_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_alert_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def delete_alert_policy_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """Delete Alert Policy  # noqa: E501

        Delete alert policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_alert_policy_with_http_info(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: Id of the requested policy (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_alert_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `delete_alert_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

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
            '/v1/policies/{policyId}', 'DELETE',
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

    def disable_alert_policy(self, policy_id, **kwargs):  # noqa: E501
        """Disable Alert Policy  # noqa: E501

        Disable the alert policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.disable_alert_policy(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: Id of the requested policy (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.disable_alert_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.disable_alert_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def disable_alert_policy_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """Disable Alert Policy  # noqa: E501

        Disable the alert policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.disable_alert_policy_with_http_info(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: Id of the requested policy (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method disable_alert_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `disable_alert_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

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
            '/v1/policies/{policyId}/disable', 'POST',
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

    def enable_alert_policy(self, policy_id, **kwargs):  # noqa: E501
        """Enable Alert Policy  # noqa: E501

        Enable the alert policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enable_alert_policy(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: Id of the requested policy (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enable_alert_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.enable_alert_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def enable_alert_policy_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """Enable Alert Policy  # noqa: E501

        Enable the alert policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enable_alert_policy_with_http_info(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: Id of the requested policy (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enable_alert_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `enable_alert_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

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
            '/v1/policies/{policyId}/enable', 'POST',
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

    def get_alert_policy(self, policy_id, **kwargs):  # noqa: E501
        """Get Alert Policy  # noqa: E501

        Used to get details of a single policy with id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alert_policy(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: Id of the requested policy (required)
        :return: DeprecatedGetAlertPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alert_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_alert_policy_with_http_info(policy_id, **kwargs)  # noqa: E501
            return data

    def get_alert_policy_with_http_info(self, policy_id, **kwargs):  # noqa: E501
        """Get Alert Policy  # noqa: E501

        Used to get details of a single policy with id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alert_policy_with_http_info(policy_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: Id of the requested policy (required)
        :return: DeprecatedGetAlertPolicyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alert_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `get_alert_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

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
            '/v1/policies/{policyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeprecatedGetAlertPolicyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_alert_policies(self, **kwargs):  # noqa: E501
        """List Alert Policies  # noqa: E501

        Returns list alert policies  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_alert_policies(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DeprecatedListAlertPoliciesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_alert_policies_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_alert_policies_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_alert_policies_with_http_info(self, **kwargs):  # noqa: E501
        """List Alert Policies  # noqa: E501

        Returns list alert policies  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_alert_policies_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DeprecatedListAlertPoliciesResponse
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
                    " to method list_alert_policies" % key
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
            '/v1/policies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeprecatedListAlertPoliciesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_alert_policy(self, policy_id, body, **kwargs):  # noqa: E501
        """Update Alert Policy  # noqa: E501

        Update alert policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_alert_policy(policy_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: Id of the requested policy (required)
        :param DeprecatedAlertPolicy body: Payload of updated alert policy (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_alert_policy_with_http_info(policy_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_alert_policy_with_http_info(policy_id, body, **kwargs)  # noqa: E501
            return data

    def update_alert_policy_with_http_info(self, policy_id, body, **kwargs):  # noqa: E501
        """Update Alert Policy  # noqa: E501

        Update alert policy with given id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_alert_policy_with_http_info(policy_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str policy_id: Id of the requested policy (required)
        :param DeprecatedAlertPolicy body: Payload of updated alert policy (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_alert_policy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'policy_id' is set
        if ('policy_id' not in params or
                params['policy_id'] is None):
            raise ValueError("Missing the required parameter `policy_id` when calling `update_alert_policy`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_alert_policy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'policy_id' in params:
            path_params['policyId'] = params['policy_id']  # noqa: E501

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
            '/v1/policies/{policyId}', 'PUT',
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