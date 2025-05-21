"""
* MANAGER USERS
"""

from src.utils.json_parser import json_for_dict, json_write

JSON_USER_PATH = "jsons/users.json"


# * READ USERS
def get_users(attribute_ref="", value_ref="") -> dict:
    users = json_for_dict(JSON_USER_PATH)
    if attribute_ref:
        filter_users = {}
        for id, user_dict in users.items():
            filter_users[id] = user_dict[attribute_ref] == value_ref
        users = filter_users
    return users


def create_user(dict_new_user=dict) -> None:
    json_users_length = len(list(json_for_dict(JSON_USER_PATH)))
    json_write(JSON_USER_PATH, {json_users_length : dict_new_user})
