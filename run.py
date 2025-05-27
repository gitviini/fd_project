"""
* RUN PROJECT 
"""

import json
import os
from src.users.manager import verify_users

support_points = {}
next_id = 0
json_file = "support_points.json"


def carregar_dados():
    global support_points, next_id
    if os.path.exists(json_file):
        with open(json_file, "r") as file:
            dados = json.load(file)
            support_points.update({int(key): value for key, value in dados.get("support_points", {}).items()})
            next_id = dados.get("next_id", 1)


def salvar_dados():
    with open(json_file, "w") as file:
        json.dump({
            "support_points": support_points,
            "next_id": next_id
        }, file, indent=4)


def criar_support_point():
    global next_id
    nome = input("Digite o nome do Ponto de Apoio que deseja adicionar: ")
    trabalhadores = {}
    animais = {}

    num_trabalhadores = int(input("Quantos trabalhadores deseja adicionar? "))
    for _ in range(num_trabalhadores):
        cpf_trab = input("Cpf do trabalhador: ")
        verify_user = verify_users(cpf_trab) # Se o usuário existir, retorna o dicionário dele, senão retorna None
        
        if(verify_user == None):
            print("Usuário não cadastrado. Cadastre-o primeiro.")
        else:
            trabalhadores[cpf_trab] = verify_user

        """ nome_trab = input("Nome do trabalhador: ")
        funcao = input("Função: ")
        trabalhadores[nome_trab] = funcao """

    num_animais = int(input("Quantos tipos de animais deseja adicionar? "))
    for id_animal in range(num_animais):
        tipo = input("Tipo do animal: ")
        quantidade = int(input("Quantidade: "))
        animais[id_animal] = {"tipo": tipo , "quantidade": quantidade}

    foto = input("Digite o caminho ou URL da foto do Ponto de Apoio: ")

    support_points[next_id] = {
        "nome": nome,
        "trabalhadores": trabalhadores,
        "animais": animais,
        "foto": foto
    }
    print(f"\nSupport point criado com ID {next_id}.")
    next_id += 1
    salvar_dados()  

def ler_support_points():
    print("Pesquisar por:\n1. Nome\n2. Mostrar todos os pontos")
    opcao = input("Escolha a opção (1/2): ")

    if opcao == "1":
        nome_busca = input("Digite o nome para buscar: ")
        encontrados = {id: sp for id, sp in support_points.items() if sp["nome"] == nome_busca}
    else:
        encontrados = support_points

    if not encontrados:
        print("Nenhum Ponto de Apoio encontrado.")
        return

    for id, sp in encontrados.items():
        print(f"\nID: {id}")
        print(f"Nome: {sp['nome']}")
        print(f"Trabalhadores: {sp['trabalhadores']}")
        print(f"Animais: {sp['animais']}")
        print(f"Foto: {sp['foto']}")

def atualizar_support_point():
    id_atualizar = int(input("Digite o ID do Ponto de Apoio a ser atualizado: "))
    nome_atual = input("Digite o nome atual do Ponto de Apoio: ")

    if id_atualizar in support_points and support_points[id_atualizar]['nome'] == nome_atual:
        novo_nome = input("Digite o novo nome: ")
        nova_foto = input("Digite o novo caminho/URL da foto: ")
        support_points[id_atualizar]['nome'] = novo_nome
        support_points[id_atualizar]['foto'] = nova_foto
        print("Ponto de Apoio atualizado com sucesso.")
        salvar_dados()  
    else:
        print("ID ou nome inválido.")

def deletar_support_point():
    id_deletar = int(input("Digite o ID do Ponto de Apoio a ser deletado: "))
    nome_confirma = input("Digite o nome do Ponto de Apoio: ")

    if id_deletar in support_points and support_points[id_deletar]['nome'] == nome_confirma:
        print("Informações do support point:")
        print(support_points[id_deletar])
        confirmar = input("Tem certeza que deseja deletar? (s/n): ")
        if confirmar.lower() == 's':
            del support_points[id_deletar]
            print("Ponto de Apoio deletado com sucesso.")
            salvar_dados() 
        else:
            print("Ação cancelada.")
    else:
        print("ID ou nome não encontrado.")

def menu():
    carregar_dados() 
    while True:
        print("\nMENU")
        print("1. Adicionar Ponto de Apoio")
        print("2. Listar Pontos de Apoio")
        print("3. Atualizar Ponto de Apoio")
        print("4. Deletar Ponto de Apoio")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_support_point()
        elif opcao == "2":
            ler_support_points()
        elif opcao == "3":
            atualizar_support_point()
        elif opcao == "4":
            deletar_support_point()
        elif opcao == "5":
            print("Encerrando")
            break
        else:
            print("Opção inválida.")


menu()