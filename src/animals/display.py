"""
* SHOW ANIMALS DATA
"""
from src.animals.manager import carregar_dados, salvar_dados
import os

def show_menu_animals():
    while True:
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
              show_menu_pesquisa_animais()
            case "2":
              show_menu_adicionar()
            case "3": 
              show_menu_atualizar_animais()
            case "4":
              show_menu_deletar_animais()
            case _:
              print("Opção inválida. Escolha entre (0 - 4)")
              input("\nPressione Enter para continuar\n")

def listar_animais():
    dados = carregar_dados()
    if verificar_dados_vazios(dados):
        return  # ou pass
    for id_animal, animal in dados.items():
        exibir_animal(id_animal, animal)
        
def exibir_animal(id_animal, animal):
    print(f"\nID: {id_animal}")
    for chave, valor in animal.items():
        print(f"{chave.capitalize()}: {valor}")
    print("-" * 30)

def verificar_dados_vazios(dados):
    if not dados:
        print("Nenhum animal cadastrado ainda.")
        input("\nPressione Enter para continuar\n")
        return True
    return False

def buscar_animal_por_id_e_nome(dados, id_animal, nome_animal):
    if id_animal in dados and dados[id_animal]['nome'].lower() == nome_animal.lower():
        return dados[id_animal]
    return None

def atualizar_campos(animal):
    for chave in ["espécie", "raça", "idade", "personalidade", "histórico_médico"]:
        valor_atual = animal.get(chave, "")
        novo_valor = input(f"{chave.capitalize()} [{valor_atual}]: ").strip()
        if novo_valor:
            animal[chave] = novo_valor

def show_menu_pesquisa_animais():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        option = input("""--PESQUISAR ANIMAIS--
0) Voltar
1) Listar Todos
2) Pesquisar por Nome
3) Pesquisar por Espécie
4) Pesquisar por Raça
5) Pesquisar por Pontos de apoio
6) Pesquisar por ID
: """).strip()

        match (option):
            case "0":
                break
            case "1":
                listar_animais()
                input("\nPressione Enter para continuar\n")
            case "2" | "3" | "4" | "5" | "6":
                chave_map = {
                    "2": "nome",
                    "3": "espécie",
                    "4": "raça",
                    "5": "pontos de apoio",
                    "6": "id"
                }
                chave = chave_map[option]
                valor = input(f"Digite o {chave.capitalize()}: ").strip()
                dados = carregar_dados()
                encontrado = False
                for id_animal, animal in dados.items():
                    if option == "6":
                        if id_animal == valor:
                            exibir_animal(id_animal, animal)
                            encontrado = True
                            break
                    else:
                        if valor.lower() in animal.get(chave, "").lower():
                            exibir_animal(id_animal, animal)
                            encontrado = True
                if not encontrado:
                    print("\nNenhum animal encontrado com esse critério.")
                input("\nPressione Enter para continuar\n")
            case _:
                print("Opção inválida. Escolha entre (0 - 6)")
                input("\nPressione Enter para continuar\n")

def show_menu_adicionar():
   while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        option = input(
"""--ADICIONAR ANIMAIS--
0) Voltar
1) Adicionar Novo Animal
:
"""
        ).strip()
        match (option):
          case "0":
            break
          case "1":
            dados = carregar_dados()
            proximo_id = str(max(map(int, dados.keys()), default=0) + 1)
            novo_animal = {}
            for campo in ["nome", "espécie", "raça", "idade", "personalidade", "histórico_médico"]:
             novo_animal[campo] = input(f"{campo.capitalize()}: ").strip()
            dados[proximo_id] = novo_animal
            salvar_dados(dados)
            print(f"\nAnimal cadastrado com sucesso! ID: {proximo_id}")
            input("\nPressione Enter para continuar\n")
                
def show_menu_atualizar_animais():
   while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      option = input(
"""--ATUALIZAR ANIMAIS--
0) Voltar
1) Listar Animais Disponíveis
2) Atualizar por ID e Nome
:
"""
        ).strip()
      match (option):
         case "0":
                break
         case "1":
                listar_animais()
                input("\nPressione Enter para continuar\n")
         case "2":
                dados = carregar_dados()
                if verificar_dados_vazios(dados):
                  return

                listar_animais()
                id_animal = input("Digite o ID do animal que deseja atualizar: ").strip()
                nome_animal = input("Digite o NOME do animal que deseja atualizar: ").strip().lower()

                animal = buscar_animal_por_id_e_nome(dados, id_animal, nome_animal)
                if animal:
                    print("\nAnimal encontrado. Insira novos valores (enter para manter):")
                    atualizar_campos(animal)
                    salvar_dados(dados)
                    print("\nAnimal atualizado com sucesso.")
                else:
                     print("ID ou Nome inválidos.")

                input("\nPressione Enter para continuar\n")

         case _:
                print("Opção inválida. Escolha entre (0 - 2)")
                input("\nPressione Enter para continuar\n")

def show_menu_deletar_animais():
   while True:
      os.system('cls' if os.name == 'nt' else 'clear')
      option = input(
"""--DELETAR ANIMAIS--
0) Voltar
1) Listar Animais disponíveis
2) Deletar por ID
:
"""
        ).strip()
      match (option):
         case "0":
                break
         case "1":
                listar_animais()
                input("\nPressione Enter para continuar\n")
         case "2":
                dados = carregar_dados()
                if verificar_dados_vazios(dados):
                    continue
                id_animal = input("Digite o ID do animal a ser deletado: ").strip()
                nome_animal = input("Digite o NOME do animal a ser deletado: ").strip()

                if id_animal in dados:
                    nome_cadastrado = dados[id_animal]["nome"]
                    if nome_animal.lower() == nome_cadastrado.lower():
                        exibir_animal(id_animal, dados[id_animal])
                        confirm = input("\nTem certeza que deseja deletar este animal (s/n)? ").strip().lower()
                        if confirm == "s":
                            del dados[id_animal]
                            salvar_dados(dados)
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
                
show_menu_animals()