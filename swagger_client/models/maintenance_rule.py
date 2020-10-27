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


class MaintenanceRule(object):
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
        'state': 'str',
        'entity': 'MaintenanceEntity'
    }

    attribute_map = {
        'state': 'state',
        'entity': 'entity'
    }

    def __init__(self, state=None, entity=None):  # noqa: E501
        """MaintenanceRule - a model defined in Swagger"""  # noqa: E501

        self._state = None
        self._entity = None
        self.discriminator = None

        if state is not None:
            self.state = state
        self.entity = entity

    @property
    def state(self):
        """Gets the state of this MaintenanceRule.  # noqa: E501

        Defines the state of the rule  # noqa: E501

        :return: The state of this MaintenanceRule.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MaintenanceRule.

        Defines the state of the rule  # noqa: E501

        :param state: The state of this MaintenanceRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["enabled", "disabled"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def entity(self):
        """Gets the entity of this MaintenanceRule.  # noqa: E501


        :return: The entity of this MaintenanceRule.  # noqa: E501
        :rtype: MaintenanceEntity
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this MaintenanceRule.


        :param entity: The entity of this MaintenanceRule.  # noqa: E501
        :type: MaintenanceEntity
        """
        if entity is None:
            raise ValueError("Invalid value for `entity`, must not be `None`")  # noqa: E501

        self._entity = entity

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
        if issubclass(MaintenanceRule, dict):
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
        if not isinstance(other, MaintenanceRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other