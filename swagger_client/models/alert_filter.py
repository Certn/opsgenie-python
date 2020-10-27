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


class AlertFilter(object):
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
        'condition_match_type': 'str',
        'conditions': 'list[CallbackCondition]'
    }

    attribute_map = {
        'condition_match_type': 'conditionMatchType',
        'conditions': 'conditions'
    }

    def __init__(self, condition_match_type=None, conditions=None):  # noqa: E501
        """AlertFilter - a model defined in Swagger"""  # noqa: E501

        self._condition_match_type = None
        self._conditions = None
        self.discriminator = None

        if condition_match_type is not None:
            self.condition_match_type = condition_match_type
        if conditions is not None:
            self.conditions = conditions

    @property
    def condition_match_type(self):
        """Gets the condition_match_type of this AlertFilter.  # noqa: E501


        :return: The condition_match_type of this AlertFilter.  # noqa: E501
        :rtype: str
        """
        return self._condition_match_type

    @condition_match_type.setter
    def condition_match_type(self, condition_match_type):
        """Sets the condition_match_type of this AlertFilter.


        :param condition_match_type: The condition_match_type of this AlertFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["match-all", "match-any-condition", "match-all-conditions"]  # noqa: E501
        if condition_match_type not in allowed_values:
            raise ValueError(
                "Invalid value for `condition_match_type` ({0}), must be one of {1}"  # noqa: E501
                .format(condition_match_type, allowed_values)
            )

        self._condition_match_type = condition_match_type

    @property
    def conditions(self):
        """Gets the conditions of this AlertFilter.  # noqa: E501


        :return: The conditions of this AlertFilter.  # noqa: E501
        :rtype: list[CallbackCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this AlertFilter.


        :param conditions: The conditions of this AlertFilter.  # noqa: E501
        :type: list[CallbackCondition]
        """

        self._conditions = conditions

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
        if issubclass(AlertFilter, dict):
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
        if not isinstance(other, AlertFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
