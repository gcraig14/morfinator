import connexion
import six

from morfinator_api.models.user_shop_list import UserShopList  # noqa: E501
from morfinator_api import util


def add_ingredient_for_user(ingredient):  # noqa: E501
    """Add new ingredient to user

     # noqa: E501

    :param ingredient: Ingredient that needs to be added to this user&#39;s shoplist
    :type ingredient: dict | bytes

    :rtype: UserShopList
    """
    if connexion.request.is_json:
        ingredient = UserShopList.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_ingredient_for_user(ingredient):  # noqa: E501
    """Delete ingredient for user

     # noqa: E501

    :param ingredient: Ingredient that needs to be removed from this user&#39;s shoplist
    :type ingredient: dict | bytes

    :rtype: UserShopList
    """
    if connexion.request.is_json:
        ingredient = UserShopList.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_shop_list(user_id):  # noqa: E501
    """Get ingredients for user

     # noqa: E501

    :param user_id: The name that needs to be fetched. Use user1 for testing. 
    :type user_id: int

    :rtype: UserShopList
    """
    return 'do some magic!'


def updategredient_for_user(ingredient):  # noqa: E501
    """Modify user&#39;s ingredient

     # noqa: E501

    :param ingredient: Ingredient that needs to be modified on this user&#39;s shoplist
    :type ingredient: dict | bytes

    :rtype: UserShopList
    """
    if connexion.request.is_json:
        ingredient = UserShopList.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
