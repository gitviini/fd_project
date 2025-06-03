import json
from src.animals.manager import load_json, save_json
from src.utils.util import clear

def show_menu_animals():
    while True:
        clear()
        option = input(
"""--ANIMAIS--
0) Voltar
1) Pesquisar
2) Adicionar
3) Atualizar
4) Deletar
:"""
).strip()
        
        match (option):
            case "0":
              break
            case "1":
              show_menu_search_animals()
            case "2":
              show_menu_add()
            case "3": 
              show_menu_update_animals()
            case "4":
              show_menu_delet_animals()
            case _:
              print("Opção inválida. Escolha entre (0 - 4)")
              input("\nPressione Enter para continuar\n")

def list_animals():
    dados = load_json()
    if check_empty_data(dados):
        return
    for id_animal, animal in dados.items():
        show_animal(id_animal, animal)
        
def show_animal(id_animal, animal):
    print(f"\nID: {id_animal}")
    for chave, valor in animal.items():
        print(f"{chave.capitalize()}: {valor}")
    print("-" * 30)

def check_empty_data(dados):
    if not dados:
        print("Nenhum animal cadastrado ainda.")
        input("\nPressione Enter para continuar\n")
        return True
    return False

def search_animal_by_id_and_name(dados, id_animal, nome_animal):
    if id_animal in dados and dados[id_animal]['nome'].lower() == nome_animal.lower():
        return dados[id_animal]
    return None

def update_fields(animal):
    for chave in ["espécie", "raça", "idade", "personalidade"]:
        valor_atual = animal.get(chave, "")
        novo_valor = input(f"{chave.capitalize()} [{valor_atual}]: ").strip()
        if novo_valor:
            animal[chave] = novo_valor

def update_animal_support_point(id = "1", name_support_point = "bananinha") -> None | dict:
    animals = load_json()
    
    if not (id in animals.keys()):
        return None

    animals[id]["support_point"] = name_support_point

    save_json(animals)

    animals[id]["id"] = id

    return animals[id]

def show_menu_search_animals():
    clear()
    while True:
        option = input("""--PESQUISAR ANIMAIS--
0) Voltar
1) Listar Todos
2) Pesquisar por Nome
3) Pesquisar por Espécie
4) Pesquisar por Raça
5) Pesquisar por Support Point
6) Pesquisar por ID
7) Pesquisar por personalidade
:""").strip()

        match (option):
            case "0":
                break
            case "1":
                list_animals()
                input("\nPressione Enter para continuar\n")
            case "2" | "3" | "4" | "5" | "6" | "7":
                chave_map = {
                    "2": "nome",
                    "3": "espécie",
                    "4": "raça",
                    "5": "support_point",
                    "6": "id",
                    "7": "personalidade"
                }
                chave = chave_map[option]
                dados = load_json()

                if option != "6":
                    options = []
                    for option in dados.values():
                        if options.count(option[chave]) == 0:
                            options.append(option[chave])

                    print(options)

                valor = input(f"Digite o {chave.capitalize()}: ").strip()
                encontrado = False

                for id_animal, animal in dados.items():
                    if option == "6":
                        if id_animal == valor:
                            show_animal(id_animal, animal)
                            encontrado = True
                            break
                    else:
                        if valor.lower() in animal.get(chave, "").lower():
                            show_animal(id_animal, animal)
                            encontrado = True
                if not encontrado:
                    print("\nNenhum animal encontrado com esse critério.")
                    input("\nPressione Enter para continuar\n")
            case _:
                print("Opção inválida. Escolha entre (0 - 6)")
                input("\nPressione Enter para continuar\n")

def show_menu_add():
   while True:
        clear()
        option = input(
"""--ADICIONAR ANIMAIS--
0) Voltar
1) Adicionar Novo Animal
:"""
        ).strip()
        match (option):
          case "0":
            break
          case "1":
            dados = load_json()
            proximo_id = str(max(map(int, dados.keys()), default=0) + 1)
            novo_animal = {}
            for campo in ["nome", "espécie", "raça", "idade", "personalidade"]:
             novo_animal[campo] = input(f"{campo.capitalize()}: ").strip()
            dados[proximo_id] = novo_animal
            save_json(dados)
            print(f"\nAnimal cadastrado com sucesso! ID: {proximo_id}")
            input("\nPressione Enter para continuar\n")
                
def show_menu_update_animals():
   while True:
      clear()
      option = input(
"""--ATUALIZAR ANIMAIS--
0) Voltar
1) Listar Animais Disponíveis
2) Atualizar por ID e Nome
:"""
        ).strip()
      match (option):
         case "0":
                break
         case "1":
                list_animals()
                input("\nPressione Enter para continuar\n")
         case "2":
                dados = load_json()
                if check_empty_data(dados):
                  return

                list_animals()
                id_animal = input("Digite o ID do animal que deseja atualizar: ").strip()
                nome_animal = input("Digite o NOME do animal que deseja atualizar: ").strip().lower()

                animal = search_animal_by_id_and_name(dados, id_animal, nome_animal)
                if animal:
                    print("\nAnimal encontrado. Insira novos valores (enter para manter):")
                    update_fields(animal)
                    save_json(dados)
                    print("\nAnimal atualizado com sucesso.")
                else:
                     print("ID ou Nome inválidos.")

                input("\nPressione Enter para continuar\n")

         case _:
                print("Opção inválida. Escolha entre (0 - 2)")
                input("\nPressione Enter para continuar\n")

def show_menu_delet_animals():
   while True:
      clear()
      option = input(
"""--DELETAR ANIMAIS--
0) Voltar
1) Listar Animais disponíveis
2) Deletar por ID
:"""
        ).strip()
      match (option):
         case "0":
                break
         case "1":
                list_animals()
                input("\nPressione Enter para continuar\n")
         case "2":
                dados = load_json()
                if check_empty_data(dados):
                    continue
                id_animal = input("Digite o ID do animal a ser deletado: ").strip()
                nome_animal = input("Digite o NOME do animal a ser deletado: ").strip()

                if id_animal in dados:
                    nome_cadastrado = dados[id_animal]["nome"]
                    if nome_animal.lower() == nome_cadastrado.lower():
                        show_animal(id_animal, dados[id_animal])
                        confirm = input("\nTem certeza que deseja deletar este animal (s/n)? ").strip().lower()
                        if confirm == "s":
                            del dados[id_animal]
                            save_json(dados)
                            print("\nAnimal deletado com sucesso.\n")
                        elif confirm == "n":
                            print("Operação cancelada.")
                        else:
                            print("Opção inválida.")
                    else:
                        print("Nome informado não confere com ID.")
                else:
                    print("ID não encontrado.")
                input("\nPressione Enter para continuar\n")
         case _:
                print("Opção inválida. Escolha entre (0 - 2)")
                input("\nPressione Enter para continuar\n")
                