import json

archive = "jsons/users.json"

def load_json():
    with open(archive, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(user_data):
    with open(archive, 'w', encoding='utf-8') as f:
        json.dump(user_data, f, indent=4, ensure_ascii=False)
