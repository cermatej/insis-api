import datetime
import re
import typing
from typing import Dict

import requests
import six
from bs4 import BeautifulSoup


def log_in(ses: requests.Session, user: 'User'):
    data = {
        'lang': 'cz',
        'destination': '/auth/?lang=cz',
        'credential_0': user.username,
        'credential_1': user.password,
        'credential_2': '86400',
        'login': 'Přihlásit se'
    }
    browser_headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.40 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Language': 'cs-CZ,cs;q=0.9,en;q=0.8'
    }
    ses.headers.update(browser_headers)
    ses.post('https://insis.vse.cz/system/login.pl', data=data)


def get_study_info(ses: requests.Session) -> Dict[str, str]:
    res = ses.post('https://insis.vse.cz/auth/student/moje_studium.pl')

    # scrape study info
    bs = BeautifulSoup(res.text, "html.parser")
    link = bs.select('td[align=center] a')[0].attrs['href']

    info: dict = {}
    for key in ['studium', 'obdobi']:
        info[key] = __get_link_val(link, key)

    return info


def __get_link_val(link, key):
    return re.search(f'{key}=(\w+)', link).group(1)


def _deserialize(data, klass):
    """Deserializes dict, list, str into an object.

    :param data: dict, list or str.
    :param klass: class literal, or string of class name.

    :return: object.
    """
    if data is None:
        return None

    if klass in six.integer_types or klass in (float, str, bool):
        return _deserialize_primitive(data, klass)
    elif klass == object:
        return _deserialize_object(data)
    elif klass == datetime.date:
        return deserialize_date(data)
    elif klass == datetime.datetime:
        return deserialize_datetime(data)
    elif type(klass) == typing.GenericMeta:
        if klass.__extra__ == list:
            return _deserialize_list(data, klass.__args__[0])
        if klass.__extra__ == dict:
            return _deserialize_dict(data, klass.__args__[1])
    else:
        return deserialize_model(data, klass)


def _deserialize_primitive(data, klass):
    """Deserializes to primitive type.

    :param data: data to deserialize.
    :param klass: class literal.

    :return: int, long, float, str, bool.
    :rtype: int | long | float | str | bool
    """
    try:
        value = klass(data)
    except UnicodeEncodeError:
        value = six.u(data)
    except TypeError:
        value = data
    return value


def _deserialize_object(value):
    """Return a original value.

    :return: object.
    """
    return value


def deserialize_date(string):
    """Deserializes string to date.

    :param string: str.
    :type string: str
    :return: date.
    :rtype: date
    """
    try:
        from dateutil.parser import parse
        return parse(string).date()
    except ImportError:
        return string


def deserialize_datetime(string):
    """Deserializes string to datetime.

    The string should be in iso8601 datetime format.

    :param string: str.
    :type string: str
    :return: datetime.
    :rtype: datetime
    """
    try:
        from dateutil.parser import parse
        return parse(string)
    except ImportError:
        return string


def deserialize_model(data, klass):
    """Deserializes list or dict to model.

    :param data: dict, list.
    :type data: dict | list
    :param klass: class literal.
    :return: model object.
    """
    instance = klass()

    if not instance.swagger_types:
        return data

    for attr, attr_type in six.iteritems(instance.swagger_types):
        if data is not None \
            and instance.attribute_map[attr] in data \
            and isinstance(data, (list, dict)):
            value = data[instance.attribute_map[attr]]
            setattr(instance, attr, _deserialize(value, attr_type))

    return instance


def _deserialize_list(data, boxed_type):
    """Deserializes a list and its elements.

    :param data: list to deserialize.
    :type data: list
    :param boxed_type: class literal.

    :return: deserialized list.
    :rtype: list
    """
    return [_deserialize(sub_data, boxed_type)
            for sub_data in data]


def _deserialize_dict(data, boxed_type):
    """Deserializes a dict and its elements.

    :param data: dict to deserialize.
    :type data: dict
    :param boxed_type: class literal.

    :return: deserialized dict.
    :rtype: dict
    """
    return {k: _deserialize(v, boxed_type)
            for k, v in six.iteritems(data)}
