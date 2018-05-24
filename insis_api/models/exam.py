# coding: utf-8

from __future__ import absolute_import

from datetime import datetime  # noqa: F401

from insis_api import util
from insis_api.models.base_model_ import Model


class Exam(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int = None, accessibility: str = None, ident: str = None, subject: str = None,
                 department: str = None, date: datetime = None, room: str = None, type: str = None, teacher: str = None,
                 availability: str = None, sign_in_from: datetime = None, sign_in_to: datetime = None,
                 sign_out_to: datetime = None):  # noqa: E501
        """Exam - a model defined in Swagger

        :param id: The id of this Exam.  # noqa: E501
        :type id: int
        :param accessibility: The accessibility of this Exam.  # noqa: E501
        :type accessibility: str
        :param ident: The ident of this Exam.  # noqa: E501
        :type ident: str
        :param subject: The subject of this Exam.  # noqa: E501
        :type subject: str
        :param department: The department of this Exam.  # noqa: E501
        :type department: str
        :param date: The date of this Exam.  # noqa: E501
        :type date: datetime
        :param room: The room of this Exam.  # noqa: E501
        :type room: str
        :param type: The type of this Exam.  # noqa: E501
        :type type: str
        :param teacher: The teacher of this Exam.  # noqa: E501
        :type teacher: str
        :param availability: The availability of this Exam.  # noqa: E501
        :type availability: str
        :param sign_in_from: The sign_in_from of this Exam.  # noqa: E501
        :type sign_in_from: datetime
        :param sign_in_to: The sign_in_to of this Exam.  # noqa: E501
        :type sign_in_to: datetime
        :param sign_out_to: The sign_out_to of this Exam.  # noqa: E501
        :type sign_out_to: datetime
        """
        self.swagger_types = {
            'id': int,
            'accessibility': str,
            'ident': str,
            'subject': str,
            'department': str,
            'date': datetime,
            'room': str,
            'type': str,
            'teacher': str,
            'availability': str,
            'sign_in_from': datetime,
            'sign_in_to': datetime,
            'sign_out_to': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'accessibility': 'accessibility',
            'ident': 'ident',
            'subject': 'subject',
            'department': 'department',
            'date': 'date',
            'room': 'room',
            'type': 'type',
            'teacher': 'teacher',
            'availability': 'availability',
            'sign_in_from': 'sign_in_from',
            'sign_in_to': 'sign_in_to',
            'sign_out_to': 'sign_out_to'
        }

        self._id = id
        self._accessibility = accessibility
        self._ident = ident
        self._subject = subject
        self._department = department
        self._date = date
        self._room = room
        self._type = type
        self._teacher = teacher
        self._availability = availability
        self._sign_in_from = sign_in_from
        self._sign_in_to = sign_in_to
        self._sign_out_to = sign_out_to

    @classmethod
    def from_dict(cls, dikt) -> 'Exam':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Exam of this Exam.  # noqa: E501
        :rtype: Exam
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Exam.


        :return: The id of this Exam.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Exam.


        :param id: The id of this Exam.
        :type id: int
        """

        self._id = id

    @property
    def accessibility(self) -> str:
        """Gets the accessibility of this Exam.


        :return: The accessibility of this Exam.
        :rtype: str
        """
        return self._accessibility

    @accessibility.setter
    def accessibility(self, accessibility: str):
        """Sets the accessibility of this Exam.


        :param accessibility: The accessibility of this Exam.
        :type accessibility: str
        """

        self._accessibility = accessibility

    @property
    def ident(self) -> str:
        """Gets the ident of this Exam.


        :return: The ident of this Exam.
        :rtype: str
        """
        return self._ident

    @ident.setter
    def ident(self, ident: str):
        """Sets the ident of this Exam.


        :param ident: The ident of this Exam.
        :type ident: str
        """

        self._ident = ident

    @property
    def subject(self) -> str:
        """Gets the subject of this Exam.


        :return: The subject of this Exam.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str):
        """Sets the subject of this Exam.


        :param subject: The subject of this Exam.
        :type subject: str
        """

        self._subject = subject

    @property
    def department(self) -> str:
        """Gets the department of this Exam.


        :return: The department of this Exam.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department: str):
        """Sets the department of this Exam.


        :param department: The department of this Exam.
        :type department: str
        """

        self._department = department

    @property
    def date(self) -> datetime:
        """Gets the date of this Exam.


        :return: The date of this Exam.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date: datetime):
        """Sets the date of this Exam.


        :param date: The date of this Exam.
        :type date: datetime
        """

        self._date = date

    @property
    def room(self) -> str:
        """Gets the room of this Exam.


        :return: The room of this Exam.
        :rtype: str
        """
        return self._room

    @room.setter
    def room(self, room: str):
        """Sets the room of this Exam.


        :param room: The room of this Exam.
        :type room: str
        """

        self._room = room

    @property
    def type(self) -> str:
        """Gets the type of this Exam.


        :return: The type of this Exam.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Exam.


        :param type: The type of this Exam.
        :type type: str
        """

        self._type = type

    @property
    def teacher(self) -> str:
        """Gets the teacher of this Exam.


        :return: The teacher of this Exam.
        :rtype: str
        """
        return self._teacher

    @teacher.setter
    def teacher(self, teacher: str):
        """Sets the teacher of this Exam.


        :param teacher: The teacher of this Exam.
        :type teacher: str
        """

        self._teacher = teacher

    @property
    def availability(self) -> str:
        """Gets the availability of this Exam.


        :return: The availability of this Exam.
        :rtype: str
        """
        return self._availability

    @availability.setter
    def availability(self, availability: str):
        """Sets the availability of this Exam.


        :param availability: The availability of this Exam.
        :type availability: str
        """

        self._availability = availability

    @property
    def sign_in_from(self) -> datetime:
        """Gets the sign_in_from of this Exam.


        :return: The sign_in_from of this Exam.
        :rtype: datetime
        """
        return self._sign_in_from

    @sign_in_from.setter
    def sign_in_from(self, sign_in_from: datetime):
        """Sets the sign_in_from of this Exam.


        :param sign_in_from: The sign_in_from of this Exam.
        :type sign_in_from: datetime
        """

        self._sign_in_from = sign_in_from

    @property
    def sign_in_to(self) -> datetime:
        """Gets the sign_in_to of this Exam.


        :return: The sign_in_to of this Exam.
        :rtype: datetime
        """
        return self._sign_in_to

    @sign_in_to.setter
    def sign_in_to(self, sign_in_to: datetime):
        """Sets the sign_in_to of this Exam.


        :param sign_in_to: The sign_in_to of this Exam.
        :type sign_in_to: datetime
        """

        self._sign_in_to = sign_in_to

    @property
    def sign_out_to(self) -> datetime:
        """Gets the sign_out_to of this Exam.


        :return: The sign_out_to of this Exam.
        :rtype: datetime
        """
        return self._sign_out_to

    @sign_out_to.setter
    def sign_out_to(self, sign_out_to: datetime):
        """Sets the sign_out_to of this Exam.


        :param sign_out_to: The sign_out_to of this Exam.
        :type sign_out_to: datetime
        """

        self._sign_out_to = sign_out_to
