"""
* RUN PROJECT
"""

from time import sleep
from src.utils.util import receive_user_input, clear
from src.users.display import show_menu_users
from src.users.manager import get_users, create_user
from src.utils.util import color
from src.animals.display import show_menu_animals

run = True

TEMPLATE = f"""{color("- 🐾 ADOÇÃO DE ANIMAIS 🐾 -", "green", "italic")}

{color("0)", "cyan")}USUÁRIOS
{color("1)", "cyan")}ANIMAIS
{color("2)", "cyan")}PONTOS DE APOIO
{color("3)", "cyan")}SAIR
: """

clear()
while run:
    option = receive_user_input(TEMPLATE)
    match option:
        case 0:
            # Users
            show_menu_users()
        case 1:
            # Animals
            show_menu_animals()
            pass
        case 2:
            # Support Points
            pass
        case 3:
            # Back
            run = False
            print(color("Desligando...", color="red"))
            sleep(1)
        case _:
            # Another
            print(color("Opção inválida. Escolha entre (0 - 3).","red"))
            input(
                color(
                    "\nPressione ⤶ Enter para continuar.",
                    color="gray",
                    style="italic",
                )
            )
    clear()
