# coding: utf-8

"""
    Opsgenie REST API

    Opsgenie OpenAPI Specification  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.incident_api import IncidentApi  # noqa: E501
from swagger_client.rest import ApiException


class TestIncidentApi(unittest.TestCase):
    """IncidentApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.incident_api.IncidentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_close_incident(self):
        """Test case for close_incident

        Close Incident  # noqa: E501
        """
        pass

    def test_create_incident(self):
        """Test case for create_incident

        Create Incident  # noqa: E501
        """
        pass

    def test_delete_incident(self):
        """Test case for delete_incident

        Delete Incident  # noqa: E501
        """
        pass

    def test_get_incident(self):
        """Test case for get_incident

        Get Incident  # noqa: E501
        """
        pass

    def test_get_incident_request_status(self):
        """Test case for get_incident_request_status

        Get Request Status of Incident  # noqa: E501
        """
        pass

    def test_list_incidents(self):
        """Test case for list_incidents

        List incidents  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
