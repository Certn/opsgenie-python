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


class TeamLog(object):
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
        'offset': 'str',
        'logs': 'list[TeamLogDetails]'
    }

    attribute_map = {
        'offset': 'offset',
        'logs': 'logs'
    }

    def __init__(self, offset=None, logs=None):  # noqa: E501
        """TeamLog - a model defined in Swagger"""  # noqa: E501

        self._offset = None
        self._logs = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if logs is not None:
            self.logs = logs

    @property
    def offset(self):
        """Gets the offset of this TeamLog.  # noqa: E501


        :return: The offset of this TeamLog.  # noqa: E501
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TeamLog.


        :param offset: The offset of this TeamLog.  # noqa: E501
        :type: str
        """

        self._offset = offset

    @property
    def logs(self):
        """Gets the logs of this TeamLog.  # noqa: E501


        :return: The logs of this TeamLog.  # noqa: E501
        :rtype: list[TeamLogDetails]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this TeamLog.


        :param logs: The logs of this TeamLog.  # noqa: E501
        :type: list[TeamLogDetails]
        """

        self._logs = logs

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
        if issubclass(TeamLog, dict):
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
        if not isinstance(other, TeamLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other