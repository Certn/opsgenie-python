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


class Incident(object):
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
        'tiny_id': 'str',
        'message': 'str',
        'status': 'str',
        'is_seen': 'bool',
        'tags': 'list[str]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'source': 'str',
        'owner': 'str',
        'priority': 'str',
        'responders': 'list[Responder]',
        'owner_team': 'str',
        'extra_properties': 'dict(str, str)',
        'request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tiny_id': 'tinyId',
        'message': 'message',
        'status': 'status',
        'is_seen': 'isSeen',
        'tags': 'tags',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'source': 'source',
        'owner': 'owner',
        'priority': 'priority',
        'responders': 'responders',
        'owner_team': 'ownerTeam',
        'extra_properties': 'extraProperties',
        'request_id': 'requestId'
    }

    def __init__(self, id=None, tiny_id=None, message=None, status=None, is_seen=None, tags=None, created_at=None, updated_at=None, source=None, owner=None, priority=None, responders=None, owner_team=None, extra_properties=None, request_id=None):  # noqa: E501
        """Incident - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._tiny_id = None
        self._message = None
        self._status = None
        self._is_seen = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self._source = None
        self._owner = None
        self._priority = None
        self._responders = None
        self._owner_team = None
        self._extra_properties = None
        self._request_id = None
        self.discriminator = None

        self.id = id
        if tiny_id is not None:
            self.tiny_id = tiny_id
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status
        if is_seen is not None:
            self.is_seen = is_seen
        if tags is not None:
            self.tags = tags
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if source is not None:
            self.source = source
        if owner is not None:
            self.owner = owner
        if priority is not None:
            self.priority = priority
        if responders is not None:
            self.responders = responders
        if owner_team is not None:
            self.owner_team = owner_team
        if extra_properties is not None:
            self.extra_properties = extra_properties
        if request_id is not None:
            self.request_id = request_id

    @property
    def id(self):
        """Gets the id of this Incident.  # noqa: E501


        :return: The id of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Incident.


        :param id: The id of this Incident.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def tiny_id(self):
        """Gets the tiny_id of this Incident.  # noqa: E501


        :return: The tiny_id of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._tiny_id

    @tiny_id.setter
    def tiny_id(self, tiny_id):
        """Sets the tiny_id of this Incident.


        :param tiny_id: The tiny_id of this Incident.  # noqa: E501
        :type: str
        """

        self._tiny_id = tiny_id

    @property
    def message(self):
        """Gets the message of this Incident.  # noqa: E501


        :return: The message of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Incident.


        :param message: The message of this Incident.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def status(self):
        """Gets the status of this Incident.  # noqa: E501


        :return: The status of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Incident.


        :param status: The status of this Incident.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def is_seen(self):
        """Gets the is_seen of this Incident.  # noqa: E501


        :return: The is_seen of this Incident.  # noqa: E501
        :rtype: bool
        """
        return self._is_seen

    @is_seen.setter
    def is_seen(self, is_seen):
        """Sets the is_seen of this Incident.


        :param is_seen: The is_seen of this Incident.  # noqa: E501
        :type: bool
        """

        self._is_seen = is_seen

    @property
    def tags(self):
        """Gets the tags of this Incident.  # noqa: E501


        :return: The tags of this Incident.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Incident.


        :param tags: The tags of this Incident.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def created_at(self):
        """Gets the created_at of this Incident.  # noqa: E501


        :return: The created_at of this Incident.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Incident.


        :param created_at: The created_at of this Incident.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Incident.  # noqa: E501


        :return: The updated_at of this Incident.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Incident.


        :param updated_at: The updated_at of this Incident.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def source(self):
        """Gets the source of this Incident.  # noqa: E501


        :return: The source of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Incident.


        :param source: The source of this Incident.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def owner(self):
        """Gets the owner of this Incident.  # noqa: E501


        :return: The owner of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Incident.


        :param owner: The owner of this Incident.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def priority(self):
        """Gets the priority of this Incident.  # noqa: E501


        :return: The priority of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Incident.


        :param priority: The priority of this Incident.  # noqa: E501
        :type: str
        """

        self._priority = priority

    @property
    def responders(self):
        """Gets the responders of this Incident.  # noqa: E501


        :return: The responders of this Incident.  # noqa: E501
        :rtype: list[Responder]
        """
        return self._responders

    @responders.setter
    def responders(self, responders):
        """Sets the responders of this Incident.


        :param responders: The responders of this Incident.  # noqa: E501
        :type: list[Responder]
        """

        self._responders = responders

    @property
    def owner_team(self):
        """Gets the owner_team of this Incident.  # noqa: E501


        :return: The owner_team of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._owner_team

    @owner_team.setter
    def owner_team(self, owner_team):
        """Sets the owner_team of this Incident.


        :param owner_team: The owner_team of this Incident.  # noqa: E501
        :type: str
        """

        self._owner_team = owner_team

    @property
    def extra_properties(self):
        """Gets the extra_properties of this Incident.  # noqa: E501

        Map of key-value pairs to use as custom properties of the incident  # noqa: E501

        :return: The extra_properties of this Incident.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extra_properties

    @extra_properties.setter
    def extra_properties(self, extra_properties):
        """Sets the extra_properties of this Incident.

        Map of key-value pairs to use as custom properties of the incident  # noqa: E501

        :param extra_properties: The extra_properties of this Incident.  # noqa: E501
        :type: dict(str, str)
        """

        self._extra_properties = extra_properties

    @property
    def request_id(self):
        """Gets the request_id of this Incident.  # noqa: E501


        :return: The request_id of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this Incident.


        :param request_id: The request_id of this Incident.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

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
        if issubclass(Incident, dict):
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
        if not isinstance(other, Incident):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
