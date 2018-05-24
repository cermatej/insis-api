# coding: utf-8

from __future__ import absolute_import

import os

from flask import json

from insis_api.models.user import User  # noqa: E501
from insis_api.test import BaseTestCase


class TestAgendaController(BaseTestCase):
    """AgendaController integration test stubs"""

    def test_get_schedule_agenda(self):
        """Test case for get_schedule_agenda

        Get week schedule agenda
        """
        body = User(os.environ['INSIS_USERNAME'], os.environ['INSIS_PASS'])
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
