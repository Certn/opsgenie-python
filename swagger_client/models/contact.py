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


class Contact(object):
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
        'id': 'str',
        'method': 'str',
        'to': 'str',
        'status': 'ContactStatus'
    }

    attribute_map = {
        'id': 'id',
        'method': 'method',
        'to': 'to',
        'status': 'status'
    }

    def __init__(self, id=None, method=None, to=None, status=None):  # noqa: E501
        """Contact - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._method = None
        self._to = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if method is not None:
            self.method = method
        if to is not None:
            self.to = to
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this Contact.  # noqa: E501


        :return: The id of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Contact.


        :param id: The id of this Contact.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def method(self):
        """Gets the method of this Contact.  # noqa: E501


        :return: The method of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Contact.


        :param method: The method of this Contact.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def to(self):
        """Gets the to of this Contact.  # noqa: E501


        :return: The to of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Contact.


        :param to: The to of this Contact.  # noqa: E501
        :type: str
        """

        self._to = to

    @property
    def status(self):
        """Gets the status of this Contact.  # noqa: E501


        :return: The status of this Contact.  # noqa: E501
        :rtype: ContactStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Contact.


        :param status: The status of this Contact.  # noqa: E501
        :type: ContactStatus
        """

        self._status = status

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
        if issubclass(Contact, dict):
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
        if not isinstance(other, Contact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
