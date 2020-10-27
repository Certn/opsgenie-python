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


class UpdateTeamRoutingRulePayload(object):
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
        'name': 'str',
        'criteria': 'Filter',
        'time_restriction': 'TimeRestrictionInterval',
        'notify': 'Recipient',
        'timezone': 'str'
    }

    attribute_map = {
        'name': 'name',
        'criteria': 'criteria',
        'time_restriction': 'timeRestriction',
        'notify': 'notify',
        'timezone': 'timezone'
    }

    def __init__(self, name=None, criteria=None, time_restriction=None, notify=None, timezone=None):  # noqa: E501
        """UpdateTeamRoutingRulePayload - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._criteria = None
        self._time_restriction = None
        self._notify = None
        self._timezone = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if criteria is not None:
            self.criteria = criteria
        if time_restriction is not None:
            self.time_restriction = time_restriction
        if notify is not None:
            self.notify = notify
        if timezone is not None:
            self.timezone = timezone

    @property
    def name(self):
        """Gets the name of this UpdateTeamRoutingRulePayload.  # noqa: E501

        Name of the team routing rule  # noqa: E501

        :return: The name of this UpdateTeamRoutingRulePayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTeamRoutingRulePayload.

        Name of the team routing rule  # noqa: E501

        :param name: The name of this UpdateTeamRoutingRulePayload.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def criteria(self):
        """Gets the criteria of this UpdateTeamRoutingRulePayload.  # noqa: E501


        :return: The criteria of this UpdateTeamRoutingRulePayload.  # noqa: E501
        :rtype: Filter
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """Sets the criteria of this UpdateTeamRoutingRulePayload.


        :param criteria: The criteria of this UpdateTeamRoutingRulePayload.  # noqa: E501
        :type: Filter
        """

        self._criteria = criteria

    @property
    def time_restriction(self):
        """Gets the time_restriction of this UpdateTeamRoutingRulePayload.  # noqa: E501


        :return: The time_restriction of this UpdateTeamRoutingRulePayload.  # noqa: E501
        :rtype: TimeRestrictionInterval
        """
        return self._time_restriction

    @time_restriction.setter
    def time_restriction(self, time_restriction):
        """Sets the time_restriction of this UpdateTeamRoutingRulePayload.


        :param time_restriction: The time_restriction of this UpdateTeamRoutingRulePayload.  # noqa: E501
        :type: TimeRestrictionInterval
        """

        self._time_restriction = time_restriction

    @property
    def notify(self):
        """Gets the notify of this UpdateTeamRoutingRulePayload.  # noqa: E501


        :return: The notify of this UpdateTeamRoutingRulePayload.  # noqa: E501
        :rtype: Recipient
        """
        return self._notify

    @notify.setter
    def notify(self, notify):
        """Sets the notify of this UpdateTeamRoutingRulePayload.


        :param notify: The notify of this UpdateTeamRoutingRulePayload.  # noqa: E501
        :type: Recipient
        """

        self._notify = notify

    @property
    def timezone(self):
        """Gets the timezone of this UpdateTeamRoutingRulePayload.  # noqa: E501

        Timezone of team routing rule. If timezone field is not given, account timezone is used as default.  # noqa: E501

        :return: The timezone of this UpdateTeamRoutingRulePayload.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this UpdateTeamRoutingRulePayload.

        Timezone of team routing rule. If timezone field is not given, account timezone is used as default.  # noqa: E501

        :param timezone: The timezone of this UpdateTeamRoutingRulePayload.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

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
        if issubclass(UpdateTeamRoutingRulePayload, dict):
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
        if not isinstance(other, UpdateTeamRoutingRulePayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
