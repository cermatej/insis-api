# coding: utf-8

from __future__ import absolute_import

from flask import json
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSubjectController(BaseTestCase):
    """SubjectController integration test stubs"""

    def test_get_enrolled_subjects(self):
        """Test case for get_enrolled_subjects

        Get enrolled subjects
        """
        body = User()
        response = self.client.open(
            '/subject/enrolled',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
