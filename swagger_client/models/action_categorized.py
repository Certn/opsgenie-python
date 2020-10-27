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


class ActionCategorized(object):
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
        'parent': 'IntegrationMeta',
        'ignore': 'list[IgnoreIntegrationAction]',
        'create': 'list[CreateIntegrationAction]',
        'close': 'list[CloseIntegrationAction]',
        'acknowledge': 'list[AckIntegrationAction]',
        'add_note': 'list[AddNoteIntegrationAction]'
    }

    attribute_map = {
        'parent': '_parent',
        'ignore': 'ignore',
        'create': 'create',
        'close': 'close',
        'acknowledge': 'acknowledge',
        'add_note': 'addNote'
    }

    def __init__(self, parent=None, ignore=None, create=None, close=None, acknowledge=None, add_note=None):  # noqa: E501
        """ActionCategorized - a model defined in Swagger"""  # noqa: E501

        self._parent = None
        self._ignore = None
        self._create = None
        self._close = None
        self._acknowledge = None
        self._add_note = None
        self.discriminator = None

        if parent is not None:
            self.parent = parent
        if ignore is not None:
            self.ignore = ignore
        if create is not None:
            self.create = create
        if close is not None:
            self.close = close
        if acknowledge is not None:
            self.acknowledge = acknowledge
        if add_note is not None:
            self.add_note = add_note

    @property
    def parent(self):
        """Gets the parent of this ActionCategorized.  # noqa: E501


        :return: The parent of this ActionCategorized.  # noqa: E501
        :rtype: IntegrationMeta
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ActionCategorized.


        :param parent: The parent of this ActionCategorized.  # noqa: E501
        :type: IntegrationMeta
        """

        self._parent = parent

    @property
    def ignore(self):
        """Gets the ignore of this ActionCategorized.  # noqa: E501


        :return: The ignore of this ActionCategorized.  # noqa: E501
        :rtype: list[IgnoreIntegrationAction]
        """
        return self._ignore

    @ignore.setter
    def ignore(self, ignore):
        """Sets the ignore of this ActionCategorized.


        :param ignore: The ignore of this ActionCategorized.  # noqa: E501
        :type: list[IgnoreIntegrationAction]
        """

        self._ignore = ignore

    @property
    def create(self):
        """Gets the create of this ActionCategorized.  # noqa: E501


        :return: The create of this ActionCategorized.  # noqa: E501
        :rtype: list[CreateIntegrationAction]
        """
        return self._create

    @create.setter
    def create(self, create):
        """Sets the create of this ActionCategorized.


        :param create: The create of this ActionCategorized.  # noqa: E501
        :type: list[CreateIntegrationAction]
        """

        self._create = create

    @property
    def close(self):
        """Gets the close of this ActionCategorized.  # noqa: E501


        :return: The close of this ActionCategorized.  # noqa: E501
        :rtype: list[CloseIntegrationAction]
        """
        return self._close

    @close.setter
    def close(self, close):
        """Sets the close of this ActionCategorized.


        :param close: The close of this ActionCategorized.  # noqa: E501
        :type: list[CloseIntegrationAction]
        """

        self._close = close

    @property
    def acknowledge(self):
        """Gets the acknowledge of this ActionCategorized.  # noqa: E501


        :return: The acknowledge of this ActionCategorized.  # noqa: E501
        :rtype: list[AckIntegrationAction]
        """
        return self._acknowledge

    @acknowledge.setter
    def acknowledge(self, acknowledge):
        """Sets the acknowledge of this ActionCategorized.


        :param acknowledge: The acknowledge of this ActionCategorized.  # noqa: E501
        :type: list[AckIntegrationAction]
        """

        self._acknowledge = acknowledge

    @property
    def add_note(self):
        """Gets the add_note of this ActionCategorized.  # noqa: E501


        :return: The add_note of this ActionCategorized.  # noqa: E501
        :rtype: list[AddNoteIntegrationAction]
        """
        return self._add_note

    @add_note.setter
    def add_note(self, add_note):
        """Sets the add_note of this ActionCategorized.


        :param add_note: The add_note of this ActionCategorized.  # noqa: E501
        :type: list[AddNoteIntegrationAction]
        """

        self._add_note = add_note

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
        if issubclass(ActionCategorized, dict):
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
        if not isinstance(other, ActionCategorized):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other