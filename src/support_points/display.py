"""
* SHOW SUPORT POINTS
"""

def show_menu_SuportPoints():
    while True:
        option = int(input(
"""--PONTOS DE APOIO--
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
              show_menu_SuportPoints()
            case 2:
              #adicionar
              show_menu_adicionar_SuportPoints()
            case 3: 
              #atualizar
              show_menu_atualizar_SuportPoints()
            case 4:
              #deletar
              show_menu_atualizar_SuportPoints()
            case _:
              print("Opção inválida.Escolha entre (0 - 4)")
              input("Pressione Enter para continuar")

def show_menu_pesquisa_SuportPoints():
   while True:
      option = int(input(
"""--PESQUISAR PONTOS DE APOIO--
0)Voltar
1)
2)
3)
4)
"""
     ))
def show_menu_adicionar_SuportPoints():
   while True:
      option = int(input(
"""--ADICIONAR PONTOS DE APOIO--
0)Voltar
1)
2)
3)
4)
"""
    ))
def show_menu_atualizar_SuportPoints():
   while True:
      option = int(input(
"""--ATUALIZAR PONTOS DE APOIO--
0)Voltar
1)
2)
3)
4)
"""
      ))
def show_menu_deletar_SuportPoints():
   while True:
      option = int(input(
"""--DELETAR PONTOS DE APOIO--
0)Voltar
1)
2)
3)
4)
"""
      ))