from typing import Optional, List

import connexion
import re
import requests
import six
from bs4 import BeautifulSoup, Tag
from datetime import datetime

from insis_api.models.exam import Exam  # noqa: E501
from insis_api.models.user import User  # noqa: E501
from connexion import NoContent
from insis_api import util
from insis_api.models.user import User

SELECTOR_ENROLLED_COURSES = '#table_1 tbody tr'
SELECTOR_AVAILABLE_COURSES = '#table_2 tbody tr'

EXAM_ENROLL_LINK = 'https://insis.vse.cz/auth/student/terminy_prihlaseni.pl'
EXAM_LIST_LINK = 'https://insis.vse.cz/auth/student/terminy_seznam.pl'


def disenroll_exam_by_id(examId, body):  # noqa: E501
    """Disenroll exam with id

     # noqa: E501

    :param examId: ID of exam to disenroll
    :type examId: int

    :param body: Insis user credentials
    :type body: dict | bytes

    :rtype: None
    """
    user = __get_credentials()
    with requests.Session() as ses:
        util.log_in(ses, user)
        info = util.get_study_info(ses)
        disenroll = {
            'termin': examId,
            'predmet': '',
            'studium': info['studium'],
            'obdobi': info['obdobi'],
            'odhlasit': 'Odhlásit z termínu'
        }
        ses.post(EXAM_ENROLL_LINK, data=disenroll)

    return NoContent, 200


def enroll_exam_by_id(examId: int, body):  # noqa: E501
    """Enroll exam with id

     # noqa: E501

    :param examId: ID of exam to enroll
    :type examId: int

    :param body: Insis user credentials
    :type body: dict | bytes

    :rtype: None
    """
    user = __get_credentials()
    with requests.Session() as ses:
        util.log_in(ses, user)
        info = util.get_study_info(ses)
        enroll = {
            'termin': examId,
            'predmet': '',
            'studium': info['studium'],
            'obdobi': info['obdobi'],
            'prihlasit': 'Přihlásit na termín'
        }
        ses.post(EXAM_ENROLL_LINK, data=enroll)

    return NoContent, 200


def get_exam(body):  # noqa: E501
    """Get all exams

     # noqa: E501

    :param body: Insis user credentials
    :type body: dict | bytes

    :rtype: Exam
    """
    exams = __list_exams(SELECTOR_AVAILABLE_COURSES)
    return (exams, 200) if exams else (NoContent, 404)


def get_enrolled_exam(body):  # noqa: E501
    """Get enrolled exams

     # noqa: E501

    :param body: Insis user credentials
    :type body: dict | bytes

    :rtype: Exam
    """
    exams = __list_exams(SELECTOR_ENROLLED_COURSES)
    return (exams, 200) if exams else (NoContent, 404)


def get_exam_by_id(examId: int, body):  # noqa: E501
    """Get exam by id

     # noqa: E501

    :param examId: ID of exam that needs to be fetched
    :type examId: int

    :param body: Insis user credentials
    :type body: dict | bytes

    :rtype: Exam
    """
    for exam in __list_exams(SELECTOR_AVAILABLE_COURSES) + __list_exams(SELECTOR_ENROLLED_COURSES):
        if exam.id == examId:
            return exam, 200
    return NoContent, 404


def __list_exams(selector: str) -> List['Exam']:
    user = __get_credentials()
    with requests.Session() as ses:
        util.log_in(ses, user)
        ter = ses.get(EXAM_LIST_LINK)

        # scrape exams html
        bs = BeautifulSoup(ter.text, "html.parser")
        exams = bs.select(selector)

    return [__get_exam_from_html(exam_html.contents) for exam_html in exams] if exams else None


def __get_exam_from_html(exam_html: str) -> 'Exam':
    offset = 1 if len(exam_html) == 13 else 0

    id = int(re.search('termin=([0-9]+);', exam_html[13 - offset].contents[0].contents[0].attrs['href']).group(1))
    accessibility = exam_html[1].contents[0].contents[0].attrs['title'] if len(exam_html) == 14 else None
    ident = exam_html[2 - offset].text
    subject = exam_html[3 - offset].text
    department = exam_html[4 - offset].text
    date = __get_date_from_text(' '.join(exam_html[5 - offset].text.split()[:-1]))
    room = exam_html[6 - offset].text
    type = exam_html[7 - offset].text
    teacher = exam_html[8 - offset].text
    availability = exam_html[9 - offset].text
    sign_in_from, sign_in_to, sign_out_to = [__get_date_from_text(date_str) for date_str
                                             in exam_html[11 - offset].contents[0].contents if
                                             not isinstance(date_str, Tag)]

    return Exam(id, accessibility, ident, subject, department, date, room, type, teacher, availability, sign_in_from, sign_in_to,
                sign_out_to)


def __get_date_from_text(text: str) -> Optional[datetime]:
    try:
        return datetime.strptime(text, '%d.%m.%Y %H:%M')
    except ValueError:
        return None


def __get_credentials() -> Optional['User']:
    if connexion.request.is_json:
        return User.from_dict(connexion.request.get_json())  # noqa: E501
    return None
