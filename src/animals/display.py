"""
* SHOW ANIMALS DATA
"""

def show_menu_animals():
    while True:
        option = int(input(
"""--ANIMAIS--
0)Voltar
1)Pesquisar
2)Adicionar
3)Atualizar
4)Deletar
:"""        
          ))
        
        match (option):
            case 0:
              break
            case 1:
              #pesquisar
            case 2:
              #adicionar
            case 3: 
              #atualizar
            case 4:
              #deltar
            case _:
              print("Opção inválida.Escolha entre (0 - 4)")
              input("Pressione Enter para continuar")