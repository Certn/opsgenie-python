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


class NotificationRuleMeta(object):
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
        'name': 'str',
        'action_type': 'NotificationActionType',
        'order': 'int',
        'enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'action_type': 'actionType',
        'order': 'order',
        'enabled': 'enabled'
    }

    def __init__(self, id=None, name=None, action_type=None, order=None, enabled=None):  # noqa: E501
        """NotificationRuleMeta - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._action_type = None
        self._order = None
        self._enabled = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if action_type is not None:
            self.action_type = action_type
        if order is not None:
            self.order = order
        if enabled is not None:
            self.enabled = enabled

    @property
    def id(self):
        """Gets the id of this NotificationRuleMeta.  # noqa: E501


        :return: The id of this NotificationRuleMeta.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationRuleMeta.


        :param id: The id of this NotificationRuleMeta.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NotificationRuleMeta.  # noqa: E501


        :return: The name of this NotificationRuleMeta.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NotificationRuleMeta.


        :param name: The name of this NotificationRuleMeta.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def action_type(self):
        """Gets the action_type of this NotificationRuleMeta.  # noqa: E501


        :return: The action_type of this NotificationRuleMeta.  # noqa: E501
        :rtype: NotificationActionType
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this NotificationRuleMeta.


        :param action_type: The action_type of this NotificationRuleMeta.  # noqa: E501
        :type: NotificationActionType
        """

        self._action_type = action_type

    @property
    def order(self):
        """Gets the order of this NotificationRuleMeta.  # noqa: E501


        :return: The order of this NotificationRuleMeta.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this NotificationRuleMeta.


        :param order: The order of this NotificationRuleMeta.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def enabled(self):
        """Gets the enabled of this NotificationRuleMeta.  # noqa: E501


        :return: The enabled of this NotificationRuleMeta.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NotificationRuleMeta.


        :param enabled: The enabled of this NotificationRuleMeta.  # noqa: E501
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
        if issubclass(NotificationRuleMeta, dict):
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
        if not isinstance(other, NotificationRuleMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other