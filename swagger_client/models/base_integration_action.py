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


class BaseIntegrationAction(object):
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
        'name': 'str',
        'order': 'int',
        'filter': 'IntegrationActionFilter',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'order': 'order',
        'filter': 'filter',
        'type': 'type'
    }

    discriminator_value_class_map = {
        'CommonIntegrationAction': 'CommonIntegrationAction',
        'ignore': 'IgnoreIntegrationAction',
        'addNote': 'AddNoteIntegrationAction',
        'close': 'CloseIntegrationAction',
        'acknowledge': 'AckIntegrationAction',
        'create': 'CreateIntegrationAction'
    }

    def __init__(self, name=None, order=None, filter=None, type=None):  # noqa: E501
        """BaseIntegrationAction - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._order = None
        self._filter = None
        self._type = None
        self.discriminator = 'type'

        self.name = name
        if order is not None:
            self.order = order
        self.filter = filter
        self.type = type

    @property
    def name(self):
        """Gets the name of this BaseIntegrationAction.  # noqa: E501


        :return: The name of this BaseIntegrationAction.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BaseIntegrationAction.


        :param name: The name of this BaseIntegrationAction.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def order(self):
        """Gets the order of this BaseIntegrationAction.  # noqa: E501


        :return: The order of this BaseIntegrationAction.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this BaseIntegrationAction.


        :param order: The order of this BaseIntegrationAction.  # noqa: E501
        :type: int
        """
        if order is not None and order < 0:  # noqa: E501
            raise ValueError("Invalid value for `order`, must be a value greater than or equal to `0`")  # noqa: E501

        self._order = order

    @property
    def filter(self):
        """Gets the filter of this BaseIntegrationAction.  # noqa: E501


        :return: The filter of this BaseIntegrationAction.  # noqa: E501
        :rtype: IntegrationActionFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this BaseIntegrationAction.


        :param filter: The filter of this BaseIntegrationAction.  # noqa: E501
        :type: IntegrationActionFilter
        """
        if filter is None:
            raise ValueError("Invalid value for `filter`, must not be `None`")  # noqa: E501

        self._filter = filter

    @property
    def type(self):
        """Gets the type of this BaseIntegrationAction.  # noqa: E501


        :return: The type of this BaseIntegrationAction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BaseIntegrationAction.


        :param type: The type of this BaseIntegrationAction.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["acknowledge", "addNote", "close", "create", "ignore"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(BaseIntegrationAction, dict):
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
        if not isinstance(other, BaseIntegrationAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other