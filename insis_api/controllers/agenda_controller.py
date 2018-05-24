import connexion

from .models.user import User  # noqa: E501


def get_schedule_agenda(body):  # noqa: E501
    """Get week schedule agenda

     # noqa: E501

    :param body: Insis user credentials
    :type body: dict | bytes

    :rtype: Exam
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
