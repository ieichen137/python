# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.certificates_v1beta1_api import CertificatesV1beta1Api


class TestCertificatesV1beta1Api(unittest.TestCase):
    """ CertificatesV1beta1Api unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.certificates_v1beta1_api.CertificatesV1beta1Api()

    def tearDown(self):
        pass

    def test_create_certificate_signing_request(self):
        """
        Test case for create_certificate_signing_request

        
        """
        pass

    def test_delete_certificate_signing_request(self):
        """
        Test case for delete_certificate_signing_request

        
        """
        pass

    def test_delete_collection_certificate_signing_request(self):
        """
        Test case for delete_collection_certificate_signing_request

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_certificate_signing_request(self):
        """
        Test case for list_certificate_signing_request

        
        """
        pass

    def test_patch_certificate_signing_request(self):
        """
        Test case for patch_certificate_signing_request

        
        """
        pass

    def test_patch_certificate_signing_request_status(self):
        """
        Test case for patch_certificate_signing_request_status

        
        """
        pass

    def test_read_certificate_signing_request(self):
        """
        Test case for read_certificate_signing_request

        
        """
        pass

    def test_read_certificate_signing_request_status(self):
        """
        Test case for read_certificate_signing_request_status

        
        """
        pass

    def test_replace_certificate_signing_request(self):
        """
        Test case for replace_certificate_signing_request

        
        """
        pass

    def test_replace_certificate_signing_request_approval(self):
        """
        Test case for replace_certificate_signing_request_approval

        
        """
        pass

    def test_replace_certificate_signing_request_status(self):
        """
        Test case for replace_certificate_signing_request_status

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
