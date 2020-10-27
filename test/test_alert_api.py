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
from swagger_client.api.alert_api import AlertApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAlertApi(unittest.TestCase):
    """AlertApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.alert_api.AlertApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_acknowledge_alert(self):
        """Test case for acknowledge_alert

        Acknowledge Alert  # noqa: E501
        """
        pass

    def test_add_attachment(self):
        """Test case for add_attachment

        Add Alert Attachment  # noqa: E501
        """
        pass

    def test_add_details(self):
        """Test case for add_details

        Add Details  # noqa: E501
        """
        pass

    def test_add_note(self):
        """Test case for add_note

        Add Note  # noqa: E501
        """
        pass

    def test_add_responder(self):
        """Test case for add_responder

        Add Responder  # noqa: E501
        """
        pass

    def test_add_tags(self):
        """Test case for add_tags

        Add Tags  # noqa: E501
        """
        pass

    def test_add_team(self):
        """Test case for add_team

        Add Team  # noqa: E501
        """
        pass

    def test_assign_alert(self):
        """Test case for assign_alert

        Assign Alert  # noqa: E501
        """
        pass

    def test_close_alert(self):
        """Test case for close_alert

        Close Alert  # noqa: E501
        """
        pass

    def test_count_alerts(self):
        """Test case for count_alerts

        Count Alerts  # noqa: E501
        """
        pass

    def test_create_alert(self):
        """Test case for create_alert

        Create Alert  # noqa: E501
        """
        pass

    def test_create_saved_searches(self):
        """Test case for create_saved_searches

        Create Saved Search  # noqa: E501
        """
        pass

    def test_delete_alert(self):
        """Test case for delete_alert

        Delete Alert  # noqa: E501
        """
        pass

    def test_delete_saved_search(self):
        """Test case for delete_saved_search

        Delete Saved Search  # noqa: E501
        """
        pass

    def test_escalate_alert(self):
        """Test case for escalate_alert

        Escalate Alert  # noqa: E501
        """
        pass

    def test_execute_custom_alert_action(self):
        """Test case for execute_custom_alert_action

        Custom Alert Action  # noqa: E501
        """
        pass

    def test_get_alert(self):
        """Test case for get_alert

        Get Alert  # noqa: E501
        """
        pass

    def test_get_attachment(self):
        """Test case for get_attachment

        Get Alert Attachment  # noqa: E501
        """
        pass

    def test_get_request_status(self):
        """Test case for get_request_status

        Get Request Status of Alert  # noqa: E501
        """
        pass

    def test_get_saved_search(self):
        """Test case for get_saved_search

        Get Saved Search  # noqa: E501
        """
        pass

    def test_list_alerts(self):
        """Test case for list_alerts

        List Alerts  # noqa: E501
        """
        pass

    def test_list_attachments(self):
        """Test case for list_attachments

        List Alert Attachments  # noqa: E501
        """
        pass

    def test_list_logs(self):
        """Test case for list_logs

        List Alert Logs  # noqa: E501
        """
        pass

    def test_list_notes(self):
        """Test case for list_notes

        List Alert Notes  # noqa: E501
        """
        pass

    def test_list_recipients(self):
        """Test case for list_recipients

        List Alert Recipients  # noqa: E501
        """
        pass

    def test_list_saved_searches(self):
        """Test case for list_saved_searches

        Lists Saved Searches  # noqa: E501
        """
        pass

    def test_remove_attachment(self):
        """Test case for remove_attachment

        Remove Alert Attachment  # noqa: E501
        """
        pass

    def test_remove_details(self):
        """Test case for remove_details

        Remove Details  # noqa: E501
        """
        pass

    def test_remove_tags(self):
        """Test case for remove_tags

        Remove Tags  # noqa: E501
        """
        pass

    def test_snooze_alert(self):
        """Test case for snooze_alert

        Snooze Alert  # noqa: E501
        """
        pass

    def test_un_acknowledge_alert(self):
        """Test case for un_acknowledge_alert

        UnAcknowledge Alert  # noqa: E501
        """
        pass

    def test_update_alert_description(self):
        """Test case for update_alert_description

        Update Alert Description  # noqa: E501
        """
        pass

    def test_update_alert_message(self):
        """Test case for update_alert_message

        Update Alert Message  # noqa: E501
        """
        pass

    def test_update_alert_priority(self):
        """Test case for update_alert_priority

        Update Alert Priority  # noqa: E501
        """
        pass

    def test_update_saved_search(self):
        """Test case for update_saved_search

        Update Saved Search  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()