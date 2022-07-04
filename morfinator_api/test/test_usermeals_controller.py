# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from morfinator_api.models.user_meals import UserMeals  # noqa: E501
from morfinator_api.test import BaseTestCase


class TestUsermealsController(BaseTestCase):
    """UsermealsController integration test stubs"""

    def test_add_meal_for_user(self):
        """Test case for add_meal_for_user

        Add new meal to user
        """
        body = UserMeals()
        response = self.client.open(
            '/v1/usermeals/{user_id}'.format(user_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_meals_for_user(self):
        """Test case for get_meals_for_user

        Get meals for user
        """
        response = self.client.open(
            '/v1/usermeals/{user_id}'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_meals_for_user(self):
        """Test case for update_meals_for_user

        Delete meal for user
        """
        response = self.client.open(
            '/v1/usermeals/{user_id}'.format(user_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
