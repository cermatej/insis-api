# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from insis_api.models.exam import Exam  # noqa: E501
from insis_api.models.user import User  # noqa: E501
from insis_api.test import BaseTestCase


class TestExamController(BaseTestCase):
    """ExamController integration test stubs"""

    def test_disenroll_exam_by_id(self):
        """Test case for disenroll_exam_by_id

        Disenroll exam with id
        """
        body = User()
        response = self.client.open(
            '/exam/{examId}/disenroll'.format(examId=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_enroll_exam_by_id(self):
        """Test case for enroll_exam_by_id

        Enroll exam with id
        """
        body = User()
        response = self.client.open(
            '/exam/{examId}/enroll'.format(examId=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_enrolled_exam(self):
        """Test case for get_enrolled_exam

        Get enrolled exams
        """
        body = User()
        response = self.client.open(
            '/exam/enrolled',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_exam(self):
        """Test case for get_exam

        Get all exams
        """
        body = User()
        response = self.client.open(
            '/exam',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_exam_by_id(self):
        """Test case for get_exam_by_id

        Get exam by id
        """
        body = User()
        response = self.client.open(
            '/exam/{examId}'.format(examId=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
