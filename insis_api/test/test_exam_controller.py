# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from insis_api.models.exam import Exam  # noqa: E501
from insis_api.test import BaseTestCase


class TestExamController(BaseTestCase):
    """ExamController integration test stubs"""

    def test_disenroll_exam_by_id(self):
        """Test case for disenroll_exam_by_id

        Disenroll exam with id
        """
        response = self.client.open(
            '/v2/exam/{examId}/disenroll'.format(examId=789),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_enroll_exam_by_id(self):
        """Test case for enroll_exam_by_id

        Enroll exam with id
        """
        response = self.client.open(
            '/v2/exam/{examId}/enroll'.format(examId=789),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_exam(self):
        """Test case for get_exam

        Get all exams
        """
        response = self.client.open(
            '/v2/exam',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_exam_by_id(self):
        """Test case for get_exam_by_id

        Get exam by id
        """
        response = self.client.open(
            '/v2/exam/{examId}'.format(examId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
