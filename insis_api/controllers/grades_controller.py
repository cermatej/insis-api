import connexion

from swagger_server.models.user import User  # noqa: E501


def get_grades_from_subject(subjectId, body):  # noqa: E501
    """Get grades from subject

     # noqa: E501

    :param subjectId: ID of subject which grades needs to be fetched
    :type subjectId: int
    :param body: Insis user credentials
    :type body: dict | bytes

    :rtype: Exam
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
