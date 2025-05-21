"""
* JSON PARSER (JSON -> DICT || DICT -> JSON)
"""

import json


def json_write(path=str, json_new_content=dict) -> None:
    try:
        json_content = {}
        with open(path) as file:
            json_content = json.load(file)

        for key, value in json_new_content.items():
            json_content[key] = value

        with open(path, "w") as file:
            json.dump(json_content, file)
    except FileNotFoundError as e:
        print(f"Arquivo {e.filename} não existe. Tente novamente.")
    except Exception:
        print("Ops!😬 Houve um erro. Tente novamente.")


def json_for_dict(path=str) -> dict:
    try:
        with open(path) as file:
            return json.load(file)
    except FileNotFoundError as e:
        print(f"Arquivo {e.filename} não existe. Tente novamente.")
    except Exception:
        print("Ops!😬 Houve um erro. Tente novamente.")
