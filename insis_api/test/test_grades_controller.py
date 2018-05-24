# coding: utf-8

from __future__ import absolute_import

from flask import json
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGradesController(BaseTestCase):
    """GradesController integration test stubs"""

    def test_get_grades_from_subject(self):
        """Test case for get_grades_from_subject

        Get grades from subject
        """
        body = User()
        response = self.client.open(
            '/grades/{subjectId}'.format(subjectId=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
