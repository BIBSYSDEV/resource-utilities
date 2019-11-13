from unittest import TestCase

from boto3.resources.base import ServiceResource

from common import dynamo


class TestDynamo(TestCase):
    def test_validate_region(self):
        region = 'Lancaster'
        self.assertRaisesRegex(ValueError, 'Region "%s" is invalid' % region, dynamo.connect, region)

    def test_connect(self):
        _dynamo = dynamo.connect('eu-west-1')
        self.assertTrue(isinstance(_dynamo, ServiceResource), 'Type was not DDB')
