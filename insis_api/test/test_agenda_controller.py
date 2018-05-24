# coding: utf-8

from __future__ import absolute_import

from flask import json
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAgendaController(BaseTestCase):
    """AgendaController integration test stubs"""

    def test_get_schedule_agenda(self):
        """Test case for get_schedule_agenda

        Get week schedule agenda
        """
        body = User()
        response = self.client.open(
            '/agenda',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
