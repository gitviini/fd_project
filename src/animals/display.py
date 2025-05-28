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
              show_menu_pesquisa_animais()
            case 2:
              #adicionar
              show_menu_adicionar()
            case 3: 
              #atualizar
              show_menu_atualizar_animais()
            case 4:
              #deletar
              show_menu_atualizar_animais()
            case _:
              print("Opção inválida.Escolha entre (0 - 4)")
              input("Pressione Enter para continuar")

def show_menu_pesquisa_animais():
   while True:
      option = int(input(
"""--PESQUISAR ANIMAIS--
0)Voltar
1)
2)
3)
4)
"""
     ))
      match (option):
         case 0:
            break
         case _:
            print("Opção inválida.Escolha entre (0 - 4)")
            input("Pressione Enter para continuar")
def show_menu_adicionar():
   while True:
      option = int(input(
"""--ADICIONAR ANIMAIS--
0)Voltar
1)
2)
3)
4)
"""
    ))
      match (option):
         case 0:
            break
         case _:
            print("Opção inválida.Escolha entre (0 - 4)")
            input("Pressione Enter para continuar")

def show_menu_atualizar_animais():
   while True:
      option = int(input(
"""--ATUALIZAR ANIMAIS--
0)Voltar
1)
2)
3)
4)
"""
      ))
def show_menu_deletar_animais():
   while True:
      option = int(input(
"""--DELETAR ANIMAIS--
0)Voltar
1)
2)
3)
4)
"""
      ))

show_menu_animals()