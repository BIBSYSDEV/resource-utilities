"""Module to provide simple, consistent access to AWS Dynamo DB"""

import boto3
from boto3 import Session

from .constants import Constants

_SESSION = Session()
_REGIONS = _SESSION.get_available_regions(Constants.ddb())


def _validate_region(region):
    """Validates the region input for DynamoDB"""

    if region in _REGIONS:
        _region = region
    else:
        raise ValueError('Region "%s" is invalid' % region)
    return _region


def connect(region):
    """Returns a Dynamo DB Service Resource in a valid region"""
    return boto3.resource(Constants.ddb(), _validate_region(region))
