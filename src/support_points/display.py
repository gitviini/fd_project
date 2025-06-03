import json
import os
from src.users.manager import verify_users

support_points = {}
next_id = 1
json_file = "support_points.json"


def load_data():
    global support_points, next_id
    if os.path.exists(json_file):
        with open(json_file, "r") as file:
            data = json.load(file)
            support_points.update({int(key): value for key, value in data.get("support_points", {}).items()})
            next_id = data.get("next_id", 1)


def save_data():
    with open(json_file, "w") as file:
        json.dump({
            "support_points": support_points,
            "next_id": next_id
        }, file, indent=4)


def create_support_point():
    global next_id

    name = input("Digite o nome do Ponto de Apoio que deseja adicionar: ")
    workers = {}
    animals = {}

    num_workers = int(input("Quantos trabalhadores deseja adicionar? "))
    for _ in range(num_workers):
        id_worker = input("Informe o ID do trabalhador:")
        verify_user = verify_users(id_worker)    #Falta fazer pegar e mostrar as infos dos usuarios
        
        if(verify_user == None):
            print("Usuário não cadastrado. Cadastre-o primeiro.")
        else:
            worker = {
                "worker_name": verify_user.get,
                "worker_function": verify_user.get        #Testar isso aqui
            }
            workers[id_worker] = worker


    num_animals = int(input("Quantos animais deseja adicionar? "))
    for id_animal in range(1, num_animals + 1):
        id = input("Informe o ID do animal:")
    
        animal = {
            "id": id   #Falta fazer pegar e mostrar as infos dos animais 
        }  
         
        animals[str(id_animal)] = animal  


    support_points[next_id] = {
        "nome": name,
        "trabalhadores": workers,    # Aqui tem q fazer mostrar as infos tbm 
        "animais": animals
    }
    print(f"\nSupport point criado com ID {next_id}.")
    next_id += 1
    save_data()  

def read_support_points():
    print("Pesquisar por:\n1. Nome\n2. Mostrar todos os pontos")
    option = input("Escolha a opção (1/2): ")

    if option == "1":
        name_search = input("Digite o nome para buscar: ")
        found = {id: sp for id, sp in support_points.items() if sp['name'] == name_search}
    else:
        found = support_points

    if not found:
        print("Nenhum Ponto de Apoio encontrado.")
        return

    for id, sp in found.items():
        print(f"\nID: {id}")
        print(f"Nome: {sp['name']}")

        print("Trabalhadores:")
    if sp['workers']:
        for id, data in sp['workers'].items():
            print(f"ID: {id}")
            for key, value in data.items():
                print(f"{key.capitalize()}: {value}")
    else:
        print("  Nenhum trabalhador registrado.")

    print("Animais:")
    if sp['animals']:
        for id_animal, data_animals in sp['animals'].items():
            print(f"\nAnimal {id_animal}:")
            for key, value in data_animals.items():
                print(f"{key.capitalize()}: {value}")
    else:
        print("Nenhum animal registrado.")

def update_support_point():
    id_update = int(input("Digite o ID do Ponto de Apoio a ser atualizado: "))
    current_name = input("Digite o nome atual do Ponto de Apoio: ")

    if id_update in support_points and support_points[id_update]['name'] == current_name:
        new_name = input("Digite o novo nome: ")
        support_points[id_update]['name'] = new_name
        print("Ponto de Apoio atualizado com sucesso.")
        save_data()  
    else:
        print("ID ou nome inválido.")

def delete_support_point():
    id_delete = int(input("Digite o ID do Ponto de Apoio a ser deletado: "))
    confirm_name = input("Digite o nome do Ponto de Apoio: ")

    if id_delete in support_points and support_points[id_delete]['name'] == confirm_name:
        print("Informações do support point:")
        print(support_points[id_delete])
        confirm = input("Tem certeza que deseja deletar? (s/n): ")
        if confirm.lower() == 's':
            del support_points[id_delete]
            print("Ponto de Apoio deletado com sucesso.")
            save_data() 
        else:
            print("Ação cancelada.")
    else:
        print("ID ou nome não encontrado.")

def menu():
    load_data() 
    while True:
        print("\nMENU")
        print("1. Adicionar Ponto de Apoio")
        print("2. Listar Pontos de Apoio")
        print("3. Atualizar Ponto de Apoio")
        print("4. Deletar Ponto de Apoio")
        print("5. Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            create_support_point()
        elif option == "2":
            read_support_points()
        elif option == "3":
            update_support_point()
        elif option == "4":
            delete_support_point()
        elif option == "5":
            print("Encerrando")
            break
        else:
            print("Opção inválida.")
