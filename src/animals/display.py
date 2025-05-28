"""
* SHOW ANIMALS DATA
"""
from manager import carregar_dados, salvar_dados

animals_db = carregar_dados() #Simular um "banco de dados"
proximo_id = max([int(i) for i in animals_db.keys()], default=0) + 1

def show_menu_animals():
    while True:
        option = str(input(
"""--ANIMAIS--
0)Voltar
1)Pesquisar
2)Adicionar
3)Atualizar
4)Deletar
:"""        
          ))
        
        match (option):
            case "0":
              break
            case "1":
              #pesquisar
              show_menu_pesquisa_animais()
            case "2":
              #adicionar
              show_menu_adicionar()
            case "3": 
              #atualizar
              show_menu_atualizar_animais()
            case "4":
              #deletar
              show_menu_deletar_animais()
            case _:
              print("Opção inválida.Escolha entre (0 - 4)")
              input("Pressione Enter para continuar")

def show_menu_pesquisa_animais():
   while True:
      option = str(input(
"""--PESQUISAR ANIMAIS--
0) Voltar
1) Listar todos os animais
2)
3)
4)
:
"""
     ))
      match (option):
         case "0":
            break
         case "1":
            dados = carregar_dados()
            if not dados:
               print("Nenhum animal cadastrado ainda.")
            else:
               print("\n-- Lista de Animais Cadastrados --")
               for id_animal, animal in dados.items():
                  print(f"\nID: {id_animal}")
                  print(f"Nome: {dados['nome']}")
                  print(f"Espécie: {dados['espécie']}")
            input("Pressione Enter para continuar")

         case _:
            print("Opção inválida.Escolha entre (0 - 4)")
            input("Pressione Enter para continuar")

def show_menu_adicionar():
   global proximo_id
   while True:
      option = str(input(
"""--ADICIONAR ANIMAIS--
0) Voltar
1) Adcionar Novo Animal
2)
3)
4)
:
"""
      ))
      match (option):
         case "0":
            break
         case "1":
            nome = input("Nome: ")
            especie = input("Espécie: ")
            print("-" * 30)

            #Criando o dicionário dos animais
            animal = {
               "nome": nome,
               "espécie": especie
            }

            #Armazenando no dicionário principal com o ID
            salvar_dados(animals_db)
            print(f"\nAnimal cadastrado com sucesso! ID: {proximo_id}\n")
            proximo_id += 1
            input("Pressione Enter para continuar")

         case _:
            print("Opção inválida.Escolha entre (0 - 4)")
            input("Pressione Enter para continuar")

def show_menu_atualizar_animais():
   while True:
      option = str(input(
"""--ATUALIZAR ANIMAIS--
0)Voltar
1)
2)
3)
4)
:
"""
      ))
      match (option):
         case "0":
            break
         case _:
            print("Opção inválida.Escolha entre (0 - 4)")
            input("Pressione Enter para continuar")

def show_menu_deletar_animais():
   while True:
      option = str(input(
"""--DELETAR ANIMAIS--
0)Voltar
1)
2)
3)
4)
:
"""
      ))
      match (option):
         case "0":
            break
         case _:
            print("Opção inválida.Escolha entre (0 - 4)")
            input("Pressione Enter para continuar")

show_menu_animals()