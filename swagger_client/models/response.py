# coding: utf-8

"""
    StreetSpectra API

    API description for StreetSpectra project  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: jgcasta@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Response(object):
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
        'info_id': 'str',
        'info_desc': 'str',
        'data': 'list[object]'
    }

    attribute_map = {
        'info_id': 'info_id',
        'info_desc': 'info_desc',
        'data': 'data'
    }

    def __init__(self, info_id=None, info_desc=None, data=None):  # noqa: E501
        """Response - a model defined in Swagger"""  # noqa: E501

        self._info_id = None
        self._info_desc = None
        self._data = None
        self.discriminator = None

        self.info_id = info_id
        self.info_desc = info_desc
        self.data = data

    @property
    def info_id(self):
        """Gets the info_id of this Response.  # noqa: E501

        Information response id  # noqa: E501

        :return: The info_id of this Response.  # noqa: E501
        :rtype: str
        """
        return self._info_id

    @info_id.setter
    def info_id(self, info_id):
        """Sets the info_id of this Response.

        Information response id  # noqa: E501

        :param info_id: The info_id of this Response.  # noqa: E501
        :type: str
        """
        if info_id is None:
            raise ValueError("Invalid value for `info_id`, must not be `None`")  # noqa: E501

        self._info_id = info_id

    @property
    def info_desc(self):
        """Gets the info_desc of this Response.  # noqa: E501

        Information response description  # noqa: E501

        :return: The info_desc of this Response.  # noqa: E501
        :rtype: str
        """
        return self._info_desc

    @info_desc.setter
    def info_desc(self, info_desc):
        """Sets the info_desc of this Response.

        Information response description  # noqa: E501

        :param info_desc: The info_desc of this Response.  # noqa: E501
        :type: str
        """
        if info_desc is None:
            raise ValueError("Invalid value for `info_desc`, must not be `None`")  # noqa: E501

        self._info_desc = info_desc

    @property
    def data(self):
        """Gets the data of this Response.  # noqa: E501

        Object response  # noqa: E501

        :return: The data of this Response.  # noqa: E501
        :rtype: list[object]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Response.

        Object response  # noqa: E501

        :param data: The data of this Response.  # noqa: E501
        :type: list[object]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if issubclass(Response, dict):
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
        if not isinstance(other, Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
