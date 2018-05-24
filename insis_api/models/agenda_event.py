# coding: utf-8

from __future__ import absolute_import

from insis_api import util
from insis_api.models.base_model_ import Model


class AgendaEvent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, day: str = None, time_from: str = None, time_to: str = None, subject: str = None,
                 type: str = None, room: str = None, teacher: str = None, capacity: int = None):  # noqa: E501
        """AgendaEvent - a model defined in Swagger

        :param day: The day of this AgendaEvent.  # noqa: E501
        :type day: str
        :param time_from: The time_from of this AgendaEvent.  # noqa: E501
        :type time_from: str
        :param time_to: The time_to of this AgendaEvent.  # noqa: E501
        :type time_to: str
        :param subject: The subject of this AgendaEvent.  # noqa: E501
        :type subject: str
        :param type: The type of this AgendaEvent.  # noqa: E501
        :type type: str
        :param room: The room of this AgendaEvent.  # noqa: E501
        :type room: str
        :param teacher: The teacher of this AgendaEvent.  # noqa: E501
        :type teacher: str
        :param capacity: The capacity of this AgendaEvent.  # noqa: E501
        :type capacity: int
        """
        self.swagger_types = {
            'day': str,
            'time_from': str,
            'time_to': str,
            'subject': str,
            'type': str,
            'room': str,
            'teacher': str,
            'capacity': int
        }

        self.attribute_map = {
            'day': 'day',
            'time_from': 'time_from',
            'time_to': 'time_to',
            'subject': 'subject',
            'type': 'type',
            'room': 'room',
            'teacher': 'teacher',
            'capacity': 'capacity'
        }

        self._day = day
        self._time_from = time_from
        self._time_to = time_to
        self._subject = subject
        self._type = type
        self._room = room
        self._teacher = teacher
        self._capacity = capacity

    @classmethod
    def from_dict(cls, dikt) -> 'AgendaEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AgendaEvent of this AgendaEvent.  # noqa: E501
        :rtype: AgendaEvent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def day(self) -> str:
        """Gets the day of this AgendaEvent.


        :return: The day of this AgendaEvent.
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day: str):
        """Sets the day of this AgendaEvent.


        :param day: The day of this AgendaEvent.
        :type day: str
        """

        self._day = day

    @property
    def time_from(self) -> str:
        """Gets the time_from of this AgendaEvent.


        :return: The time_from of this AgendaEvent.
        :rtype: str
        """
        return self._time_from

    @time_from.setter
    def time_from(self, time_from: str):
        """Sets the time_from of this AgendaEvent.


        :param time_from: The time_from of this AgendaEvent.
        :type time_from: str
        """

        self._time_from = time_from

    @property
    def time_to(self) -> str:
        """Gets the time_to of this AgendaEvent.


        :return: The time_to of this AgendaEvent.
        :rtype: str
        """
        return self._time_to

    @time_to.setter
    def time_to(self, time_to: str):
        """Sets the time_to of this AgendaEvent.


        :param time_to: The time_to of this AgendaEvent.
        :type time_to: str
        """

        self._time_to = time_to

    @property
    def subject(self) -> str:
        """Gets the subject of this AgendaEvent.


        :return: The subject of this AgendaEvent.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject: str):
        """Sets the subject of this AgendaEvent.


        :param subject: The subject of this AgendaEvent.
        :type subject: str
        """

        self._subject = subject

    @property
    def type(self) -> str:
        """Gets the type of this AgendaEvent.


        :return: The type of this AgendaEvent.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this AgendaEvent.


        :param type: The type of this AgendaEvent.
        :type type: str
        """

        self._type = type

    @property
    def room(self) -> str:
        """Gets the room of this AgendaEvent.


        :return: The room of this AgendaEvent.
        :rtype: str
        """
        return self._room

    @room.setter
    def room(self, room: str):
        """Sets the room of this AgendaEvent.


        :param room: The room of this AgendaEvent.
        :type room: str
        """

        self._room = room

    @property
    def teacher(self) -> str:
        """Gets the teacher of this AgendaEvent.


        :return: The teacher of this AgendaEvent.
        :rtype: str
        """
        return self._teacher

    @teacher.setter
    def teacher(self, teacher: str):
        """Sets the teacher of this AgendaEvent.


        :param teacher: The teacher of this AgendaEvent.
        :type teacher: str
        """

        self._teacher = teacher

    @property
    def capacity(self) -> int:
        """Gets the capacity of this AgendaEvent.


        :return: The capacity of this AgendaEvent.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int):
        """Sets the capacity of this AgendaEvent.


        :param capacity: The capacity of this AgendaEvent.
        :type capacity: int
        """

        self._capacity = capacity