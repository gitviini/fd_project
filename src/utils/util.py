import os
from typing import Literal
from src.utils.constants import COLORS, STYLES


def clear():
    match (os.name):
        case "posix":
            # for linux
            os.system("clear")
        case "nt":
            # for windows
            os.system("cls")
        case _:
            # for anyone
            os.system("clear")


def receive_user_input(
    text="", output_type: Literal["int", "str"] = "int"
) -> int | str:
    response = ""
    while True:
        try:
            response = int(input(text)) if output_type == "int" else input(text)
            break
        except ValueError:
            print(color("Valor inválido. Tente novamente.", "red"))
            input(
                color(
                    "\nPressione ⤶ Enter para continuar.",
                    color="gray",
                    style="italic",
                )
            )
        except Exception:
            print("Ops!😬 Houve um erro. Tente novamente.")
    return response


def color(
    text=str,
    color: Literal[
        "normal", "cyan", "red", "green", "yellow", "pink", "purple", "gray"
    ] = "normal",
    style: Literal["normal", "italic", "bold"] = "normal",
) -> str:
    try:
        return f"\x1b[{STYLES[style]};{COLORS[color]}m{text}\x1b[m"
    except KeyError:
        print(color("Valor inválido. Tente novamente.", "red"))
        input(
            color(
                "\nPressione ⤶ Enter para continuar.",
                color="gray",
                style="italic",
            )
        )
    except Exception:
        print("Ops!😬 Houve um erro. Tente novamente.")
