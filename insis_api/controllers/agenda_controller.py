import requests
from bs4 import BeautifulSoup
from connexion import NoContent

from insis_api import util
from insis_api.models.agenda_event import AgendaEvent

SHOW_AGENDA_LINK = 'https://insis.vse.cz/auth/katalog/rozvrhy_view.pl'


def get_schedule_agenda(body):  # noqa: E501
    """Get week schedule agenda

     # noqa: E501

    :param body: Insis user credentials
    :type body: dict | bytes

    :rtype: AgendaEvent
    """
    user = util.get_credentials()
    with requests.Session() as ses:
        util.log_in(ses, user)
        args = {
            'osobni': 1,
            'z': 1,
            'k': 1,
            'f': 0,
            'studijni_zpet': 0,
            'format': 'list',
            'typ_vypisu': 'souhrn',
            'zobraz': 1,
            'zobraz2': 'Zobrazit'
        }

        res = ses.post(SHOW_AGENDA_LINK, data=args)

        bs = BeautifulSoup(res.text, "html.parser")
        exams = bs.select('#tmtab_1 tbody tr')

        agenda_events = [__get_agenda_from_html(exam) for exam in exams]
    return (agenda_events, 200) if agenda_events else (NoContent, 404)


def __get_agenda_from_html(exam):
    day = exam.contents[0].text
    time_from = exam.contents[1].text
    time_to = exam.contents[2].text
    subject = exam.contents[3].text
    type = exam.contents[4].text
    room = exam.contents[5].text
    teacher = exam.contents[6].text
    capacity = exam.contents[8].text

    return AgendaEvent(day, time_from, time_to, subject, type, room, teacher, capacity)
