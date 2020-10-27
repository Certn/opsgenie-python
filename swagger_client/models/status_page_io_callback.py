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


class StatusPageIOCallback(object):
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
        'status_page_page_id': 'str',
        'status_page_api_key': 'str'
    }

    attribute_map = {
        'status_page_page_id': 'statusPagePageId',
        'status_page_api_key': 'statusPageApiKey'
    }

    def __init__(self, status_page_page_id=None, status_page_api_key=None):  # noqa: E501
        """StatusPageIOCallback - a model defined in Swagger"""  # noqa: E501

        self._status_page_page_id = None
        self._status_page_api_key = None
        self.discriminator = None

        if status_page_page_id is not None:
            self.status_page_page_id = status_page_page_id
        if status_page_api_key is not None:
            self.status_page_api_key = status_page_api_key

    @property
    def status_page_page_id(self):
        """Gets the status_page_page_id of this StatusPageIOCallback.  # noqa: E501


        :return: The status_page_page_id of this StatusPageIOCallback.  # noqa: E501
        :rtype: str
        """
        return self._status_page_page_id

    @status_page_page_id.setter
    def status_page_page_id(self, status_page_page_id):
        """Sets the status_page_page_id of this StatusPageIOCallback.


        :param status_page_page_id: The status_page_page_id of this StatusPageIOCallback.  # noqa: E501
        :type: str
        """

        self._status_page_page_id = status_page_page_id

    @property
    def status_page_api_key(self):
        """Gets the status_page_api_key of this StatusPageIOCallback.  # noqa: E501


        :return: The status_page_api_key of this StatusPageIOCallback.  # noqa: E501
        :rtype: str
        """
        return self._status_page_api_key

    @status_page_api_key.setter
    def status_page_api_key(self, status_page_api_key):
        """Sets the status_page_api_key of this StatusPageIOCallback.


        :param status_page_api_key: The status_page_api_key of this StatusPageIOCallback.  # noqa: E501
        :type: str
        """

        self._status_page_api_key = status_page_api_key

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
        if issubclass(StatusPageIOCallback, dict):
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
        if not isinstance(other, StatusPageIOCallback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
