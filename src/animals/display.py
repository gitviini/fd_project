"""
* SHOW ANIMALS DATA
"""
from src.animals.manager import carregar_dados, salvar_dados

animals_db = carregar_dados() #Simular um "banco de dados"
proximo_id = max([int(i) for i in animals_db.keys()], default=0) + 1

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
              input("\nPressione Enter para continuar\n")

def show_menu_pesquisa_animais():
    while True:
        option = input(
"""--PESQUISAR ANIMAIS--
0) Voltar
1) Listar Todos os Animais
2) Listar por Nome
3) Listar por Ponto de apoio
4) Listar por Espécies
5) Listar por Raças
6) Listar por Idades
7) Listar por Personalidade
8) Listar por Histórico Médico
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
                    input("\nPressione Enter para continuar\n")
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
                        input("\nPressione Enter para continuar\n")
                        
            case "2":
                dados = carregar_dados()
                nomes =  set(animal.get("nome", "").capitalize() for animal in dados.values())

                if not nomes:
                    print("Nenhum animal cadastrado ainda.")
                    input("\nPressione Enter para continuar\n")
                    continue
                
                print("\n-- NOMES CADASTRADOS --")
                nomes = sorted(nomes)
                for i, nome in enumerate(nomes, 1):
                    print(f"{i}) {nome}")

                try:
                    escolha = int(input("Escolha uma opção (número do nome): "))
                    if 1 <= escolha <= len(nomes):
                        nome_escolhido = nomes[escolha - 1].lower()
                        encontrados = False
                        for id_animal, animal in dados.items():
                            if animal.get("nome", "").lower() == nome_escolhido:
                                print(f"\nID: {id_animal}")
                                print(f"Nome: {animal.get('nome', '')}")
                                print(f"Espécie: {animal.get('espécie', '')}")
                                print(f"Raça: {animal.get('raça', '')}")
                                print(f"Idade: {animal.get('idade', '')}")
                                print(f"Personalidade: {animal.get('personalidade', '')}")
                                print(f"Histórico Médico: {animal.get('histórico_medico', '')}")
                                encontrados = True
                                print("-" * 30)
                        print("\n")
                        if not encontrados:
                            print("Nenhum animal com esse nome foi encontrado.")
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
                    input("\nPressione Enter para continuar\n")

            case "3":
                print("Pendente!")

            case "4":
                dados = carregar_dados()
                especies = set(animal.get("espécie", "").capitalize() for animal in dados.values())

                if not especies:
                    print("Nenhuma espécie cadastrada ainda.")
                    input("\nPressione Enter para continuar\n")
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
                                print("-" * 30)
                        print("\n")
                        if not encontrados:
                            print("Nenhum animal dessa espécie foi encontrado.")
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
                    input("\nPressione Enter para continuar\n")

            case "5":
                dados = carregar_dados()
                racas = set(animal.get("raça", "").capitalize() for animal in dados.values())
                if not racas:
                    print("Nenhuma raça cadastrada ainda.")
                    input("\nPressione Enter para continuar\n")
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
                                print("-" * 30)
                        print("\n")
                        if not encontrados:
                            print("Nenhum animal encontrado para essa raça.")
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
                    input("\nPressione Enter para continuar\n")

            case "6":
                dados = carregar_dados()
                idades =  set(animal.get("idade", "").capitalize() for animal in dados.values())

                if not idades:
                    print("Nenhum animal cadastrado ainda.")
                    input("\nPressione Enter para continuar\n")
                    continue
                
                print("\n-- IDADES CADASTRADAS --")
                idades = sorted(idades)
                for i, idade in enumerate(idades, 1):
                    print(f"{i}) {idade}")

                try:
                    escolha = int(input("Escolha uma opção (número da idade): "))
                    if 1 <= escolha <= len(idades):
                        idade_escolhida = idades[escolha - 1].lower()
                        encontrados = False
                        for id_animal, animal in dados.items():
                            if animal.get("idade", "").lower() == idade_escolhida:
                                print(f"\nID: {id_animal}")
                                print(f"Nome: {animal.get('nome', '')}")
                                print(f"Espécie: {animal.get('espécie', '')}")
                                print(f"Raça: {animal.get('raça', '')}")
                                print(f"Idade: {animal.get('idade', '')}")
                                print(f"Personalidade: {animal.get('personalidade', '')}")
                                print(f"Histórico Médico: {animal.get('histórico_medico', '')}")
                                encontrados = True
                                print("-" * 30)
                        print("\n")
                        if not encontrados:
                            print("Nenhum animal dessa espécie foi encontrado.")
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
                    input("\nPressione Enter para continuar\n")
      
            case "7":
                dados = carregar_dados()
                personalidades =  set(animal.get("personalidade", "").capitalize() for animal in dados.values())

                if not personalidades:
                    print("Nenhum animal cadastrado ainda.")
                    input("\nPressione Enter para continuar\n")
                    continue
                
                print("\n-- PERSONALIDADES CADASTRADAS --")
                personalidades = sorted(personalidades)
                for i, personalidade in enumerate(personalidades, 1):
                    print(f"{i}) {personalidade}")

                try:
                    escolha = int(input("Escolha uma opção (número da personalidade): "))
                    if 1 <= escolha <= len(personalidades):
                        personalidade_escolhida = personalidades[escolha - 1].lower()
                        encontrados = False
                        for id_animal, animal in dados.items():
                            if animal.get("personalidade", "").lower() == personalidade_escolhida:
                                print(f"\nID: {id_animal}")
                                print(f"Nome: {animal.get('nome', '')}")
                                print(f"Espécie: {animal.get('espécie', '')}")
                                print(f"Raça: {animal.get('raça', '')}")
                                print(f"Idade: {animal.get('idade', '')}")
                                print(f"Personalidade: {animal.get('personalidade', '')}")
                                print(f"Histórico Médico: {animal.get('histórico_medico', '')}")
                                encontrados = True
                                print("-" * 30)
                        print("\n")
                        if not encontrados:
                            print("Nenhum animal com essa personalidade foi encontrado.")
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
                    input("\nPressione Enter para continuar\n")
            
            case "8":
                dados = carregar_dados()
                historicos =  set(animal.get("histórico_médico", "").capitalize() for animal in dados.values())

                if not historicos:
                    print("Nenhum animal cadastrado ainda.")
                    input("\nPressione Enter para continuar\n")
                    continue
                
                print("\n-- HISTÓRICOS MÉDICOS CADASTRADOS --")
                historicos = sorted(historicos)
                for i, historico in enumerate(historicos, 1):
                    print(f"{i}) {historico}")

                try:
                    escolha = int(input("Escolha uma opção (número da historico): "))
                    if 1 <= escolha <= len(historicos):
                        historico_escolhido = historicos[escolha - 1].lower()
                        encontrados = False
                        for id_animal, animal in dados.items():
                            if animal.get("histórico_médico", "").lower() == historico_escolhido:
                                print(f"\nID: {id_animal}")
                                print(f"Nome: {animal.get('nome', '')}")
                                print(f"Espécie: {animal.get('espécie', '')}")
                                print(f"Raça: {animal.get('raça', '')}")
                                print(f"Idade: {animal.get('idade', '')}")
                                print(f"Personalidade: {animal.get('personalidade', '')}")
                                print(f"Histórico Médico: {animal.get('histórico_medico', '')}")
                                encontrados = True
                                print("-" * 30)
                        print("\n")
                        if not encontrados:
                            print("Nenhum animal com essa personalidade foi encontrado.")
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
                    input("\nPressione Enter para continuar\n")

            case _:
                print("Opção inválida. Escolha entre (0 - 2)")
                input("\nPressione Enter para continuar\n")
            

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
                input("\nPressione Enter para continuar\n")     
            case _:
                print("Opção inválida.Escolha entre (0 - 1)")
                input("\nPressione Enter para continuar\n")

def show_menu_atualizar_animais():
   while True:
      option = input(
"""--ATUALIZAR ANIMAIS--
0) Voltar
1) Listar Animais Disponíveis
2) Atualizar por ID e Nome
3)
4)
:
"""
        ).strip()
      match (option):
            case "0":
                break
            case "1":
                dados = carregar_dados()
                if not dados:
                    print("Nenhum animal cadastrado ainda.")
                    input("\nPressione Enter para continuar\n")
                else:
                    print("-- Animais Cadastrados --")
                    for id_animal, dados in dados.items():
                        print(f"ID: {id_animal} - Nome: {dados["nome"]}")
                input("\nPressione Enter para continuar\n")
            
            case "2":
                dados = carregar_dados()
                if not dados:
                    print("Nenhum animal cadastrado ainda.")
                    input("\nPressione Enter para continuar\n")
                    continue

                id_animal =  input("Digite o ID do animal que deseja atualizar: ").strip()
                nome_animal = input("Digite o NOME do animal que deseja atualizar: ").strip().lower()

                if id_animal in dados:
                    nome_cadastrado = dados[id_animal]["nome"]
                    if nome_animal.lower() == nome_cadastrado.lower():
                        print("\nAnimal encontrado. Insira novos valores (enter para manter):")

                        especie_atual = dados[id_animal].get("espécie", "")
                        nova_especie = input(f"Espécie [{especie_atual}]: ").strip()
                        if nova_especie:
                            dados[id_animal]["espécie"] = nova_especie

                        raca_atual = dados[id_animal].get("raça", "")
                        nova_raca = input(f"Raça [{raca_atual}]: ").strip()
                        if nova_raca:
                            dados[id_animal]["raça"] = nova_raca

                        idade_atual = dados[id_animal].get("idade", "")
                        nova_idade = input(f"Idade [{idade_atual}]: ").strip()
                        if nova_idade:
                            dados[id_animal]["idade"] = nova_idade

                        personalidade_atual = dados[id_animal].get("personalidade", "")
                        nova_personalidade = input(f"Personalidade [{personalidade_atual}]: ").strip()
                        if nova_personalidade:
                            dados[id_animal]["personalidade"] = nova_personalidade

                        historico_atual = dados[id_animal].get("histórico_médico", "")
                        novo_historico = input(f"Histórico Médico [{historico_atual}]: ").strip()
                        if novo_historico:
                            dados[id_animal]["histórico-médico"] = novo_historico

                        salvar_dados(dados)
                        print("\n✅ Animal atualizado com sucesso.")
                    else:
                        print("Nome informado não confere com ID.")
                else:
                    print("ID não encontrado.")
                input("\nPressione Enter para continuar\n")

            case _:
                print("Opção inválida.Escolha entre (0 - 4)")
                input("\nPressione Enter para continuar\n")

def show_menu_deletar_animais():
   while True:
      option = input(
"""--DELETAR ANIMAIS--
0) Voltar
1) Listar Animais disponíveis
2) Deletar por ID
3)
4)
:
"""
        ).strip()
      match (option):
            case "0":
                break
            case "1":
                dados = carregar_dados()
                if not dados:
                    print("Nenhum animal cadastrado ainda.")
                    input("\nPressione Enter para continuar\n")
                else:
                    print("-- Animais Cadastrados --")
                for id_animal, dados in dados.items():
                    print(f"ID: {id_animal} - Nome: {dados["nome"]}")
                input("\nPressione Enter para continuar\n")
            case "2":
                dados = carregar_dados()
                if not dados:
                    print("Nenhum animal cadastrado ainda.")
                    input("\nPressione Enter para continuar\n")
                    continue
            
                id_animal = input("Digite o ID do animal a ser deletado: ").strip()
                nome_animal = input("Digite o NOME do animal a ser deletado: ").strip()

                if id_animal in dados:
                   nome_cadastrado = dados[id_animal]["nome"]
                   if nome_animal.lower() == nome_cadastrado.lower():
                      print("\nAnimal encontrado:")
                      for chave, valor in dados[id_animal].items():
                         print(f"{chave.capitalize()}: {valor}")

                      confirm = input("\nTem certeza que deseja deletar este animal (s/n)? ").strip().lower()
                      if confirm == "s":
                          if id_animal in dados:
                            del dados[id_animal]
                            salvar_dados(dados)
                            print("-" * 30)
                            print("\nAnimal deletado com sucesso.\n")
                            print("-" * 30)
                      else:
                            print("\nOperação Cancelada")
                   else:
                        print("Nome informado não confere com o ID.")
                else:
                    print("ID não encontrado.")
                    input("\nPressione Enter para continuar\n")

            case _:
                print("Opção inválida.Escolha entre (0 - 4)")
                input("\nPressione Enter para continuar\n")
