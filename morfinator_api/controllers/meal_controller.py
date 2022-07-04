import connexion
import six

from morfinator_api.models.api_response import ApiResponse  # noqa: E501
from morfinator_api.models.meal import Meal  # noqa: E501
from morfinator_api import util


def add_meal(body):  # noqa: E501
    """Add a new meal to the db

     # noqa: E501

    :param body: Meal object that needs to be added to the store
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = Meal.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_meal(body, id):  # noqa: E501
    """Remove meal from the db

     # noqa: E501

    :param body: Meal object that needs to be added to the store
    :type body: dict | bytes
    :param id: The id that needs to be fetched.
    :type id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Meal.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_meal(body, id):  # noqa: E501
    """Update an existing meal

     # noqa: E501

    :param body: Meal object that needs to be added
    :type body: dict | bytes
    :param id: The id that needs to be fetched.
    :type id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Meal.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
