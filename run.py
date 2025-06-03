
from time import sleep
from src.utils.util import clear
from src.users.display import show_users_menu
from src.animals.display import show_menu_animals
from src.support_points.display import show_menu_support_points

run = True


TEMPLATE = f"""- 🐾 ADOÇÃO DE ANIMAIS 🐾 -

0)USUÁRIOS
1)ANIMAIS
2)PONTOS DE APOIO
3)SAIR
: """

clear()
while run:
    option = input(TEMPLATE)
    match option:
        case "0":
            show_users_menu()
        case "1":
            show_menu_animals()
        case "2":
            show_menu_support_points()
        case "3":
            run = False
            print("Desligando...")
            sleep(1)
        case _:
            print("\nOpção inválida. Escolha entre (0 - 3).")
            input("\nPressione ⤶ Enter para continuar.")
    
    clear()
