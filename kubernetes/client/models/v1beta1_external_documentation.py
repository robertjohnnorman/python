# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1ExternalDocumentation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'description': 'str',
        'url': 'str'
    }

    attribute_map = {
        'description': 'description',
        'url': 'url'
    }

    def __init__(self, description=None, url=None):
        """
        V1beta1ExternalDocumentation - a model defined in Swagger
        """

        self._description = None
        self._url = None
        self.discriminator = None

        if description is not None:
          self.description = description
        if url is not None:
          self.url = url

    @property
    def description(self):
        """
        Gets the description of this V1beta1ExternalDocumentation.

        :return: The description of this V1beta1ExternalDocumentation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this V1beta1ExternalDocumentation.

        :param description: The description of this V1beta1ExternalDocumentation.
        :type: str
        """

        self._description = description

    @property
    def url(self):
        """
        Gets the url of this V1beta1ExternalDocumentation.

        :return: The url of this V1beta1ExternalDocumentation.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this V1beta1ExternalDocumentation.

        :param url: The url of this V1beta1ExternalDocumentation.
        :type: str
        """

        self._url = url

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1beta1ExternalDocumentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
