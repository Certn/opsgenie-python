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


class DeprecatedNotificationDeduplicationAlertPolicy(object):
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
        'deduplication_action_type': 'str',
        'count': 'int',
        'duration': 'Duration'
    }

    attribute_map = {
        'deduplication_action_type': 'deduplicationActionType',
        'count': 'count',
        'duration': 'duration'
    }

    def __init__(self, deduplication_action_type=None, count=None, duration=None):  # noqa: E501
        """DeprecatedNotificationDeduplicationAlertPolicy - a model defined in Swagger"""  # noqa: E501

        self._deduplication_action_type = None
        self._count = None
        self._duration = None
        self.discriminator = None

        if deduplication_action_type is not None:
            self.deduplication_action_type = deduplication_action_type
        if count is not None:
            self.count = count
        if duration is not None:
            self.duration = duration

    @property
    def deduplication_action_type(self):
        """Gets the deduplication_action_type of this DeprecatedNotificationDeduplicationAlertPolicy.  # noqa: E501

        Deduplication type  # noqa: E501

        :return: The deduplication_action_type of this DeprecatedNotificationDeduplicationAlertPolicy.  # noqa: E501
        :rtype: str
        """
        return self._deduplication_action_type

    @deduplication_action_type.setter
    def deduplication_action_type(self, deduplication_action_type):
        """Sets the deduplication_action_type of this DeprecatedNotificationDeduplicationAlertPolicy.

        Deduplication type  # noqa: E501

        :param deduplication_action_type: The deduplication_action_type of this DeprecatedNotificationDeduplicationAlertPolicy.  # noqa: E501
        :type: str
        """
        allowed_values = ["value-based", "frequency-based"]  # noqa: E501
        if deduplication_action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `deduplication_action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(deduplication_action_type, allowed_values)
            )

        self._deduplication_action_type = deduplication_action_type

    @property
    def count(self):
        """Gets the count of this DeprecatedNotificationDeduplicationAlertPolicy.  # noqa: E501

        Number of alerts before deduplication  # noqa: E501

        :return: The count of this DeprecatedNotificationDeduplicationAlertPolicy.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this DeprecatedNotificationDeduplicationAlertPolicy.

        Number of alerts before deduplication  # noqa: E501

        :param count: The count of this DeprecatedNotificationDeduplicationAlertPolicy.  # noqa: E501
        :type: int
        """
        if count is not None and count > 100:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value less than or equal to `100`")  # noqa: E501
        if count is not None and count < 2:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `2`")  # noqa: E501

        self._count = count

    @property
    def duration(self):
        """Gets the duration of this DeprecatedNotificationDeduplicationAlertPolicy.  # noqa: E501

        Interval to keep count of alerts for frequency based deduplication  # noqa: E501

        :return: The duration of this DeprecatedNotificationDeduplicationAlertPolicy.  # noqa: E501
        :rtype: Duration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DeprecatedNotificationDeduplicationAlertPolicy.

        Interval to keep count of alerts for frequency based deduplication  # noqa: E501

        :param duration: The duration of this DeprecatedNotificationDeduplicationAlertPolicy.  # noqa: E501
        :type: Duration
        """

        self._duration = duration

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
        if issubclass(DeprecatedNotificationDeduplicationAlertPolicy, dict):
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
        if not isinstance(other, DeprecatedNotificationDeduplicationAlertPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
