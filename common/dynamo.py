import boto3
from boto3 import Session

from constants import Constants

_session = Session()
_regions = _session.get_available_regions(Constants.DDB)


def _validate_region(region):
    if region in _regions:
        return region
    else:
        raise ValueError('Region "%s" is invalid' % region)


def connect(region):
    return boto3.resource(Constants.DDB, _validate_region(region))

