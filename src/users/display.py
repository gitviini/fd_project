import re
from src.users.manager import load_json, save_json

all_users = {}

def update_user_workplace(id, workplace_name):
    users = load_json()

    if not (id in users.keys()):
        return None
    
    users[id]["workplace"] = workplace_name
    save_json(users)

    users[id]["id"] = id

    return(users[id])

def user_search():
    print("\n--- PESQUISAR USUÁRIO ---")
    search_name = input("Digite o nome completo do usuário: ").strip().title()

    users = load_json()
    found = {}

    for id, user in users.items():
        if search_name in user["name"]:
            found[id] = user

    if found:
        print("\nUsuários encontrados: \n")
        for id, user in found.items():
            print(f"{id}. Nome: {user['name']}")
            print(f"Contato: {user['contact']}")
            print(f"CPF: {user['cpf']}")
            print("\n")

    else:
        print("Nenhum usuário encontrado.")
        print("\nAperte enter para retornar")
        
    return found        
       
def cpf_validate(user_data):
    while True:
            cpf = input("CPF (somente números): ").strip()

            if not cpf.isdigit():
                print("CPF inválido. Insira apenas números.")
                continue
            
            if len(cpf) != 11:
                print("Número de CPF inválido. Verifique se possui 11 dígitos.")
                continue

            formatted_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

            for user in user_data.values():
                if user.get('cpf', "") == formatted_cpf:
                    print("Já existe um usuário cadastrado sob esse CPF.")
                    input("Aperte enter para retornar.")
                    return

            return formatted_cpf            

def contact_validate():
    while True:
        contact = input("Celular (DDD + Número): ").strip()
                
        if len(contact) != 11:
            print("Número de celular inválido. Verifique se possui 11 dígitos.")

        if not contact.isdigit():
            print("Número de celular incorreto. O celular deve conter 11 dígitos (DDD + número)..")
            input("Aperte enter para tentar novamente")
            continue

        formated_contact = f"{contact[:2]}.{contact[2:3]}.{contact[3:7]}-{contact[7:]}"
        return formated_contact
        
def name_validate(user_data):    
    while True:
        name = input("Insira o nome do usuário: ").strip()

        if not name:
            print("O nome não pode estar vazio.")
            continue

        if not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+",name):
            print("O nome deve conter apenas letras e espaços. \nTente novamente.")
            continue

        for user in user_data.values():
            if user['name'] == name:
                print("Já existe um usuário cadastrado sob esse nome")
                print("Tente novamente.")
                break

        else:
            return name.title()

def personality_validate():
    while True:
        print("Informe a personalidade do usuário: ")
        print("1) INTROVERTIDO(A)")
        print("2) EXTROVERTIDO(A)")

        try:
            option = int(input("OPÇÃO: "))

        except ValueError:
            print("Opção inválida. Pressione '1' ou '2'")
            break

        if option == 1:
            return "Introvertido(a)"
        
        elif option == 2:
            return "Extrovertido(a)"
        
        else:
            print("Opção inválida.\nTente novamente.")
            break

def user_register():
    print("\n--- CADASTRAR NOVO USUÁRIO ---")

    all_users = load_json()

    if all_users:
        numeros_existentes = []
        for key in all_users.keys():
            numeros_existentes.append(int(key))
        next_user_id = len(numeros_existentes) + 1

    else:
        next_user_id = 1


    name = name_validate(all_users)
    contact = contact_validate()
    cpf = cpf_validate(all_users)
    personality = personality_validate()

    new_user_key = f"{next_user_id}"

    all_users[new_user_key] = {
        'name': name,
        'contact': contact,
        'cpf': cpf,
        'personality': personality,
        'workplace': ""
    }
    
    next_user_id += 1
    save_json(all_users)

    print("Cliente cadastrado com sucesso!")

