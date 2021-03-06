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


class WeekdayTimeRestriction(object):
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
        'start_day': 'str',
        'start_hour': 'int',
        'start_min': 'int',
        'end_day': 'str',
        'end_hour': 'int',
        'end_min': 'int'
    }

    attribute_map = {
        'start_day': 'startDay',
        'start_hour': 'startHour',
        'start_min': 'startMin',
        'end_day': 'endDay',
        'end_hour': 'endHour',
        'end_min': 'endMin'
    }

    def __init__(self, start_day=None, start_hour=None, start_min=None, end_day=None, end_hour=None, end_min=None):  # noqa: E501
        """WeekdayTimeRestriction - a model defined in Swagger"""  # noqa: E501

        self._start_day = None
        self._start_hour = None
        self._start_min = None
        self._end_day = None
        self._end_hour = None
        self._end_min = None
        self.discriminator = None

        if start_day is not None:
            self.start_day = start_day
        if start_hour is not None:
            self.start_hour = start_hour
        if start_min is not None:
            self.start_min = start_min
        if end_day is not None:
            self.end_day = end_day
        if end_hour is not None:
            self.end_hour = end_hour
        if end_min is not None:
            self.end_min = end_min

    @property
    def start_day(self):
        """Gets the start_day of this WeekdayTimeRestriction.  # noqa: E501


        :return: The start_day of this WeekdayTimeRestriction.  # noqa: E501
        :rtype: str
        """
        return self._start_day

    @start_day.setter
    def start_day(self, start_day):
        """Sets the start_day of this WeekdayTimeRestriction.


        :param start_day: The start_day of this WeekdayTimeRestriction.  # noqa: E501
        :type: str
        """
        allowed_values = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]  # noqa: E501
        if start_day not in allowed_values:
            raise ValueError(
                "Invalid value for `start_day` ({0}), must be one of {1}"  # noqa: E501
                .format(start_day, allowed_values)
            )

        self._start_day = start_day

    @property
    def start_hour(self):
        """Gets the start_hour of this WeekdayTimeRestriction.  # noqa: E501


        :return: The start_hour of this WeekdayTimeRestriction.  # noqa: E501
        :rtype: int
        """
        return self._start_hour

    @start_hour.setter
    def start_hour(self, start_hour):
        """Sets the start_hour of this WeekdayTimeRestriction.


        :param start_hour: The start_hour of this WeekdayTimeRestriction.  # noqa: E501
        :type: int
        """

        self._start_hour = start_hour

    @property
    def start_min(self):
        """Gets the start_min of this WeekdayTimeRestriction.  # noqa: E501


        :return: The start_min of this WeekdayTimeRestriction.  # noqa: E501
        :rtype: int
        """
        return self._start_min

    @start_min.setter
    def start_min(self, start_min):
        """Sets the start_min of this WeekdayTimeRestriction.


        :param start_min: The start_min of this WeekdayTimeRestriction.  # noqa: E501
        :type: int
        """

        self._start_min = start_min

    @property
    def end_day(self):
        """Gets the end_day of this WeekdayTimeRestriction.  # noqa: E501


        :return: The end_day of this WeekdayTimeRestriction.  # noqa: E501
        :rtype: str
        """
        return self._end_day

    @end_day.setter
    def end_day(self, end_day):
        """Sets the end_day of this WeekdayTimeRestriction.


        :param end_day: The end_day of this WeekdayTimeRestriction.  # noqa: E501
        :type: str
        """
        allowed_values = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]  # noqa: E501
        if end_day not in allowed_values:
            raise ValueError(
                "Invalid value for `end_day` ({0}), must be one of {1}"  # noqa: E501
                .format(end_day, allowed_values)
            )

        self._end_day = end_day

    @property
    def end_hour(self):
        """Gets the end_hour of this WeekdayTimeRestriction.  # noqa: E501


        :return: The end_hour of this WeekdayTimeRestriction.  # noqa: E501
        :rtype: int
        """
        return self._end_hour

    @end_hour.setter
    def end_hour(self, end_hour):
        """Sets the end_hour of this WeekdayTimeRestriction.


        :param end_hour: The end_hour of this WeekdayTimeRestriction.  # noqa: E501
        :type: int
        """

        self._end_hour = end_hour

    @property
    def end_min(self):
        """Gets the end_min of this WeekdayTimeRestriction.  # noqa: E501


        :return: The end_min of this WeekdayTimeRestriction.  # noqa: E501
        :rtype: int
        """
        return self._end_min

    @end_min.setter
    def end_min(self, end_min):
        """Sets the end_min of this WeekdayTimeRestriction.


        :param end_min: The end_min of this WeekdayTimeRestriction.  # noqa: E501
        :type: int
        """

        self._end_min = end_min

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
        if issubclass(WeekdayTimeRestriction, dict):
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
        if not isinstance(other, WeekdayTimeRestriction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
