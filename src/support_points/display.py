from src.users.display import update_user_workplace
from src.animals.display import atualizar_animal_support_point
from src.support_points.manager import next_id, support_points, load_data, save_data

def create_support_point():
    try:

        global next_id

        name = input("Digite o nome do Ponto de Apoio que deseja adicionar: ")
        workers = {}
        animals = {}

        num_workers = int(input("Quantos trabalhadores deseja adicionar? "))

        for _ in range(num_workers):
            while True:
                id_worker = input("Informe o ID do trabalhador:")
                if id_worker.lower() == 'sair':
                    break
                verify_user = update_user_workplace(id_worker, name)

                if(verify_user == None):
                    print("Usuário não cadastrado. Informe um ID existente ou digite 'sair' para sair: ")
                else:
                    workers[id_worker] = verify_user
                    print(f"Trabalhador {verify_user.get('name','')} adicionado com sucesso")
                    break
        num_animals = int(input("Quantos animais deseja adicionar? "))
        for _ in range( num_animals ):

            while True:
                id_animal= input("Informe o ID do animal:")
                if id_animal.lower() == 'sair':
                    return
                verify_animal= atualizar_animal_support_point(id_animal, name)

                if(verify_animal == None):
                    print("Animal não cadastrado. Informe um ID existente ou digite 'sair' para sair.")
                else:
                    animals[(id_animal)] = verify_animal
                    print(f"Animal {verify_animal.get('name','')} adicionado com sucesso")
                    break
        support_points[next_id] = {
            "name": name,
            "workers": workers,
            "animals": animals
        }
        print(f"\nPonto de Apoio criado com ID {next_id}.")
        next_id += 1
        save_data()
    except Exception:
        print("Valor inválido. Tente novamente")

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
            for key, value in data.items():
                print(f"  {key.capitalize()}: {value}")
    else:
        print("Nenhum trabalhador registrado.")

    print("Animais:")
    if sp['animals']:
        for id_animal, data_animals in sp['animals'].items():
            for key, value in data_animals.items():
                print(f"  {key.capitalize()}: {value}")
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
            for id_user in support_points[id_delete]["workers"].keys():
                update_user_workplace(id_user,"")
            for id_animal in support_points[id_delete]["animals"].keys():
                update_user_workplace(id_animal,"")
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
