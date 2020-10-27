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


class CreateNotificationRulePayload(object):
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
        'action_type': 'NotificationActionType',
        'criteria': 'Filter',
        'notification_time': 'list[NotifyTime]',
        'time_restriction': 'TimeRestrictionInterval',
        'schedules': 'list[ScheduleRecipient]',
        'order': 'int',
        'steps': 'list[CreateNotificationRuleStepPayload]',
        'repeat': 'NotificationRepeat',
        'enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'action_type': 'actionType',
        'criteria': 'criteria',
        'notification_time': 'notificationTime',
        'time_restriction': 'timeRestriction',
        'schedules': 'schedules',
        'order': 'order',
        'steps': 'steps',
        'repeat': 'repeat',
        'enabled': 'enabled'
    }

    def __init__(self, name=None, action_type=None, criteria=None, notification_time=None, time_restriction=None, schedules=None, order=None, steps=None, repeat=None, enabled=None):  # noqa: E501
        """CreateNotificationRulePayload - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._action_type = None
        self._criteria = None
        self._notification_time = None
        self._time_restriction = None
        self._schedules = None
        self._order = None
        self._steps = None
        self._repeat = None
        self._enabled = None
        self.discriminator = None

        self.name = name
        self.action_type = action_type
        if criteria is not None:
            self.criteria = criteria
        if notification_time is not None:
            self.notification_time = notification_time
        if time_restriction is not None:
            self.time_restriction = time_restriction
        if schedules is not None:
            self.schedules = schedules
        if order is not None:
            self.order = order
        if steps is not None:
            self.steps = steps
        if repeat is not None:
            self.repeat = repeat
        self.enabled = enabled

    @property
    def name(self):
        """Gets the name of this CreateNotificationRulePayload.  # noqa: E501

        Name of the notification rule  # noqa: E501

        :return: The name of this CreateNotificationRulePayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateNotificationRulePayload.

        Name of the notification rule  # noqa: E501

        :param name: The name of this CreateNotificationRulePayload.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def action_type(self):
        """Gets the action_type of this CreateNotificationRulePayload.  # noqa: E501


        :return: The action_type of this CreateNotificationRulePayload.  # noqa: E501
        :rtype: NotificationActionType
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this CreateNotificationRulePayload.


        :param action_type: The action_type of this CreateNotificationRulePayload.  # noqa: E501
        :type: NotificationActionType
        """
        if action_type is None:
            raise ValueError("Invalid value for `action_type`, must not be `None`")  # noqa: E501

        self._action_type = action_type

    @property
    def criteria(self):
        """Gets the criteria of this CreateNotificationRulePayload.  # noqa: E501


        :return: The criteria of this CreateNotificationRulePayload.  # noqa: E501
        :rtype: Filter
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        """Sets the criteria of this CreateNotificationRulePayload.


        :param criteria: The criteria of this CreateNotificationRulePayload.  # noqa: E501
        :type: Filter
        """

        self._criteria = criteria

    @property
    def notification_time(self):
        """Gets the notification_time of this CreateNotificationRulePayload.  # noqa: E501

        List of Time Periods that notification for schedule start/end will be sent  # noqa: E501

        :return: The notification_time of this CreateNotificationRulePayload.  # noqa: E501
        :rtype: list[NotifyTime]
        """
        return self._notification_time

    @notification_time.setter
    def notification_time(self, notification_time):
        """Sets the notification_time of this CreateNotificationRulePayload.

        List of Time Periods that notification for schedule start/end will be sent  # noqa: E501

        :param notification_time: The notification_time of this CreateNotificationRulePayload.  # noqa: E501
        :type: list[NotifyTime]
        """

        self._notification_time = notification_time

    @property
    def time_restriction(self):
        """Gets the time_restriction of this CreateNotificationRulePayload.  # noqa: E501

        Time interval that notification rule will work  # noqa: E501

        :return: The time_restriction of this CreateNotificationRulePayload.  # noqa: E501
        :rtype: TimeRestrictionInterval
        """
        return self._time_restriction

    @time_restriction.setter
    def time_restriction(self, time_restriction):
        """Sets the time_restriction of this CreateNotificationRulePayload.

        Time interval that notification rule will work  # noqa: E501

        :param time_restriction: The time_restriction of this CreateNotificationRulePayload.  # noqa: E501
        :type: TimeRestrictionInterval
        """

        self._time_restriction = time_restriction

    @property
    def schedules(self):
        """Gets the schedules of this CreateNotificationRulePayload.  # noqa: E501

        List of schedules that notification rule will be applied when on call of that schedule starts/ends. This field is valid for Schedule Start/End rules  # noqa: E501

        :return: The schedules of this CreateNotificationRulePayload.  # noqa: E501
        :rtype: list[ScheduleRecipient]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this CreateNotificationRulePayload.

        List of schedules that notification rule will be applied when on call of that schedule starts/ends. This field is valid for Schedule Start/End rules  # noqa: E501

        :param schedules: The schedules of this CreateNotificationRulePayload.  # noqa: E501
        :type: list[ScheduleRecipient]
        """

        self._schedules = schedules

    @property
    def order(self):
        """Gets the order of this CreateNotificationRulePayload.  # noqa: E501

        The order of the notification rule within the notification rules with the same action type  # noqa: E501

        :return: The order of this CreateNotificationRulePayload.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this CreateNotificationRulePayload.

        The order of the notification rule within the notification rules with the same action type  # noqa: E501

        :param order: The order of this CreateNotificationRulePayload.  # noqa: E501
        :type: int
        """
        if order is not None and order < 0:  # noqa: E501
            raise ValueError("Invalid value for `order`, must be a value greater than or equal to `0`")  # noqa: E501

        self._order = order

    @property
    def steps(self):
        """Gets the steps of this CreateNotificationRulePayload.  # noqa: E501

        List of steps that will be added to notification rule  # noqa: E501

        :return: The steps of this CreateNotificationRulePayload.  # noqa: E501
        :rtype: list[CreateNotificationRuleStepPayload]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this CreateNotificationRulePayload.

        List of steps that will be added to notification rule  # noqa: E501

        :param steps: The steps of this CreateNotificationRulePayload.  # noqa: E501
        :type: list[CreateNotificationRuleStepPayload]
        """

        self._steps = steps

    @property
    def repeat(self):
        """Gets the repeat of this CreateNotificationRulePayload.  # noqa: E501


        :return: The repeat of this CreateNotificationRulePayload.  # noqa: E501
        :rtype: NotificationRepeat
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat):
        """Sets the repeat of this CreateNotificationRulePayload.


        :param repeat: The repeat of this CreateNotificationRulePayload.  # noqa: E501
        :type: NotificationRepeat
        """

        self._repeat = repeat

    @property
    def enabled(self):
        """Gets the enabled of this CreateNotificationRulePayload.  # noqa: E501

        Defines if notification rule will be enabled or not when it is created  # noqa: E501

        :return: The enabled of this CreateNotificationRulePayload.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CreateNotificationRulePayload.

        Defines if notification rule will be enabled or not when it is created  # noqa: E501

        :param enabled: The enabled of this CreateNotificationRulePayload.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

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
        if issubclass(CreateNotificationRulePayload, dict):
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
        if not isinstance(other, CreateNotificationRulePayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
