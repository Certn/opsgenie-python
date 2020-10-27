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


class NotificationRuleStepApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_notification_rule_step(self, identifier, rule_id, body, **kwargs):  # noqa: E501
        """Create Notification Rule Step  # noqa: E501

        Creates a new notification rule step  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_notification_rule_step(identifier, rule_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the user to be searched (required)
        :param str rule_id: Id of the notification rule that step will belong to. (required)
        :param CreateNotificationRuleStepPayload body: Request payload to create notification rule step (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_notification_rule_step_with_http_info(identifier, rule_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_notification_rule_step_with_http_info(identifier, rule_id, body, **kwargs)  # noqa: E501
            return data

    def create_notification_rule_step_with_http_info(self, identifier, rule_id, body, **kwargs):  # noqa: E501
        """Create Notification Rule Step  # noqa: E501

        Creates a new notification rule step  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_notification_rule_step_with_http_info(identifier, rule_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the user to be searched (required)
        :param str rule_id: Id of the notification rule that step will belong to. (required)
        :param CreateNotificationRuleStepPayload body: Request payload to create notification rule step (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'rule_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_notification_rule_step" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `create_notification_rule_step`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `create_notification_rule_step`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_notification_rule_step`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']  # noqa: E501

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
            '/v2/users/{identifier}/notification-rules/{ruleId}/steps', 'POST',
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

    def delete_notification_rule_step(self, identifier, rule_id, id, **kwargs):  # noqa: E501
        """Delete Notification Rule Step  # noqa: E501

        Deletes a notification rule step using user identifier, rule id, notification rule step id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_notification_rule_step(identifier, rule_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the user to be searched (required)
        :param str rule_id: Id of the notification rule that step will belong to. (required)
        :param str id: Id of the rule step will be changed. (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_notification_rule_step_with_http_info(identifier, rule_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_notification_rule_step_with_http_info(identifier, rule_id, id, **kwargs)  # noqa: E501
            return data

    def delete_notification_rule_step_with_http_info(self, identifier, rule_id, id, **kwargs):  # noqa: E501
        """Delete Notification Rule Step  # noqa: E501

        Deletes a notification rule step using user identifier, rule id, notification rule step id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_notification_rule_step_with_http_info(identifier, rule_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the user to be searched (required)
        :param str rule_id: Id of the notification rule that step will belong to. (required)
        :param str id: Id of the rule step will be changed. (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'rule_id', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_notification_rule_step" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `delete_notification_rule_step`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `delete_notification_rule_step`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_notification_rule_step`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v2/users/{identifier}/notification-rules/{ruleId}/steps/{id}', 'DELETE',
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

    def disable_notification_rule_step(self, identifier, rule_id, id, **kwargs):  # noqa: E501
        """Disable Notification Rule Step  # noqa: E501

        Disables a new notification rule step  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.disable_notification_rule_step(identifier, rule_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the user to be searched (required)
        :param str rule_id: Id of the notification rule that step will belong to. (required)
        :param str id: Id of the rule step will be changed. (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.disable_notification_rule_step_with_http_info(identifier, rule_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.disable_notification_rule_step_with_http_info(identifier, rule_id, id, **kwargs)  # noqa: E501
            return data

    def disable_notification_rule_step_with_http_info(self, identifier, rule_id, id, **kwargs):  # noqa: E501
        """Disable Notification Rule Step  # noqa: E501

        Disables a new notification rule step  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.disable_notification_rule_step_with_http_info(identifier, rule_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the user to be searched (required)
        :param str rule_id: Id of the notification rule that step will belong to. (required)
        :param str id: Id of the rule step will be changed. (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'rule_id', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method disable_notification_rule_step" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `disable_notification_rule_step`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `disable_notification_rule_step`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `disable_notification_rule_step`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v2/users/{identifier}/notification-rules/{ruleId}/steps/{id}/disable', 'POST',
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

    def enable_notification_rule_step(self, identifier, rule_id, id, **kwargs):  # noqa: E501
        """Enable Notification Rule Step  # noqa: E501

        Enables a new notification rule step  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enable_notification_rule_step(identifier, rule_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the user to be searched (required)
        :param str rule_id: Id of the notification rule that step will belong to. (required)
        :param str id: Id of the rule step will be changed. (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.enable_notification_rule_step_with_http_info(identifier, rule_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.enable_notification_rule_step_with_http_info(identifier, rule_id, id, **kwargs)  # noqa: E501
            return data

    def enable_notification_rule_step_with_http_info(self, identifier, rule_id, id, **kwargs):  # noqa: E501
        """Enable Notification Rule Step  # noqa: E501

        Enables a new notification rule step  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.enable_notification_rule_step_with_http_info(identifier, rule_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the user to be searched (required)
        :param str rule_id: Id of the notification rule that step will belong to. (required)
        :param str id: Id of the rule step will be changed. (required)
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'rule_id', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method enable_notification_rule_step" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `enable_notification_rule_step`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `enable_notification_rule_step`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `enable_notification_rule_step`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v2/users/{identifier}/notification-rules/{ruleId}/steps/{id}/enable', 'POST',
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

    def get_notification_rule_step(self, identifier, rule_id, id, **kwargs):  # noqa: E501
        """Get Notification Rule Step  # noqa: E501

        Returns notification rule step with given user identifier and rule id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notification_rule_step(identifier, rule_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the user to be searched (required)
        :param str rule_id: Id of the notification rule that step will belong to. (required)
        :param str id: Id of the rule step will be changed. (required)
        :return: GetNotificationRuleStepResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_notification_rule_step_with_http_info(identifier, rule_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_notification_rule_step_with_http_info(identifier, rule_id, id, **kwargs)  # noqa: E501
            return data

    def get_notification_rule_step_with_http_info(self, identifier, rule_id, id, **kwargs):  # noqa: E501
        """Get Notification Rule Step  # noqa: E501

        Returns notification rule step with given user identifier and rule id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notification_rule_step_with_http_info(identifier, rule_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the user to be searched (required)
        :param str rule_id: Id of the notification rule that step will belong to. (required)
        :param str id: Id of the rule step will be changed. (required)
        :return: GetNotificationRuleStepResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'rule_id', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notification_rule_step" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `get_notification_rule_step`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `get_notification_rule_step`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_notification_rule_step`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v2/users/{identifier}/notification-rules/{ruleId}/steps/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetNotificationRuleStepResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_notification_rule_steps(self, identifier, rule_id, **kwargs):  # noqa: E501
        """List Notification Rule Steps  # noqa: E501

        Returns list of notification rule steps  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_notification_rule_steps(identifier, rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the user to be searched (required)
        :param str rule_id: Id of the notification rule that step will belong to. (required)
        :return: ListNotificationRuleStepsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_notification_rule_steps_with_http_info(identifier, rule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_notification_rule_steps_with_http_info(identifier, rule_id, **kwargs)  # noqa: E501
            return data

    def list_notification_rule_steps_with_http_info(self, identifier, rule_id, **kwargs):  # noqa: E501
        """List Notification Rule Steps  # noqa: E501

        Returns list of notification rule steps  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_notification_rule_steps_with_http_info(identifier, rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the user to be searched (required)
        :param str rule_id: Id of the notification rule that step will belong to. (required)
        :return: ListNotificationRuleStepsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'rule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_notification_rule_steps" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `list_notification_rule_steps`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `list_notification_rule_steps`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']  # noqa: E501

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
            '/v2/users/{identifier}/notification-rules/{ruleId}/steps', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListNotificationRuleStepsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_notification_rule_step(self, identifier, rule_id, id, **kwargs):  # noqa: E501
        """Update Notification Rule Step (Partial)  # noqa: E501

        Update a notification rule step with given user identifier, rule id, and notification rule step id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_notification_rule_step(identifier, rule_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the user to be searched (required)
        :param str rule_id: Id of the notification rule that step will belong to. (required)
        :param str id: Id of the rule step will be changed. (required)
        :param UpdateNotificationRuleStepPayload body: Request payload of update schedule action
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_notification_rule_step_with_http_info(identifier, rule_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_notification_rule_step_with_http_info(identifier, rule_id, id, **kwargs)  # noqa: E501
            return data

    def update_notification_rule_step_with_http_info(self, identifier, rule_id, id, **kwargs):  # noqa: E501
        """Update Notification Rule Step (Partial)  # noqa: E501

        Update a notification rule step with given user identifier, rule id, and notification rule step id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_notification_rule_step_with_http_info(identifier, rule_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str identifier: Identifier of the user to be searched (required)
        :param str rule_id: Id of the notification rule that step will belong to. (required)
        :param str id: Id of the rule step will be changed. (required)
        :param UpdateNotificationRuleStepPayload body: Request payload of update schedule action
        :return: SuccessResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'rule_id', 'id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_notification_rule_step" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'identifier' is set
        if ('identifier' not in params or
                params['identifier'] is None):
            raise ValueError("Missing the required parameter `identifier` when calling `update_notification_rule_step`")  # noqa: E501
        # verify the required parameter 'rule_id' is set
        if ('rule_id' not in params or
                params['rule_id'] is None):
            raise ValueError("Missing the required parameter `rule_id` when calling `update_notification_rule_step`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_notification_rule_step`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'identifier' in params:
            path_params['identifier'] = params['identifier']  # noqa: E501
        if 'rule_id' in params:
            path_params['ruleId'] = params['rule_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/v2/users/{identifier}/notification-rules/{ruleId}/steps/{id}', 'PATCH',
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