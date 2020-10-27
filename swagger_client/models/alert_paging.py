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


class AlertPaging(object):
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
        'first': 'str',
        'next': 'str'
    }

    attribute_map = {
        'first': 'first',
        'next': 'next'
    }

    def __init__(self, first=None, next=None):  # noqa: E501
        """AlertPaging - a model defined in Swagger"""  # noqa: E501

        self._first = None
        self._next = None
        self.discriminator = None

        if first is not None:
            self.first = first
        if next is not None:
            self.next = next

    @property
    def first(self):
        """Gets the first of this AlertPaging.  # noqa: E501


        :return: The first of this AlertPaging.  # noqa: E501
        :rtype: str
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this AlertPaging.


        :param first: The first of this AlertPaging.  # noqa: E501
        :type: str
        """

        self._first = first

    @property
    def next(self):
        """Gets the next of this AlertPaging.  # noqa: E501


        :return: The next of this AlertPaging.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this AlertPaging.


        :param next: The next of this AlertPaging.  # noqa: E501
        :type: str
        """

        self._next = next

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
        if issubclass(AlertPaging, dict):
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
        if not isinstance(other, AlertPaging):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
