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


class BaseResponseWithExpandable(object):
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
        'request_id': 'str',
        'took': 'float',
        'expandable': 'list[str]'
    }

    attribute_map = {
        'request_id': 'requestId',
        'took': 'took',
        'expandable': 'expandable'
    }

    def __init__(self, request_id=None, took=0.0, expandable=None):  # noqa: E501
        """BaseResponseWithExpandable - a model defined in Swagger"""  # noqa: E501

        self._request_id = None
        self._took = None
        self._expandable = None
        self.discriminator = None

        self.request_id = request_id
        self.took = took
        if expandable is not None:
            self.expandable = expandable

    @property
    def request_id(self):
        """Gets the request_id of this BaseResponseWithExpandable.  # noqa: E501


        :return: The request_id of this BaseResponseWithExpandable.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this BaseResponseWithExpandable.


        :param request_id: The request_id of this BaseResponseWithExpandable.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def took(self):
        """Gets the took of this BaseResponseWithExpandable.  # noqa: E501


        :return: The took of this BaseResponseWithExpandable.  # noqa: E501
        :rtype: float
        """
        return self._took

    @took.setter
    def took(self, took):
        """Sets the took of this BaseResponseWithExpandable.


        :param took: The took of this BaseResponseWithExpandable.  # noqa: E501
        :type: float
        """
        if took is None:
            raise ValueError("Invalid value for `took`, must not be `None`")  # noqa: E501

        self._took = took

    @property
    def expandable(self):
        """Gets the expandable of this BaseResponseWithExpandable.  # noqa: E501


        :return: The expandable of this BaseResponseWithExpandable.  # noqa: E501
        :rtype: list[str]
        """
        return self._expandable

    @expandable.setter
    def expandable(self, expandable):
        """Sets the expandable of this BaseResponseWithExpandable.


        :param expandable: The expandable of this BaseResponseWithExpandable.  # noqa: E501
        :type: list[str]
        """

        self._expandable = expandable

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
        if issubclass(BaseResponseWithExpandable, dict):
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
        if not isinstance(other, BaseResponseWithExpandable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