def user_update(user_data):
    print("\n--- ATUALIZAR USUÁRIO ---")

    name_search = input("Informe o nome completo do usuário que deseja alterar: ")

    for user in user_data.values():
        if user['name'] == name_search:
            print(f"Informe a seguir qual dado deseja alterar do usuário: {user['name']}")
            print("1)NOME")
            print("2)CPF")
            print("3)CONTATO")
            print("4)PERSONALIDADE")
            print("5)CANCELAR OPERAÇÃO")

            try:
                option = int(input("OPÇÃO: "))
            except ValueError:
                print("Opção inválida. Tente novamente. . .")
                break
        
            match option:
                case 1:
                    print("--- ATUALIZAÇÃO DE NOME DE USUÁRIO ---")
                    cancel = input("Pressione Enter para continuar ou 0 para cancelar. ")

                    if cancel == '0':
                        print("OPERAÇÃO CANCELADA: ")
                        print("\nNenhuma alteração feita.")
                        print("Retornando ao menu anterior: ")
                        return

                    new_user_name = name_validate(user_data)
                    user['name'] = new_user_name 
                    save_json(user_data)
                    print(f"Usuário atualizado com sucesso: {new_user_name}!")
                    print("\nAperte enter para retornar")
                    return
                

                case 2:
                    print("--- ATUALIZAÇÃO DE CPF DE USUÁRIO ---")
                    cancel = input("Pressione Enter para continuar ou 0 para cancelar. ")

                    if cancel == '0':
                        print("OPERAÇÃO CANCELADA")
                        print("\nNenhuma alteração feita.")
                        print("Retornando ao menu anterior")
                        return
                    
                    user_new_cpf = cpf_validate(user_data)
                    old_cpf = user['cpf']
                    user['cpf'] = user_new_cpf                    
                    save_json(user_data)
                    print(f"CPF alterado de {old_cpf} para {user_new_cpf} com sucesso!")
                    input("\nAperte enter para retornar")
                    return

                case 3:
                    print("--- ATUALIZAÇÃO DE CONTATO DE USUÁRIO ---")
                    cancel = input("Pressione Enter para continuar ou 0 para cancelar. ")

                    if cancel == '0':
                        print("OPERAÇÃO CANCELADA")
                        print("\nNenhuma alteração feita.")
                        print("Retornando ao menu anterior")
                        return
                    
                    user_new_contact = contact_validate()  
                    user['contact'] = user_new_contact
                    save_json(user_data)                                        
                    print(f"Contato alterado de {user['contact']} para {user_new_contact} com sucesso!")
                    input("\nAperte enter para retornar ")
                    return                                        

                case 4:
                    print("--- ATUALIZAÇÃO DE PERSONALIDADE DE USUÁRIO ---")
                    cancel = input("Pressione Enter para continuar ou 0 para cancelar. ")


                    if cancel == '0':
                        print("OPERAÇÃO CANCELADA")
                        print("Nenhuma alteração feita.")
                        print("Retornando ao menu anterior")
                        return
                    
                    personality = personality_validate()
                    user['personality'] = personality
                    save_json(user_data)
                    print(f"Personalidade atualizada com sucesso para {personality}!")
                    return

                
                case 5:
                    print("OPERAÇÃO CANCELADA\nRetornando ao menu . . .")
                    return
                
                case _:
                    print("Opção inválida.")
                    return

def user_delet():
    print("\n--- DELETAR USUÁRIO ---")

    users = load_json()

    while True:
        try:
            user_search()
            index = input("\nDigite o índice que deseja deletar ou 0 para cancelar: ").strip()

            if index == '0':
                print("Operação cancelada. \nNenhum usuário foi deletado.")
                print("Aperte enter para retornar")
                break

            if int(index) >= 1 and index in users.keys():
                user_to_delete = users[index]

                print("\nTem certeza que deseja deletar: ")
                print(f"NOME: {user_to_delete['name']}")
                print(f"CPF: {user_to_delete['cpf']}")
                print(f"CONTATO: {user_to_delete['contact']}")
                confirm = input("OPÇÃO (S/N): ").lower().strip()

                if confirm == 's':
                    users.pop(index)
                    save_json(users)
                    print(f"Usuário(s) {user_to_delete['name']} deletado com sucesso")
                    input("Pressione Enter para retornar ao menu")
                    return
                else:
                    print("--- OPERAÇÃO CANCELADA ---")
                    print("Nenhum usuário deletado.\nRetornando ao menu")
                    return
            else:
                print(f"Opção inválida. Digite um id válido.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def show_users_menu():
    while True:
        print("--- MENU ---")
        print("0)PESQUISAR USUÁRIO")
        print("1)CADASTRAR USUÁRIO")
        print("2)ATUALIZAR USUÁRIO")
        print("3)DELETAR USUÁRIO")
        print("4)VOLTAR AO MENU PRINCIPAL")
        try:
            option = int(input("OPÇÃO: "))
        except ValueError:
            return
        
        match(option):
            case 0:
               user_search()
            case 1:
                user_register()
            case 2:
                user_data = load_json()
                user_update(user_data)
            case 3:
                user_delet()
            case 4:
                print("Retornando ao menu principal")
                break         
            case _:
                print("Opção inválida. \nTente novamente.")
                print("Aperte enter para retornar")