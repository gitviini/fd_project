import json

def atualizar_animal_support_point(id, name_support_point ) -> None | dict:
    animals = {}
    with open("animals.json", "r", encoding="utf-8") as file:
        animals = json.load(file)

    if not (id in animals.keys()):
        return None

    animals[id]["support_point"] = name_support_point

    with open("animals.json", "w") as file:
        json.dump(animals, file)

    return animals[id]