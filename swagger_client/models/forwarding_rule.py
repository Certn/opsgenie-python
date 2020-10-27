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


class ForwardingRule(object):
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
        'from_user': 'UserMeta',
        'to_user': 'UserMeta',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'alias': 'str',
        'id': 'str'
    }

    attribute_map = {
        'from_user': 'fromUser',
        'to_user': 'toUser',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'alias': 'alias',
        'id': 'id'
    }

    def __init__(self, from_user=None, to_user=None, start_date=None, end_date=None, alias=None, id=None):  # noqa: E501
        """ForwardingRule - a model defined in Swagger"""  # noqa: E501

        self._from_user = None
        self._to_user = None
        self._start_date = None
        self._end_date = None
        self._alias = None
        self._id = None
        self.discriminator = None

        if from_user is not None:
            self.from_user = from_user
        if to_user is not None:
            self.to_user = to_user
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if alias is not None:
            self.alias = alias
        if id is not None:
            self.id = id

    @property
    def from_user(self):
        """Gets the from_user of this ForwardingRule.  # noqa: E501


        :return: The from_user of this ForwardingRule.  # noqa: E501
        :rtype: UserMeta
        """
        return self._from_user

    @from_user.setter
    def from_user(self, from_user):
        """Sets the from_user of this ForwardingRule.


        :param from_user: The from_user of this ForwardingRule.  # noqa: E501
        :type: UserMeta
        """

        self._from_user = from_user

    @property
    def to_user(self):
        """Gets the to_user of this ForwardingRule.  # noqa: E501


        :return: The to_user of this ForwardingRule.  # noqa: E501
        :rtype: UserMeta
        """
        return self._to_user

    @to_user.setter
    def to_user(self, to_user):
        """Sets the to_user of this ForwardingRule.


        :param to_user: The to_user of this ForwardingRule.  # noqa: E501
        :type: UserMeta
        """

        self._to_user = to_user

    @property
    def start_date(self):
        """Gets the start_date of this ForwardingRule.  # noqa: E501


        :return: The start_date of this ForwardingRule.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ForwardingRule.


        :param start_date: The start_date of this ForwardingRule.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ForwardingRule.  # noqa: E501


        :return: The end_date of this ForwardingRule.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ForwardingRule.


        :param end_date: The end_date of this ForwardingRule.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def alias(self):
        """Gets the alias of this ForwardingRule.  # noqa: E501


        :return: The alias of this ForwardingRule.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ForwardingRule.


        :param alias: The alias of this ForwardingRule.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def id(self):
        """Gets the id of this ForwardingRule.  # noqa: E501


        :return: The id of this ForwardingRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ForwardingRule.


        :param id: The id of this ForwardingRule.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(ForwardingRule, dict):
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
        if not isinstance(other, ForwardingRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
