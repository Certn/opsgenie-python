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


class OutgoingCallback(object):
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
        'callback_type': 'str'
    }

    attribute_map = {
        'alert_filter': 'alertFilter',
        'alert_actions': 'alertActions',
        'callback_type': 'callback-type'
    }

    discriminator_value_class_map = {
        'nagios-based-v2-callback': 'NagiosBasedV2Callback',
        'icinga-callback': 'IcingaCallback',
        'campfire-callback': 'CampfireCallback',
        'flowdock-callback': 'FlowdockCallback',
        'icinga2-callback': 'Icinga2Callback',
        'es-watcher-callback': 'XPackAlertingCallback',
        'planio-callback': 'PlanioCallback',
        'track-it-callback': 'TrackItCallback',
        'xmpp-callback': 'XmppCallback',
        'solar-winds-web-help-desk-callback': 'SolarWindsWebHelpDeskCallback',
        'status-io-callback': 'StatusIOCallback',
        'mattermost-callback': 'MattermostCallback',
        'nagios-xiv1-callback': 'NagiosXIV1Callback',
        'connect-wise-callback': 'ConnectWiseCallback',
        'marid-callback': 'MaridCallback',
        'zenoss-callback': 'ZenossCallback',
        'slack-app-callback': 'SlackAppCallback',
        'desk-callback': 'DeskCallback',
        'bidirectional-callback': 'BidirectionalCallback',
        'hip-chat-add-on-callback': 'HipChatAddOnCallback',
        'nagios-based-v1-callback': 'NagiosBasedV1Callback',
        'nagios-xiv2-callback': 'NagiosXIV2Callback',
        'hip-chat-callback-v2': 'HipChatCallbackV2',
        'stackdriver-callback': 'StackdriverCallback',
        'flowdock-v2-callback': 'FlowdockV2Callback',
        'zabbix-callback': 'ZabbixCallback',
        'slack-callback': 'SlackCallback',
        'solarwinds-callback': 'SolarwindsCallback'
    }

    def __init__(self, alert_filter=None, alert_actions=None, callback_type=None):  # noqa: E501
        """OutgoingCallback - a model defined in Swagger"""  # noqa: E501

        self._alert_filter = None
        self._alert_actions = None
        self._callback_type = None
        self.discriminator = 'callback-type'

        if alert_filter is not None:
            self.alert_filter = alert_filter
        if alert_actions is not None:
            self.alert_actions = alert_actions
        if callback_type is not None:
            self.callback_type = callback_type

    @property
    def alert_filter(self):
        """Gets the alert_filter of this OutgoingCallback.  # noqa: E501


        :return: The alert_filter of this OutgoingCallback.  # noqa: E501
        :rtype: AlertFilter
        """
        return self._alert_filter

    @alert_filter.setter
    def alert_filter(self, alert_filter):
        """Sets the alert_filter of this OutgoingCallback.


        :param alert_filter: The alert_filter of this OutgoingCallback.  # noqa: E501
        :type: AlertFilter
        """

        self._alert_filter = alert_filter

    @property
    def alert_actions(self):
        """Gets the alert_actions of this OutgoingCallback.  # noqa: E501


        :return: The alert_actions of this OutgoingCallback.  # noqa: E501
        :rtype: list[str]
        """
        return self._alert_actions

    @alert_actions.setter
    def alert_actions(self, alert_actions):
        """Sets the alert_actions of this OutgoingCallback.


        :param alert_actions: The alert_actions of this OutgoingCallback.  # noqa: E501
        :type: list[str]
        """

        self._alert_actions = alert_actions

    @property
    def callback_type(self):
        """Gets the callback_type of this OutgoingCallback.  # noqa: E501


        :return: The callback_type of this OutgoingCallback.  # noqa: E501
        :rtype: str
        """
        return self._callback_type

    @callback_type.setter
    def callback_type(self, callback_type):
        """Sets the callback_type of this OutgoingCallback.


        :param callback_type: The callback_type of this OutgoingCallback.  # noqa: E501
        :type: str
        """
        allowed_values = ["bidirectional-callback", "campfire-callback", "flowdock-callback", "flowdock-v2-callback", "planio-callback"]  # noqa: E501
        if callback_type not in allowed_values:
            raise ValueError(
                "Invalid value for `callback_type` ({0}), must be one of {1}"  # noqa: E501
                .format(callback_type, allowed_values)
            )

        self._callback_type = callback_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(OutgoingCallback, dict):
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
        if not isinstance(other, OutgoingCallback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
