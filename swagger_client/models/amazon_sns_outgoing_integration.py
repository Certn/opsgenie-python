# coding: utf-8

"""
    Opsgenie REST API

    Opsgenie OpenAPI Specification  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AmazonSnsOutgoingIntegration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'alert_filter': 'AlertFilter',
        'forwarding_enabled': 'bool',
        'forwarding_action_mappings': 'list[ActionMapping]',
        'callback_type': 'str',
        'topic_arn': 'str',
        'region': 'str',
        'new_conf_type': 'bool'
    }

    attribute_map = {
        'alert_filter': 'alertFilter',
        'forwarding_enabled': 'forwardingEnabled',
        'forwarding_action_mappings': 'forwardingActionMappings',
        'callback_type': 'callback-type',
        'topic_arn': 'topicArn',
        'region': 'region',
        'new_conf_type': 'newConfType'
    }

    def __init__(self, alert_filter=None, forwarding_enabled=None, forwarding_action_mappings=None, callback_type=None, topic_arn=None, region=None, new_conf_type=None):  # noqa: E501
        """AmazonSnsOutgoingIntegration - a model defined in Swagger"""  # noqa: E501

        self._alert_filter = None
        self._forwarding_enabled = None
        self._forwarding_action_mappings = None
        self._callback_type = None
        self._topic_arn = None
        self._region = None
        self._new_conf_type = None
        self.discriminator = None

        if alert_filter is not None:
            self.alert_filter = alert_filter
        if forwarding_enabled is not None:
            self.forwarding_enabled = forwarding_enabled
        if forwarding_action_mappings is not None:
            self.forwarding_action_mappings = forwarding_action_mappings
        if callback_type is not None:
            self.callback_type = callback_type
        if topic_arn is not None:
            self.topic_arn = topic_arn
        if region is not None:
            self.region = region
        if new_conf_type is not None:
            self.new_conf_type = new_conf_type

    @property
    def alert_filter(self):
        """Gets the alert_filter of this AmazonSnsOutgoingIntegration.  # noqa: E501


        :return: The alert_filter of this AmazonSnsOutgoingIntegration.  # noqa: E501
        :rtype: AlertFilter
        """
        return self._alert_filter

    @alert_filter.setter
    def alert_filter(self, alert_filter):
        """Sets the alert_filter of this AmazonSnsOutgoingIntegration.


        :param alert_filter: The alert_filter of this AmazonSnsOutgoingIntegration.  # noqa: E501
        :type: AlertFilter
        """

        self._alert_filter = alert_filter

    @property
    def forwarding_enabled(self):
        """Gets the forwarding_enabled of this AmazonSnsOutgoingIntegration.  # noqa: E501


        :return: The forwarding_enabled of this AmazonSnsOutgoingIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._forwarding_enabled

    @forwarding_enabled.setter
    def forwarding_enabled(self, forwarding_enabled):
        """Sets the forwarding_enabled of this AmazonSnsOutgoingIntegration.


        :param forwarding_enabled: The forwarding_enabled of this AmazonSnsOutgoingIntegration.  # noqa: E501
        :type: bool
        """

        self._forwarding_enabled = forwarding_enabled

    @property
    def forwarding_action_mappings(self):
        """Gets the forwarding_action_mappings of this AmazonSnsOutgoingIntegration.  # noqa: E501


        :return: The forwarding_action_mappings of this AmazonSnsOutgoingIntegration.  # noqa: E501
        :rtype: list[ActionMapping]
        """
        return self._forwarding_action_mappings

    @forwarding_action_mappings.setter
    def forwarding_action_mappings(self, forwarding_action_mappings):
        """Sets the forwarding_action_mappings of this AmazonSnsOutgoingIntegration.


        :param forwarding_action_mappings: The forwarding_action_mappings of this AmazonSnsOutgoingIntegration.  # noqa: E501
        :type: list[ActionMapping]
        """

        self._forwarding_action_mappings = forwarding_action_mappings

    @property
    def callback_type(self):
        """Gets the callback_type of this AmazonSnsOutgoingIntegration.  # noqa: E501


        :return: The callback_type of this AmazonSnsOutgoingIntegration.  # noqa: E501
        :rtype: str
        """
        return self._callback_type

    @callback_type.setter
    def callback_type(self, callback_type):
        """Sets the callback_type of this AmazonSnsOutgoingIntegration.


        :param callback_type: The callback_type of this AmazonSnsOutgoingIntegration.  # noqa: E501
        :type: str
        """
        allowed_values = ["amazon-sns-callback", "base-webhook-callback", "bidirectional-callback-new", "bmc-remedy-on-demand-callback", "oec-callback"]  # noqa: E501
        if callback_type not in allowed_values:
            raise ValueError(
                "Invalid value for `callback_type` ({0}), must be one of {1}"  # noqa: E501
                .format(callback_type, allowed_values)
            )

        self._callback_type = callback_type

    @property
    def topic_arn(self):
        """Gets the topic_arn of this AmazonSnsOutgoingIntegration.  # noqa: E501


        :return: The topic_arn of this AmazonSnsOutgoingIntegration.  # noqa: E501
        :rtype: str
        """
        return self._topic_arn

    @topic_arn.setter
    def topic_arn(self, topic_arn):
        """Sets the topic_arn of this AmazonSnsOutgoingIntegration.


        :param topic_arn: The topic_arn of this AmazonSnsOutgoingIntegration.  # noqa: E501
        :type: str
        """

        self._topic_arn = topic_arn

    @property
    def region(self):
        """Gets the region of this AmazonSnsOutgoingIntegration.  # noqa: E501


        :return: The region of this AmazonSnsOutgoingIntegration.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AmazonSnsOutgoingIntegration.


        :param region: The region of this AmazonSnsOutgoingIntegration.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def new_conf_type(self):
        """Gets the new_conf_type of this AmazonSnsOutgoingIntegration.  # noqa: E501


        :return: The new_conf_type of this AmazonSnsOutgoingIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._new_conf_type

    @new_conf_type.setter
    def new_conf_type(self, new_conf_type):
        """Sets the new_conf_type of this AmazonSnsOutgoingIntegration.


        :param new_conf_type: The new_conf_type of this AmazonSnsOutgoingIntegration.  # noqa: E501
        :type: bool
        """

        self._new_conf_type = new_conf_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AmazonSnsOutgoingIntegration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AmazonSnsOutgoingIntegration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other