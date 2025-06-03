import json
import os

support_points = {}
next_id = 1
json_file = "jsons/support_points.json"


def load_data():
    global support_points, next_id
    if os.path.exists(json_file):
        with open(json_file, "r") as file:
            data = json.load(file)
            support_points.update({int(key): value for key, value in data.get("support_points", {}).items()})
            next_id = data.get("next_id", 1)


def save_data():
    with open(json_file, "w") as file:
        json.dump({
            "support_points": support_points,
            "next_id": next_id
        }, file, indent=4)