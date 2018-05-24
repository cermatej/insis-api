import connexion

from insis_api.models.user import User  # noqa: E501


def get_enrolled_subjects(body):  # noqa: E501
    """Get enrolled subjects

     # noqa: E501

    :param body: Insis user credentials
    :type body: dict | bytes

    :rtype: Exam
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
