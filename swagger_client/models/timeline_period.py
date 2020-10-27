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


class TimelinePeriod(object):
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
        'start_date': 'datetime',
        'end_date': 'datetime',
        'type': 'str',
        'from_user': 'str',
        'recipient': 'TimelineRecipient',
        'flattened_recipients': 'list[TimelineRecipient]'
    }

    attribute_map = {
        'start_date': 'startDate',
        'end_date': 'endDate',
        'type': 'type',
        'from_user': 'fromUser',
        'recipient': 'recipient',
        'flattened_recipients': 'flattenedRecipients'
    }

    def __init__(self, start_date=None, end_date=None, type=None, from_user=None, recipient=None, flattened_recipients=None):  # noqa: E501
        """TimelinePeriod - a model defined in Swagger"""  # noqa: E501

        self._start_date = None
        self._end_date = None
        self._type = None
        self._from_user = None
        self._recipient = None
        self._flattened_recipients = None
        self.discriminator = None

        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if type is not None:
            self.type = type
        if from_user is not None:
            self.from_user = from_user
        if recipient is not None:
            self.recipient = recipient
        if flattened_recipients is not None:
            self.flattened_recipients = flattened_recipients

    @property
    def start_date(self):
        """Gets the start_date of this TimelinePeriod.  # noqa: E501


        :return: The start_date of this TimelinePeriod.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TimelinePeriod.


        :param start_date: The start_date of this TimelinePeriod.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this TimelinePeriod.  # noqa: E501


        :return: The end_date of this TimelinePeriod.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TimelinePeriod.


        :param end_date: The end_date of this TimelinePeriod.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def type(self):
        """Gets the type of this TimelinePeriod.  # noqa: E501


        :return: The type of this TimelinePeriod.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TimelinePeriod.


        :param type: The type of this TimelinePeriod.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def from_user(self):
        """Gets the from_user of this TimelinePeriod.  # noqa: E501

        Only used by 'forwarding' period types  # noqa: E501

        :return: The from_user of this TimelinePeriod.  # noqa: E501
        :rtype: str
        """
        return self._from_user

    @from_user.setter
    def from_user(self, from_user):
        """Sets the from_user of this TimelinePeriod.

        Only used by 'forwarding' period types  # noqa: E501

        :param from_user: The from_user of this TimelinePeriod.  # noqa: E501
        :type: str
        """

        self._from_user = from_user

    @property
    def recipient(self):
        """Gets the recipient of this TimelinePeriod.  # noqa: E501


        :return: The recipient of this TimelinePeriod.  # noqa: E501
        :rtype: TimelineRecipient
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this TimelinePeriod.


        :param recipient: The recipient of this TimelinePeriod.  # noqa: E501
        :type: TimelineRecipient
        """

        self._recipient = recipient

    @property
    def flattened_recipients(self):
        """Gets the flattened_recipients of this TimelinePeriod.  # noqa: E501

        Only used by 'historical' period types  # noqa: E501

        :return: The flattened_recipients of this TimelinePeriod.  # noqa: E501
        :rtype: list[TimelineRecipient]
        """
        return self._flattened_recipients

    @flattened_recipients.setter
    def flattened_recipients(self, flattened_recipients):
        """Sets the flattened_recipients of this TimelinePeriod.

        Only used by 'historical' period types  # noqa: E501

        :param flattened_recipients: The flattened_recipients of this TimelinePeriod.  # noqa: E501
        :type: list[TimelineRecipient]
        """

        self._flattened_recipients = flattened_recipients

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
        if issubclass(TimelinePeriod, dict):
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
        if not isinstance(other, TimelinePeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other