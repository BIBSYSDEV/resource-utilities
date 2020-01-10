"""Helper methods"""

from .constants import Constants


def remove_none_values(temp_value):
    """Remove None from dicts to ensure that nulls are ignored"""
    return_value = dict()
    for key, value in temp_value.items():
        if value is not None:
            return_value[key] = value
    return return_value


def response(status_code, body, headers=None):
    """Formulates a response with status code and body"""
    composed_response = {
        Constants.RESPONSE_STATUS_CODE: status_code,
        Constants.RESPONSE_BODY: body
    }
    if headers is not None:
        composed_response[Constants.RESPONSE_HEADERS] = headers
    return composed_response
