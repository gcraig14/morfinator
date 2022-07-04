# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from morfinator_api.models.user_shop_list import UserShopList  # noqa: E501
from morfinator_api.test import BaseTestCase


class TestUsershoplistController(BaseTestCase):
    """UsershoplistController integration test stubs"""

    def test_add_ingredient_for_user(self):
        """Test case for add_ingredient_for_user

        Add new ingredient to user
        """
        ingredient = UserShopList()
        response = self.client.open(
            '/v1/usershoplist/',
            method='POST',
            data=json.dumps(ingredient),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_ingredient_for_user(self):
        """Test case for delete_ingredient_for_user

        Delete ingredient for user
        """
        ingredient = UserShopList()
        response = self.client.open(
            '/v1/usershoplist/',
            method='DELETE',
            data=json.dumps(ingredient),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_shop_list(self):
        """Test case for get_shop_list

        Get ingredients for user
        """
        response = self.client.open(
            '/v1/usershoplist/{user_id}'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_updategredient_for_user(self):
        """Test case for updategredient_for_user

        Modify user's ingredient
        """
        ingredient = UserShopList()
        response = self.client.open(
            '/v1/usershoplist/',
            method='PUT',
            data=json.dumps(ingredient),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
