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


class CampfireIntegration(object):
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
        'alert_actions': 'list[str]',
        'callback_type': 'str',
        'token': 'str',
        'subdomain': 'str',
        'notify': 'bool',
        'rooms': 'list[str]'
    }

    attribute_map = {
        'alert_filter': 'alertFilter',
        'alert_actions': 'alertActions',
        'callback_type': 'callback-type',
        'token': 'token',
        'subdomain': 'subdomain',
        'notify': 'notify',
        'rooms': 'rooms'
    }

    def __init__(self, alert_filter=None, alert_actions=None, callback_type=None, token=None, subdomain=None, notify=None, rooms=None):  # noqa: E501
        """CampfireIntegration - a model defined in Swagger"""  # noqa: E501

        self._alert_filter = None
        self._alert_actions = None
        self._callback_type = None
        self._token = None
        self._subdomain = None
        self._notify = None
        self._rooms = None
        self.discriminator = None

        if alert_filter is not None:
            self.alert_filter = alert_filter
        if alert_actions is not None:
            self.alert_actions = alert_actions
        if callback_type is not None:
            self.callback_type = callback_type
        if token is not None:
            self.token = token
        if subdomain is not None:
            self.subdomain = subdomain
        if notify is not None:
            self.notify = notify
        if rooms is not None:
            self.rooms = rooms

    @property
    def alert_filter(self):
        """Gets the alert_filter of this CampfireIntegration.  # noqa: E501


        :return: The alert_filter of this CampfireIntegration.  # noqa: E501
        :rtype: AlertFilter
        """
        return self._alert_filter

    @alert_filter.setter
    def alert_filter(self, alert_filter):
        """Sets the alert_filter of this CampfireIntegration.


        :param alert_filter: The alert_filter of this CampfireIntegration.  # noqa: E501
        :type: AlertFilter
        """

        self._alert_filter = alert_filter

    @property
    def alert_actions(self):
        """Gets the alert_actions of this CampfireIntegration.  # noqa: E501


        :return: The alert_actions of this CampfireIntegration.  # noqa: E501
        :rtype: list[str]
        """
        return self._alert_actions

    @alert_actions.setter
    def alert_actions(self, alert_actions):
        """Sets the alert_actions of this CampfireIntegration.


        :param alert_actions: The alert_actions of this CampfireIntegration.  # noqa: E501
        :type: list[str]
        """

        self._alert_actions = alert_actions

    @property
    def callback_type(self):
        """Gets the callback_type of this CampfireIntegration.  # noqa: E501


        :return: The callback_type of this CampfireIntegration.  # noqa: E501
        :rtype: str
        """
        return self._callback_type

    @callback_type.setter
    def callback_type(self, callback_type):
        """Sets the callback_type of this CampfireIntegration.


        :param callback_type: The callback_type of this CampfireIntegration.  # noqa: E501
        :type: str
        """
        allowed_values = ["bidirectional-callback", "campfire-callback", "flowdock-callback", "flowdock-v2-callback", "planio-callback"]  # noqa: E501
        if callback_type not in allowed_values:
            raise ValueError(
                "Invalid value for `callback_type` ({0}), must be one of {1}"  # noqa: E501
                .format(callback_type, allowed_values)
            )

        self._callback_type = callback_type

    @property
    def token(self):
        """Gets the token of this CampfireIntegration.  # noqa: E501


        :return: The token of this CampfireIntegration.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this CampfireIntegration.


        :param token: The token of this CampfireIntegration.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def subdomain(self):
        """Gets the subdomain of this CampfireIntegration.  # noqa: E501


        :return: The subdomain of this CampfireIntegration.  # noqa: E501
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """Sets the subdomain of this CampfireIntegration.


        :param subdomain: The subdomain of this CampfireIntegration.  # noqa: E501
        :type: str
        """

        self._subdomain = subdomain

    @property
    def notify(self):
        """Gets the notify of this CampfireIntegration.  # noqa: E501


        :return: The notify of this CampfireIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._notify

    @notify.setter
    def notify(self, notify):
        """Sets the notify of this CampfireIntegration.


        :param notify: The notify of this CampfireIntegration.  # noqa: E501
        :type: bool
        """

        self._notify = notify

    @property
    def rooms(self):
        """Gets the rooms of this CampfireIntegration.  # noqa: E501


        :return: The rooms of this CampfireIntegration.  # noqa: E501
        :rtype: list[str]
        """
        return self._rooms

    @rooms.setter
    def rooms(self, rooms):
        """Sets the rooms of this CampfireIntegration.


        :param rooms: The rooms of this CampfireIntegration.  # noqa: E501
        :type: list[str]
        """

        self._rooms = rooms

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
        if issubclass(CampfireIntegration, dict):
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
        if not isinstance(other, CampfireIntegration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
