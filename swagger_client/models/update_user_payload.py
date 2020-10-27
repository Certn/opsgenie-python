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


class UpdateUserPayload(object):
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
        'username': 'str',
        'full_name': 'str',
        'role': 'UserRole',
        'skype_username': 'str',
        'time_zone': 'str',
        'locale': 'str',
        'user_address': 'UserAddress',
        'tags': 'list[str]',
        'details': 'dict(str, list[str])',
        'invitation_disabled': 'bool'
    }

    attribute_map = {
        'username': 'username',
        'full_name': 'fullName',
        'role': 'role',
        'skype_username': 'skypeUsername',
        'time_zone': 'timeZone',
        'locale': 'locale',
        'user_address': 'userAddress',
        'tags': 'tags',
        'details': 'details',
        'invitation_disabled': 'invitationDisabled'
    }

    def __init__(self, username=None, full_name=None, role=None, skype_username=None, time_zone=None, locale=None, user_address=None, tags=None, details=None, invitation_disabled=None):  # noqa: E501
        """UpdateUserPayload - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._full_name = None
        self._role = None
        self._skype_username = None
        self._time_zone = None
        self._locale = None
        self._user_address = None
        self._tags = None
        self._details = None
        self._invitation_disabled = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if full_name is not None:
            self.full_name = full_name
        if role is not None:
            self.role = role
        if skype_username is not None:
            self.skype_username = skype_username
        if time_zone is not None:
            self.time_zone = time_zone
        if locale is not None:
            self.locale = locale
        if user_address is not None:
            self.user_address = user_address
        if tags is not None:
            self.tags = tags
        if details is not None:
            self.details = details
        if invitation_disabled is not None:
            self.invitation_disabled = invitation_disabled

    @property
    def username(self):
        """Gets the username of this UpdateUserPayload.  # noqa: E501

        E-mail address of the user  # noqa: E501

        :return: The username of this UpdateUserPayload.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UpdateUserPayload.

        E-mail address of the user  # noqa: E501

        :param username: The username of this UpdateUserPayload.  # noqa: E501
        :type: str
        """
        if username is not None and len(username) > 100:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `100`")  # noqa: E501

        self._username = username

    @property
    def full_name(self):
        """Gets the full_name of this UpdateUserPayload.  # noqa: E501

        Name of the user  # noqa: E501

        :return: The full_name of this UpdateUserPayload.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this UpdateUserPayload.

        Name of the user  # noqa: E501

        :param full_name: The full_name of this UpdateUserPayload.  # noqa: E501
        :type: str
        """
        if full_name is not None and len(full_name) > 512:
            raise ValueError("Invalid value for `full_name`, length must be less than or equal to `512`")  # noqa: E501

        self._full_name = full_name

    @property
    def role(self):
        """Gets the role of this UpdateUserPayload.  # noqa: E501

        Role of user. It may be one of owner, admin, user or the name of a custom role you've created.  # noqa: E501

        :return: The role of this UpdateUserPayload.  # noqa: E501
        :rtype: UserRole
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UpdateUserPayload.

        Role of user. It may be one of owner, admin, user or the name of a custom role you've created.  # noqa: E501

        :param role: The role of this UpdateUserPayload.  # noqa: E501
        :type: UserRole
        """

        self._role = role

    @property
    def skype_username(self):
        """Gets the skype_username of this UpdateUserPayload.  # noqa: E501

        Skype username of the user  # noqa: E501

        :return: The skype_username of this UpdateUserPayload.  # noqa: E501
        :rtype: str
        """
        return self._skype_username

    @skype_username.setter
    def skype_username(self, skype_username):
        """Sets the skype_username of this UpdateUserPayload.

        Skype username of the user  # noqa: E501

        :param skype_username: The skype_username of this UpdateUserPayload.  # noqa: E501
        :type: str
        """

        self._skype_username = skype_username

    @property
    def time_zone(self):
        """Gets the time_zone of this UpdateUserPayload.  # noqa: E501

        Timezone of the user. If not set, timezone of the customer will be used instead.  # noqa: E501

        :return: The time_zone of this UpdateUserPayload.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this UpdateUserPayload.

        Timezone of the user. If not set, timezone of the customer will be used instead.  # noqa: E501

        :param time_zone: The time_zone of this UpdateUserPayload.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def locale(self):
        """Gets the locale of this UpdateUserPayload.  # noqa: E501

        Location information of the user. If not set, locale of the customer will be used instead.  # noqa: E501

        :return: The locale of this UpdateUserPayload.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this UpdateUserPayload.

        Location information of the user. If not set, locale of the customer will be used instead.  # noqa: E501

        :param locale: The locale of this UpdateUserPayload.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def user_address(self):
        """Gets the user_address of this UpdateUserPayload.  # noqa: E501

        Address of the user  # noqa: E501

        :return: The user_address of this UpdateUserPayload.  # noqa: E501
        :rtype: UserAddress
        """
        return self._user_address

    @user_address.setter
    def user_address(self, user_address):
        """Sets the user_address of this UpdateUserPayload.

        Address of the user  # noqa: E501

        :param user_address: The user_address of this UpdateUserPayload.  # noqa: E501
        :type: UserAddress
        """

        self._user_address = user_address

    @property
    def tags(self):
        """Gets the tags of this UpdateUserPayload.  # noqa: E501

        List of labels attached to the user. You can label users to differentiate them from the rest. For example, you can add ITManager tag to differentiate people with this role from others.  # noqa: E501

        :return: The tags of this UpdateUserPayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateUserPayload.

        List of labels attached to the user. You can label users to differentiate them from the rest. For example, you can add ITManager tag to differentiate people with this role from others.  # noqa: E501

        :param tags: The tags of this UpdateUserPayload.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def details(self):
        """Gets the details of this UpdateUserPayload.  # noqa: E501

        Set of user defined properties.  # noqa: E501

        :return: The details of this UpdateUserPayload.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this UpdateUserPayload.

        Set of user defined properties.  # noqa: E501

        :param details: The details of this UpdateUserPayload.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._details = details

    @property
    def invitation_disabled(self):
        """Gets the invitation_disabled of this UpdateUserPayload.  # noqa: E501

        Invitation email will not be sent if set to true. Default value is false  # noqa: E501

        :return: The invitation_disabled of this UpdateUserPayload.  # noqa: E501
        :rtype: bool
        """
        return self._invitation_disabled

    @invitation_disabled.setter
    def invitation_disabled(self, invitation_disabled):
        """Sets the invitation_disabled of this UpdateUserPayload.

        Invitation email will not be sent if set to true. Default value is false  # noqa: E501

        :param invitation_disabled: The invitation_disabled of this UpdateUserPayload.  # noqa: E501
        :type: bool
        """

        self._invitation_disabled = invitation_disabled

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
        if issubclass(UpdateUserPayload, dict):
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
        if not isinstance(other, UpdateUserPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other