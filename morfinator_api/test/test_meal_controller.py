# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from morfinator_api.models.api_response import ApiResponse  # noqa: E501
from morfinator_api.models.meal import Meal  # noqa: E501
from morfinator_api.test import BaseTestCase


class TestMealController(BaseTestCase):
    """MealController integration test stubs"""

    def test_add_meal(self):
        """Test case for add_meal

        Add a new meal to the db
        """
        body = Meal()
        response = self.client.open(
            '/v1/meal',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_meal(self):
        """Test case for delete_meal

        Remove meal from the db
        """
        body = Meal()
        response = self.client.open(
            '/v1/meal/{id}'.format(id=56),
            method='DELETE',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_meal(self):
        """Test case for update_meal

        Update an existing meal
        """
        body = Meal()
        response = self.client.open(
            '/v1/meal/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
