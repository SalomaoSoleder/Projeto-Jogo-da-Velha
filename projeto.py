import random

def primeiro_jogadorFuncao() :
  if random.randint(0, 1) == 0:
        return 'Player 2'
  else:
        return 'Player 1'


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

def vencedorFuncao(posicoes) :
  if (posicoes[1] == posicoes [2] == posicoes[3] and posicoes[1]!=" ") :
    return True
  if (posicoes[1] == posicoes [4] == posicoes[7] and posicoes[1]!=" ") :
    return True
  if (posicoes[1] == posicoes [5] == posicoes[9] and posicoes[1]!=" ") :
    return True
  if (posicoes[4] == posicoes [5] == posicoes[6] and posicoes[4]!=" ") :
    return True
  if (posicoes[2] == posicoes [5] == posicoes[8] and posicoes[2]!=" ") :
    return True
  if (posicoes[7] == posicoes [8] == posicoes[9] and posicoes[7]!=" ") :
    return True
  if (posicoes[7] == posicoes [5] == posicoes[3] and posicoes[7]!=" ") :
    return True
  if (posicoes[3] == posicoes [6] == posicoes[9] and posicoes[3]!=" ") :
    return True
  return False

if __name__ == '__main__':
  posicoes = ["@"," "," "," "," "," "," "," "," "," "]
  player_1 = escolherFuncao()
  if player_1=="X" :
    player_2 = "O"
  else :
    player_2 ="X"
  primeiro_a_jogar = primeiro_jogadorFuncao()

  if (primeiro_a_jogar=="Player 1") :
    print("player 1 é o primeiro a começar")
    tabuleiroFuncao(posicoes)
    print("È a vez de player 1 jogar")
    posicao_do_usuario = dadosFuncao()
    posicoes[posicao_do_usuario] = player_1
    tabuleiroFuncao(posicoes)
    
    
    while (True) :
      print("È a vez de player 2 jogar")
      posicao_do_usuario = dadosFuncao()
      while (posicoes[posicao_do_usuario]!=" ") :
        print("Valor invalido")
        posicao_do_usuario = dadosFuncao()

      posicoes[posicao_do_usuario] = player_2
      tabuleiroFuncao(posicoes)
      vencedor = vencedorFuncao(posicoes)

      if (vencedor==True) :
        print("Voce ganhou player 2 ")
        break

      print("È a vez de player 1 jogar")
      posicao_do_usuario = dadosFuncao()
      while (posicoes[posicao_do_usuario]!=" ") :
        print("Valor invalido")
        posicao_do_usuario = dadosFuncao()

      posicoes[posicao_do_usuario] = player_1
      tabuleiroFuncao(posicoes)
      vencedor = vencedorFuncao(posicoes)
      if (vencedor==True) :
        print("Voce ganhou player 1 ")
        break

  if (primeiro_a_jogar=="Player 2") :
    print("player 2 é o primeiro a começar")
    tabuleiroFuncao(posicoes)
    print("È a vez de player 2 jogar")
    posicao_do_usuario = dadosFuncao()
    posicoes[posicao_do_usuario] = player_2
    tabuleiroFuncao(posicoes)
    while (True) :
      print("È a vez de player 1 jogar")
      posicao_do_usuario = dadosFuncao()
      while (posicoes[posicao_do_usuario]!=" ") :
        print("Valor invalido")
        posicao_do_usuario = dadosFuncao()

      posicoes[posicao_do_usuario] = player_1
      tabuleiroFuncao(posicoes)
      vencedor = vencedorFuncao(posicoes)

      if (vencedor==True) :
        print("Voce ganhou player 1 ")
        break

      print("È a vez de player 2 jogar")
      posicao_do_usuario = dadosFuncao()
      while (posicoes[posicao_do_usuario]!=" ") :
        print("Valor invalido")
        posicao_do_usuario = dadosFuncao()

      posicoes[posicao_do_usuario] = player_2
      tabuleiroFuncao(posicoes)
      vencedor = vencedorFuncao(posicoes)
      if (vencedor==True) :
        print("Voce ganhou player 2 ")
        break









'''
def dadosFuncao() :
    pergunta = int(input("Digite um valor entre 1 e 9 "))
    if (pergunta<1 or pergunta>9) :
        while (pergunta<1 or pergunta>9) :
            pergunta = int(input("Digite um valor entre 1 e 9 "))
  '''



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

'''
Fazer um loop que execute permanentemente enquanto não exista vencedores no jogo, ou todas as posições da lista de posições estejam ocupadas.

"usuario escolhe X ou O"

se esxitir isso " " na lista, o jogo pode continuar

( "alguém não ganhou?" ou "lista com as posições não está cheia?"): jogo jogo jogo jogo jogo ...
'''
#Velha ou não ?#
