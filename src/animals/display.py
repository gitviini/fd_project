"""
* SHOW ANIMALS DATA
"""
from manager import carregar_dados, salvar_dados

animals_db = carregar_dados() #Simular um "banco de dados"
proximo_id = max([int(i) for i in animals_db.keys()], default=0) + 1

def show_menu_animals():
    while True:
        option = input(
"""--ANIMAIS--
0)Voltar
1)Pesquisar
2)Adicionar
3)Atualizar
4)Deletar
:"""        
          ).strip()
        
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
        option = input(
"""--PESQUISAR ANIMAIS--
0) Voltar
1) Listar todos os animais
2) Listar por espécies
3) LIstar por raças
:
"""
        ).strip()
        match option:
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
                        print(f"Nome: {animal.get('nome', '')}")
                        print(f"Espécie: {animal.get('espécie', '')}")
                        print(f"Raça: {animal.get('raça', '')}")
                        print(f"Idade: {animal.get('idade', '')}")
                        print(f"Personalidade: {animal.get('personalidade', '')}")
                        print(f"Histórico Médico: {animal.get('histórico_medico', '')}")
                input("Pressione Enter para continuar")

            case "2":
                dados = carregar_dados()
                especies = set(animal.get("espécie", "").capitalize() for animal in dados.values())

                if not especies:
                    print("Nenhuma espécie cadastrada ainda.")
                    input("Pressione Enter para continuar")
                    continue

                print("\n-- ESPÉCIES CADASTRADAS --")
                especies = sorted(especies)
                for i, especie in enumerate(especies, 1):
                    print(f"{i}) {especie}")

                try:
                    escolha = int(input("Escolha uma opção (número da espécie): "))
                    if 1 <= escolha <= len(especies):
                        especie_escolhida = especies[escolha - 1].lower()
                        encontrados = False
                        for id_animal, animal in dados.items():
                            if animal.get("espécie", "").lower() == especie_escolhida:
                                print(f"\nID: {id_animal}")
                                print(f"Nome: {animal.get('nome', '')}")
                                print(f"Espécie: {animal.get('espécie', '')}")
                                print(f"Raça: {animal.get('raça', '')}")
                                print(f"Idade: {animal.get('idade', '')}")
                                print(f"Personalidade: {animal.get('personalidade', '')}")
                                print(f"Histórico Médico: {animal.get('histórico_medico', '')}")
                                encontrados = True
                        if not encontrados:
                            print("Nenhum animal dessa espécie foi encontrado.")
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
                    input("Pressione Enter para continuar")
            case "3":
                dados = carregar_dados()
                racas = set(animal.get("raça", "").capitalize() for animal in dados.values())
                if not racas:
                    print("Nenhuma raça cadastrada ainda.")
                    input("Pressione Enter para continuar")
                    continue

                print("\n-- RAÇAS CADASTRADAS --")
                racas = sorted(racas)
                for i, raca in enumerate(racas, 1):
                    print(f"{i}) {raca}")

                try:
                    escolha = int(input("Escolha uma opção (número da raça): "))
                    if 1 <= escolha <= len(racas):
                        raca_escolhida = racas[escolha - 1].lower()
                        encontrados = False
                        for id_animal, animal in dados.items():
                            if animal.get("raça", "").lower() == raca_escolhida:
                                print(f"\nID: {id_animal}")
                                print(f"Nome: {animal.get('nome', '')}")
                                print(f"Espécie: {animal.get('espécie', '')}")
                                print(f"Raça: {animal.get('raça', '')}")
                                print(f"Idade: {animal.get('idade', '')}")
                                print(f"Personalidade: {animal.get('personalidade', '')}")
                                print(f"Histórico Médico: {animal.get('histórico_médico', '')}")
                                encontrados = True
                        if not encontrados:
                            print("Nenhum animal encontrado para essa raça.")
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
                    input("Pressione Enter para continuar")
            
            case _:
                print("Opção inválida. Escolha entre (0 - 2)")
                input("Pressione Enter para continuar")

def show_menu_adicionar():
   global proximo_id
   while True:
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
            nome = input("Nome: ")
            especie = input("Espécie: ")
            raca = input("Raça: ")
            idade = input("Idade: ")
            personalidade = input("Personalidade: ")
            historico_medico = input("Histórico Médico: ")
            print("-" * 30)

            #Criando o dicionário dos animais
            animal = {
               "nome": nome,
               "espécie": especie,
               "raça": raca,
               "idade": idade,
               "personalidade": personalidade,
               "histórico_médico": historico_medico,
            }

            #Armazenando no dicionário principal com o ID
            animals_db[str(proximo_id)] = animal
            salvar_dados(animals_db)
            print(f"\nAnimal cadastrado com sucesso! ID: {proximo_id}\n")
            proximo_id += 1
            input("Pressione Enter para continuar")

         case _:
            print("Opção inválida.Escolha entre (0 - 1)")
            input("Pressione Enter para continuar")

def show_menu_atualizar_animais():
   while True:
      option = input(
"""--ATUALIZAR ANIMAIS--
0)Voltar
1)
2)
3)
4)
:
"""
      ).strip()
      match (option):
         case "0":
            break
         case _:
            print("Opção inválida.Escolha entre (0 - 4)")
            input("Pressione Enter para continuar")

def show_menu_deletar_animais():
   while True:
      option = input(
"""--DELETAR ANIMAIS--
0)Voltar
1)
2)
3)
4)
:
"""
      ).strip()
      match (option):
         case "0":
            break
         case _:
            print("Opção inválida.Escolha entre (0 - 4)")
            input("Pressione Enter para continuar")

show_menu_animals()