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


class SolarwindsCallback(object):
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
        'send_via_marid': 'bool',
        'send_via_oec': 'bool'
    }

    attribute_map = {
        'send_via_marid': 'sendViaMarid',
        'send_via_oec': 'sendViaOEC'
    }

    def __init__(self, send_via_marid=None, send_via_oec=None):  # noqa: E501
        """SolarwindsCallback - a model defined in Swagger"""  # noqa: E501

        self._send_via_marid = None
        self._send_via_oec = None
        self.discriminator = None

        if send_via_marid is not None:
            self.send_via_marid = send_via_marid
        if send_via_oec is not None:
            self.send_via_oec = send_via_oec

    @property
    def send_via_marid(self):
        """Gets the send_via_marid of this SolarwindsCallback.  # noqa: E501


        :return: The send_via_marid of this SolarwindsCallback.  # noqa: E501
        :rtype: bool
        """
        return self._send_via_marid

    @send_via_marid.setter
    def send_via_marid(self, send_via_marid):
        """Sets the send_via_marid of this SolarwindsCallback.


        :param send_via_marid: The send_via_marid of this SolarwindsCallback.  # noqa: E501
        :type: bool
        """

        self._send_via_marid = send_via_marid

    @property
    def send_via_oec(self):
        """Gets the send_via_oec of this SolarwindsCallback.  # noqa: E501


        :return: The send_via_oec of this SolarwindsCallback.  # noqa: E501
        :rtype: bool
        """
        return self._send_via_oec

    @send_via_oec.setter
    def send_via_oec(self, send_via_oec):
        """Sets the send_via_oec of this SolarwindsCallback.


        :param send_via_oec: The send_via_oec of this SolarwindsCallback.  # noqa: E501
        :type: bool
        """

        self._send_via_oec = send_via_oec

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
        if issubclass(SolarwindsCallback, dict):
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
        if not isinstance(other, SolarwindsCallback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
