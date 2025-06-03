import json

def update_user_workplace(id, name_workplace) -> None | dict:
    users = {}
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)

    if not (id in users.keys()):
        return None

    users[id]["workplace"] = name_workplace

    with open("users.json", "w") as file:
        json.dump(users, file)

    return users[id]