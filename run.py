"""
* RUN PROJECT
"""

from time import sleep
from src.utils.util import receive_user_input, clear
from src.users.display import new_user_dict, show_users
from src.users.manager import get_users, create_user
from src.utils.util import color

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
            while True:
                clear()
                print(color("- USUÁRIOS -", "green", "italic"))
                option_user = receive_user_input(
                    f"\n{color('0)VOLTAR', 'cyan')}\n{color('1)', 'cyan')}PESQUISAR\n{color('2)', 'cyan')}CRIAR\n{color('3)', 'cyan')}ATUALIZAR\n{color('4)', 'cyan')}DELETAR\n: "
                )
                match option_user:
                    case 0:
                        break
                    case 1:
                        while True:
                            clear()
                            print(color("- PESQUISA DE USUÁRIOS -", "green", "italic"))
                            options_filter_users = receive_user_input(
                                f"\n{color('0)VOLTAR','cyan')}\n{color('1)','cyan')}TODOS OS USUÁRIOS\n{color('2)','cyan')}POR ID\n{color('3)','cyan')}POR NOME\n{color('4)','cyan')}SE TRABALHA\n: "
                            )
                            match (options_filter_users):
                                case 0:
                                    break
                                case 1:
                                    show_users(get_users())
                                case 2:
                                    pass
                                case 3:
                                    pass
                                case 4:
                                    pass
                                case _:
                                    print(color("Opção inválida. Escolha entre (0 - 4).","red"))
                                    input(
                                        color(
                                            "\nPressione ⤶ Enter para continuar.",
                                            color="gray",
                                            style="italic",
                                        )
                                    )
                    case 2:
                        create_user(new_user_dict())
                    case 3:
                        pass
                    case 4:
                        pass
                    case _:
                        print(color("Opção inválida. Escolha entre (0 - 4).","red"))
                        input(
                            color(
                                "\nPressione ⤶ Enter para continuar.",
                                color="gray",
                                style="italic",
                            )
                        )
        case 1:
            # Animals
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
