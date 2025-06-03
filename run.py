from time import sleep
from src.utils.util import receive_user_input, clear
from src.users.display import show_menu_users
from src.users.manager import get_users, create_user
from src.animals.display import show_menu_animals

run = True

TEMPLATE = f"""🐾 ADOÇÃO DE ANIMAIS 🐾
0)USUÁRIOS
1)ANIMAIS
2)PONTOS DE APOIO
3)SAIR
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
            print("Desligando...")
            sleep(1)
        case _:
            # Another
            print("Opção inválida. Escolha entre (0 - 3).")
            input("\nPressione ⤶ Enter para continuar.",)
    clear()
