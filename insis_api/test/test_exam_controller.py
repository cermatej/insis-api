# coding: utf-8

from __future__ import absolute_import

import os
from flask import json
from six import BytesIO

from insis_api.models.exam import Exam  # noqa: E501
from insis_api.models.user import User  # noqa: E501
from insis_api.test import BaseTestCase


class TestExamController(BaseTestCase):
    """ExamController integration test stubs"""

    def test_get_exam(self):
        """Test case for get_exam

        Get all exams
        """
        body = User(os.environ['INSIS_USERNAME'], os.environ['INSIS_PASS'])
        response = self.client.open(
            '/exam',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
