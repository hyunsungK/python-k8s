# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1beta1_host_port_range import V1beta1HostPortRange


class TestV1beta1HostPortRange(unittest.TestCase):
    """ V1beta1HostPortRange unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1HostPortRange(self):
        """
        Test V1beta1HostPortRange
        """
        model = kubernetes.client.models.v1beta1_host_port_range.V1beta1HostPortRange()


if __name__ == '__main__':
    unittest.main()