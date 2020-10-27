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


class CreateAlertPayload(object):
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
        'user': 'str',
        'note': 'str',
        'source': 'str',
        'message': 'str',
        'alias': 'str',
        'description': 'str',
        'responders': 'list[Recipient]',
        'visible_to': 'list[Recipient]',
        'actions': 'list[str]',
        'tags': 'list[str]',
        'details': 'dict(str, str)',
        'entity': 'str',
        'priority': 'str'
    }

    attribute_map = {
        'user': 'user',
        'note': 'note',
        'source': 'source',
        'message': 'message',
        'alias': 'alias',
        'description': 'description',
        'responders': 'responders',
        'visible_to': 'visibleTo',
        'actions': 'actions',
        'tags': 'tags',
        'details': 'details',
        'entity': 'entity',
        'priority': 'priority'
    }

    def __init__(self, user=None, note=None, source=None, message=None, alias=None, description=None, responders=None, visible_to=None, actions=None, tags=None, details=None, entity=None, priority=None):  # noqa: E501
        """CreateAlertPayload - a model defined in Swagger"""  # noqa: E501

        self._user = None
        self._note = None
        self._source = None
        self._message = None
        self._alias = None
        self._description = None
        self._responders = None
        self._visible_to = None
        self._actions = None
        self._tags = None
        self._details = None
        self._entity = None
        self._priority = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if note is not None:
            self.note = note
        if source is not None:
            self.source = source
        self.message = message
        if alias is not None:
            self.alias = alias
        if description is not None:
            self.description = description
        if responders is not None:
            self.responders = responders
        if visible_to is not None:
            self.visible_to = visible_to
        if actions is not None:
            self.actions = actions
        if tags is not None:
            self.tags = tags
        if details is not None:
            self.details = details
        if entity is not None:
            self.entity = entity
        if priority is not None:
            self.priority = priority

    @property
    def user(self):
        """Gets the user of this CreateAlertPayload.  # noqa: E501

        Display name of the request owner  # noqa: E501

        :return: The user of this CreateAlertPayload.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this CreateAlertPayload.

        Display name of the request owner  # noqa: E501

        :param user: The user of this CreateAlertPayload.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def note(self):
        """Gets the note of this CreateAlertPayload.  # noqa: E501

        Additional note that will be added while creating the alert  # noqa: E501

        :return: The note of this CreateAlertPayload.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this CreateAlertPayload.

        Additional note that will be added while creating the alert  # noqa: E501

        :param note: The note of this CreateAlertPayload.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def source(self):
        """Gets the source of this CreateAlertPayload.  # noqa: E501

        Source field of the alert. Default value is IP address of the incoming request  # noqa: E501

        :return: The source of this CreateAlertPayload.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CreateAlertPayload.

        Source field of the alert. Default value is IP address of the incoming request  # noqa: E501

        :param source: The source of this CreateAlertPayload.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def message(self):
        """Gets the message of this CreateAlertPayload.  # noqa: E501

        Message of the alert  # noqa: E501

        :return: The message of this CreateAlertPayload.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CreateAlertPayload.

        Message of the alert  # noqa: E501

        :param message: The message of this CreateAlertPayload.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def alias(self):
        """Gets the alias of this CreateAlertPayload.  # noqa: E501

        Client-defined identifier of the alert, that is also the key element of alert deduplication.  # noqa: E501

        :return: The alias of this CreateAlertPayload.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this CreateAlertPayload.

        Client-defined identifier of the alert, that is also the key element of alert deduplication.  # noqa: E501

        :param alias: The alias of this CreateAlertPayload.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def description(self):
        """Gets the description of this CreateAlertPayload.  # noqa: E501

        Description field of the alert that is generally used to provide a detailed information about the alert.  # noqa: E501

        :return: The description of this CreateAlertPayload.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAlertPayload.

        Description field of the alert that is generally used to provide a detailed information about the alert.  # noqa: E501

        :param description: The description of this CreateAlertPayload.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def responders(self):
        """Gets the responders of this CreateAlertPayload.  # noqa: E501

        Responders that the alert will be routed to send notifications  # noqa: E501

        :return: The responders of this CreateAlertPayload.  # noqa: E501
        :rtype: list[Recipient]
        """
        return self._responders

    @responders.setter
    def responders(self, responders):
        """Sets the responders of this CreateAlertPayload.

        Responders that the alert will be routed to send notifications  # noqa: E501

        :param responders: The responders of this CreateAlertPayload.  # noqa: E501
        :type: list[Recipient]
        """

        self._responders = responders

    @property
    def visible_to(self):
        """Gets the visible_to of this CreateAlertPayload.  # noqa: E501

        Teams and users that the alert will become visible to without sending any notification  # noqa: E501

        :return: The visible_to of this CreateAlertPayload.  # noqa: E501
        :rtype: list[Recipient]
        """
        return self._visible_to

    @visible_to.setter
    def visible_to(self, visible_to):
        """Sets the visible_to of this CreateAlertPayload.

        Teams and users that the alert will become visible to without sending any notification  # noqa: E501

        :param visible_to: The visible_to of this CreateAlertPayload.  # noqa: E501
        :type: list[Recipient]
        """

        self._visible_to = visible_to

    @property
    def actions(self):
        """Gets the actions of this CreateAlertPayload.  # noqa: E501

        Custom actions that will be available for the alert  # noqa: E501

        :return: The actions of this CreateAlertPayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this CreateAlertPayload.

        Custom actions that will be available for the alert  # noqa: E501

        :param actions: The actions of this CreateAlertPayload.  # noqa: E501
        :type: list[str]
        """

        self._actions = actions

    @property
    def tags(self):
        """Gets the tags of this CreateAlertPayload.  # noqa: E501

        Tags of the alert  # noqa: E501

        :return: The tags of this CreateAlertPayload.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateAlertPayload.

        Tags of the alert  # noqa: E501

        :param tags: The tags of this CreateAlertPayload.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def details(self):
        """Gets the details of this CreateAlertPayload.  # noqa: E501

        Map of key-value pairs to use as custom properties of the alert  # noqa: E501

        :return: The details of this CreateAlertPayload.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this CreateAlertPayload.

        Map of key-value pairs to use as custom properties of the alert  # noqa: E501

        :param details: The details of this CreateAlertPayload.  # noqa: E501
        :type: dict(str, str)
        """

        self._details = details

    @property
    def entity(self):
        """Gets the entity of this CreateAlertPayload.  # noqa: E501

        Entity field of the alert that is generally used to specify which domain alert is related to  # noqa: E501

        :return: The entity of this CreateAlertPayload.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this CreateAlertPayload.

        Entity field of the alert that is generally used to specify which domain alert is related to  # noqa: E501

        :param entity: The entity of this CreateAlertPayload.  # noqa: E501
        :type: str
        """

        self._entity = entity

    @property
    def priority(self):
        """Gets the priority of this CreateAlertPayload.  # noqa: E501

        Priority level of the alert  # noqa: E501

        :return: The priority of this CreateAlertPayload.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateAlertPayload.

        Priority level of the alert  # noqa: E501

        :param priority: The priority of this CreateAlertPayload.  # noqa: E501
        :type: str
        """
        allowed_values = ["P1", "P2", "P3", "P4", "P5"]  # noqa: E501
        if priority not in allowed_values:
            raise ValueError(
                "Invalid value for `priority` ({0}), must be one of {1}"  # noqa: E501
                .format(priority, allowed_values)
            )

        self._priority = priority

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
        if issubclass(CreateAlertPayload, dict):
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
        if not isinstance(other, CreateAlertPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
