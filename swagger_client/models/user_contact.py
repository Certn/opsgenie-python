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


class UserContact(object):
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
        'to': 'str',
        'id': 'str',
        'contact_method': 'str',
        'disabled_reason': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'to': 'to',
        'id': 'id',
        'contact_method': 'contactMethod',
        'disabled_reason': 'disabledReason',
        'enabled': 'enabled'
    }

    def __init__(self, to=None, id=None, contact_method=None, disabled_reason=None, enabled=None):  # noqa: E501
        """UserContact - a model defined in Swagger"""  # noqa: E501

        self._to = None
        self._id = None
        self._contact_method = None
        self._disabled_reason = None
        self._enabled = None
        self.discriminator = None

        if to is not None:
            self.to = to
        if id is not None:
            self.id = id
        if contact_method is not None:
            self.contact_method = contact_method
        if disabled_reason is not None:
            self.disabled_reason = disabled_reason
        if enabled is not None:
            self.enabled = enabled

    @property
    def to(self):
        """Gets the to of this UserContact.  # noqa: E501


        :return: The to of this UserContact.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this UserContact.


        :param to: The to of this UserContact.  # noqa: E501
        :type: str
        """

        self._to = to

    @property
    def id(self):
        """Gets the id of this UserContact.  # noqa: E501


        :return: The id of this UserContact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserContact.


        :param id: The id of this UserContact.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def contact_method(self):
        """Gets the contact_method of this UserContact.  # noqa: E501


        :return: The contact_method of this UserContact.  # noqa: E501
        :rtype: str
        """
        return self._contact_method

    @contact_method.setter
    def contact_method(self, contact_method):
        """Sets the contact_method of this UserContact.


        :param contact_method: The contact_method of this UserContact.  # noqa: E501
        :type: str
        """
        allowed_values = ["email", "sms", "voice", "mobile"]  # noqa: E501
        if contact_method not in allowed_values:
            raise ValueError(
                "Invalid value for `contact_method` ({0}), must be one of {1}"  # noqa: E501
                .format(contact_method, allowed_values)
            )

        self._contact_method = contact_method

    @property
    def disabled_reason(self):
        """Gets the disabled_reason of this UserContact.  # noqa: E501


        :return: The disabled_reason of this UserContact.  # noqa: E501
        :rtype: str
        """
        return self._disabled_reason

    @disabled_reason.setter
    def disabled_reason(self, disabled_reason):
        """Sets the disabled_reason of this UserContact.


        :param disabled_reason: The disabled_reason of this UserContact.  # noqa: E501
        :type: str
        """

        self._disabled_reason = disabled_reason

    @property
    def enabled(self):
        """Gets the enabled of this UserContact.  # noqa: E501


        :return: The enabled of this UserContact.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UserContact.


        :param enabled: The enabled of this UserContact.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if issubclass(UserContact, dict):
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
        if not isinstance(other, UserContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
