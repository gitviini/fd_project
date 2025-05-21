"""
* SHOW USERS
"""

from src.utils.util import color, receive_user_input, clear


# * Read users
def show_users(users=dict) -> None:
    clear()

    # If users dict is empty, show alert
    (
        input(
            color(
                "Ainda não há usuários registrados.\n\nPressione ⤶ Enter para continuar.",
                color="gray",
                style="italic",
            )
        )
        if not len(list(users))
        else ()
    )

    # Show name and attributes of user
    for key, attributes in users.items():
        print(f"{color("id", "purple", "italic")}: {key}")
        # Show user's attributes
        for attribute, value in attributes.items():
            print(f"{color(attribute, "yellow")}: {value}")

    input(
        color(
            "\nPressione ⤶ Enter para continuar.",
            color="gray",
            style="italic",
        )
    )


# * Create users
def new_user_dict() -> dict:
    STEPS = {
        "name": {"text": "Digite seu nome: ", "type": "str"},
        "age": {"text": "Digite sua idade: ", "type": "int"},
        "personality": {
            "text": f"Descreva a personalidade\n{color("0)","cyan")}Extrovertido\n{color("1)","cyan")}Introvertido\n: ",
            "type": "int",
            "options": [0, 1],
        },
        "if_work": {
            "text": f"Trabalha?\n{color("0)","cyan")}SIm\n{color("1)","cyan")}NÃO\n: ",
            "type": "int",
            "options": [0, 1],
        },
        "workplace": {"text": f"Digite seu local de trabalho: ", "type": "str"},
    }

    dict_new_user = {}

    for step, question in STEPS.items():
        clear()
        if list(question).count("options"):
            while True:
                value = receive_user_input(question["text"], question["type"])
                if not (value in question["options"]):
                    print(
                        f"Valor {color(value, color="gray", style="italic")} é inválido. Tente novamente"
                    )
                    continue
                dict_new_user[step] = value
                break
        else:
            dict_new_user[step] = receive_user_input(question["text"], question["type"])

    return dict_new_user


# * Update user
def update_user() -> dict:
    pass


# * Delete user
def delete_user() -> dict:
    pass
