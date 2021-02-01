# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestLondonersController(BaseTestCase):
    """LondonersController integration test stubs"""

    def test_get_londoners(self):
        """Test case for get_londoners

        
        """
        response = self.client.open(
            '/londoners',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
