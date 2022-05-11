def tabuleiroFuncao(lista_posicoes) :
    print("   |   |   ")
    print(f" {lista_posicoes[1]} | {lista_posicoes[2]} | {lista_posicoes[3]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {lista_posicoes[4]} | {lista_posicoes[5]} | {lista_posicoes[6]} ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(f" {lista_posicoes[7]} | {lista_posicoes[8]} | {lista_posicoes[9]} ")
    print("   |   |   ")

def dadosFuncao() :
    pergunta = int(input("Digite um valor entre 1 e 9 "))
    if (pergunta<1 or pergunta>9) :
        while (pergunta<1 or pergunta>9) :
            pergunta = int(input("Digite um valor entre 1 e 9 "))
    return pergunta



def escolherFuncao() :
  pergunta_de_escolha = str(input("Voce prefere jogar com X ou O ? "))
  if (pergunta_de_escolha!="X" and pergunta_de_escolha!="O") :
    while (pergunta_de_escolha!="X" and pergunta_de_escolha!="O") :
      pergunta_de_escolha = str(input("Voce prefere jogar com X ou O ? "))
  return pergunta_de_escolha

def VencedorFuncao(posicoes) :
  if (posicoes[1] == posicoes [2] == posicoes[3]) :
    return True
  if (posicoes[1] == posicoes [4] == posicoes[7]) :
    return True
  if (posicoes[1] == posicoes [5] == posicoes[9]) :
    return True
  if (posicoes[4] == posicoes [4] == posicoes[6]) :
    return True
  if (posicoes[2] == posicoes [5] == posicoes[8]) :
    return True
  if (posicoes[7] == posicoes [8] == posicoes[9]) :
    return True
  if (posicoes[7] == posicoes [5] == posicoes[3]) :
    return True
  if (posicoes[3] == posicoes [6] == posicoes[9]) :
    return True

if __name__ == '__main__':
  posicoes = ["@"," "," "," "," "," "," "," "," "," "]
  player_1 = escolherFuncao()
  if player_1=="X" :
    player_2 = "O"
  else :
    player_2 ="X"
  tabuleiroFuncao(posicoes)
  posicao_do_usuario = dadosFuncao()
  posicoes[posicao_do_usuario] = player_1
  tabuleiroFuncao(posicoes)

if __name__ == '__main__':
  posicoes = ["@"," "," "," "," "," "," "," "," "," "]
  player_1 = escolherFuncao()
  tabuleiroFuncao(posicoes)
  posicao_do_usuario = dadosFuncao()
  posicoes[posicao_do_usuario] = player_1
  tabuleiroFuncao(posicoes)


#manter o tabuleiro, utilizar if para mantelo ?#
#E colocar a parte colocada para nao ser mais possivel ser atualizada#
#if("manter os dados") :#

#while(variavel==9 or (variavel[])) :#
#loop aqui ate a pergunta seja igual "TRUE"
#sair do loop#

#pos[1] == pos [2] == pos[3]#


'''
numeros_de_posicoes = dadosFuncao()
posicoes[numeros_de_posicoes] = ""
tabuleiroFuncao(posicoes)

'''


'''

for dado in range(0,len(dado)) :
  if

'''




'''


   |   |
 X | O | X
   |   |
-----------
   |   |
 O | X | O
   |   |
-----------
   |   |
 X | O | X
   |   |




'''