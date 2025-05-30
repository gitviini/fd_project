import json
import os

parent_dir = os.path.dirname(os.path.dirname(__file__))
archive = os.path.join(parent_dir, 'json', 'users.json')

def load_json():
    with open(archive, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(user_data):
    with open(archive, 'w', encoding='utf-8') as f:
        json.dump(user_data, f, indent=4, ensure_ascii=False)

def user_search():
    print("\n--- PESQUISAR USUÁRIO ---")
    search_name = input("Digite o nome completo do usuário: ").strip().title()

    users = load_json()
    found = []

    for user in users:
        if search_name in user["name"]:
            found.append(user)

    if found:
        print("\nUsuários encontrados: \n")
        for i, user in enumerate(found, 1):
            print(f"{i}. Nome: {user['name']}")
            print(f"Contato: {user['contact']}")
            print(f"CPF: {user['cpf']}")
            print("\n")

    else:
        print("Nenhum usuário encontrado.")
        print("\nAperte enter para retornar >>>")
        
    return found        
       
def cpf_validate():
    user_data = load_json()
    while True:
        try:
            cpf = input("CPF (somente números): ").strip()

            if (int(cpf)):
                return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            
            elif user["cpf"]:
                for user in user_data:
                    print("Já existe um usuário cadastrado sob esse CPF.")
                    input("Aperte enter para retornar.")
                    break

            elif len(cpf) != 11:
                print("Número de CPF inválido. Verifique se possui 11 dígitos.")
                return
            else:
                raise Exception("Cpf inválido. Tente novamente")
            
        except Exception:
            print("Valor inválido. Tente novamente.")
            input("Aperte enter para retornar.")

def contact_validate():
    while True:
        try:
            contact = input("Celular (DDD + Número): ").strip()

            
            if (contact[2] == "." and contact[3] == "." and contact[7] == "-"):
                return contact
            
            elif len(contact) != 11:
                print("Número de celular inválido. Verifique se possui 11 dígitos.")

            elif(int(contact)):
                return f"{contact[:2]}.{contact[2:3]}.{contact[3:7]}-{contact[7:]}"

            else:
                raise Exception("Número de celular incorreto. O celular deve conter 11 dígitos (DDD + número). \nDigite novamente.")
        
        except Exception:
            print("Valor inválido. Tente novamente.")
            input("Aperte enter para tentar novamente >>> ")

def name_validate():
    user_data = load_json()
    
    while True:
        name = input("Insira o nome do usuário: ").strip()

        if not name:
            raise ValueError("O nome não pode estar vazio.")

        for user in user_data:
            if user['name'].title() == name:
                print("Já existe um usuário cadastrado sob esse nome")
                print("Aperte enter para retornar.")

        if name:
            return name

        else:
            raise Exception("O nome não pode possuir caracteres ou números. Insira um nome válido.")

def user_register():
    print("\n--- CADASTRAR NOVO USUÁRIO ---")

    user_data = load_json()

    name = name_validate()
    contact = contact_validate()
    cpf = cpf_validate()

    user_data.append({
        'name': name,
        'contact': contact,
        'cpf': cpf
    })
    

    save_json(user_data) 

    print("Cliente cadastrado com sucesso!")

def user_update():
    print("\n--- ATUALIZAR USUÁRIO ---")
    found = load_json()

    name_search = input("Informe o nome do usuário que deseja atualizar >>> ")

    for user in found:
        if user['name'].lower() == name_search.lower():
            print(f"Informe a seguir qual dado deseja alterar do usuário: {user['name']}")
            print("1) NOME")
            print("2) CPF")
            print("3) CONTATO")
            print("4) CANCELAR OPERAÇÃO")

            try:
                option = int(input("OPÇÃO >>>> "))
            except ValueError:
                print("Opção inválida. Tente novamente. . .")
                print("Retornando ao menu")
                return
        
            match option:
                case 1:
                    print(" >>> ATUALIZAÇÃO DE NOME DE USUÁRIO <<<")
                    print("Para cancelar a operação, insira 0")
                    new_user_name = name_validate()

                    if new_user_name == '0':
                        print(">>> OPERAÇÃO CANCELADA <<<.")
                        print("\nNenhuma alteração feita.")
                        print("Retornando ao menu anterior >>>")
                        return

                    save_json(found)
                    print(f"Usuário atualizado com sucesso: {new_user_name}!")
                    user['name'] = new_user_name                    
                    print("\nAperte enter para retornar >>>>")
                    return menu()
                

                case 2:
                    print(" >>> ATUALIZAÇÃO DE CPF DE USUÁRIO <<<")
                    print("\nPara cancelar a operação insira 0")
                    user_new_cpf = cpf_validate()

                    if user_new_cpf == '0':
                        print(">>> OPERAÇÃO CANCELADA <<<.")
                        print("\nNenhuma alteração feita.")
                        print("Retornando ao menu anterior >>>")
                        return



                    save_json(found)
                    print(f"CPF alterado de {user['cpf']} para {user_new_cpf} com sucesso!")
                    user['cpf'] = user_new_cpf                    
                    print("\nAperte enter para retornar. >>> ")
                    return menu()

                case 3:
                    print(" >>> ATUALIZAÇÃO DE CONTATO DE USUÁRIO <<<")
                    print("\nPara cancelar a operação insira 0")
                    user_new_contact = contact_validate()  

                    if user_new_contact == '0':
                        print(">>> OPERAÇÃO CANCELADA <<<.")
                        print("\nNenhuma alteração feita.")
                        print("Retornando ao menu anterior >>>")
                        return

                    save_json(found)
                    print(f"Contato alterado de {user['contact']} para {user_new_contact} com sucesso!")
                    user['contact'] = user_new_contact                    
                    print("\nAperte enter para retornar. >>> ")
                    return menu()                                        

                case 4:
                    print(">>> OPERAÇÃO CANCELADA <<<.")
                    print("\nRetornando ao menu . . .")
                    return
                
                case _:
                    print("Opção inválida.")
                    return
    
    print("Usuário não encontrado.")
    input("\nPressione Enter para voltar ao menu.")


def user_delet():
    print("\n--- DELETAR USUÁRIO ---")

    users = load_json()
    found = user_search()

    while True:
        try:
            indice = int(input("\nDigite o índice que deseja deletar ou 0 para cancelar. >>> ").strip())

            if indice == '0':
                print("Operação cancelada. \nNenhum usuário foi deletado.")
                print("Aperte enter para retornar >>>")
                break

            if 1 <= indice <= len(found):
                deleted_user=users.pop(indice)
                save_json(users)
                

            else:
                raise Exception(f"Opção inválida. Digite um número entre 1 e {len(found)}.")
            
        except Exception:
            print("Operação inválida. Tente novamente.")
            input("Aperte enter para retornar.")


        confirmation = input(f"\nTem certeza que deseja deletar (S/N): ").lower().strip()
        print(f"NOME: {deleted_user['name']}")
        print(f"CPF: {deleted_user['cpf']}")
        print(f"CONTATO: {deleted_user['contact']}")
        print("?")

        if confirmation != 's':
            print("Operação cancelada.\nNenhum usuário deletado.")
            print("Aperte enter para retornar >>> ")
            return
               
        save_json(users)

        print(f"Usuário(s) {deleted_user['name']} removido com sucesso")
        return

def menu():
    while True:
        print(">>>>> MENU <<<<<")
        print("0) PESQUISAR USUÁRIO")
        print("1) CADASTRAR USUÁRIO")
        print("2) ATUALIZAR USUÁRIO")
        print("3) DELETAR USUÁRIO")
        print("4) VOLTAR AO MENU PRINCIPAL")
        option = int(input("OPÇÃO >>>> "))
        
        match(option):
            case 0:
               user_search()
            case 1:
                user_register()
            case 2:
                user_update()
            case 3:
                user_delet()
            case 4:
                print("Retornando ao menu principal. . .")
                break         
            case _:
                print("Opção inválida. \nTente novamente.")
                print("Aperte enter para retornar >>> ")

def main():
    menu()

if __name__ == '__main__':
    main()
