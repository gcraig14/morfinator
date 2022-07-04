import connexion
import six

from morfinator_api.models.user_meals import UserMeals  # noqa: E501
from morfinator_api import util


def add_meal_for_user(user_id, body):  # noqa: E501
    """Add new meal to user

     # noqa: E501

    :param user_id: The name that needs to be fetched. Use user1 for testing. 
    :type user_id: int
    :param body: Meal object that needs to be added to this user
    :type body: dict | bytes

    :rtype: UserMeals
    """
    if connexion.request.is_json:
        body = UserMeals.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_meals_for_user(user_id):  # noqa: E501
    """Get meals for user

     # noqa: E501

    :param user_id: The name that needs to be fetched. Use user1 for testing. 
    :type user_id: int

    :rtype: UserMeals
    """
    return 'do some magic!'


def update_meals_for_user(user_id):  # noqa: E501
    """Delete meal for user

     # noqa: E501

    :param user_id: The name that needs to be fetched. Use user1 for testing. 
    :type user_id: int

    :rtype: UserMeals
    """
    return 'do some magic!'
