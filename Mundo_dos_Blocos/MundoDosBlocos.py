import random
from copy import deepcopy

""" AI para resolver o problema do mundo dos Blocos """

__Author__ = "Caio Pompei, Alexandre Ciro"
__Version__ = "1.0"
__email__ = "caio.pompei@gmail.com"


# EstadoAtual é o estado do jogo abaixo

torre_1 = []
torre_2 = ["B", "A", "C"]
torre_3 = []

#----------------------

estadoFinal = ["C","B","A"]

rodando = True

#For AI -----------------------------------

la = [] #Lista Aberta
lf = [] #Lista Fechada

estadoInicial =[]
estadoAtual = []

estadoInicial.append(torre_1)
estadoInicial.append(torre_2)
estadoInicial.append(torre_3)

la.append(estadoInicial)

# --------------------------------------

def player():

    random.shuffle(torre_2)  # Embaralhar a lista

    printTorre()

    print("Posição esperada: ")
    printTorre_U(estadoFinal)


    while rodando:
      blocoSelecionado = input("Digite o bloco que deseja mover: \n A \n B \n C \n")
      torreFinal = input("Digite a torre que deseja mover o bloco: \n 1 - Torre 1 \n 2 - Torre 2 \n 3 - Torre 3 \n")

      moverBloco(blocoSelecionado, torreFinal)

      printTorre()

      if (torre_1 or torre_2 or torre_3) == estadoFinal:
        print("Você ganhou!")
        break

# AI ---------------------------------------------------------------------------------------------------------------------

def AI(): #Funcao main para rodar a AI

  random.shuffle(torre_2)  # Embaralhar a lista

  print("Estado inicial: ")
  printTorre()

  la = [] 
  lf = []  


  estadoInicial = [torre_1[:], torre_2[:], torre_3[:]] # [:] significa fazer uma cópia da lista
  la.append((estadoInicial, []))  # Estado inicial com o caminho vazio

  while la:
      estado_atual, caminho = la.pop(0) # Retira de LA
      lf.append(estado_atual)  # Adiciona em LF

      if estadoIgual(estado_atual):
          print("Solução encontrada! Caminho:")
          for passo in caminho:
            printTorre_AI(passo)
          printTorre_AI(estado_atual)
          return None
          

      novos_estados = gerarEstados(estado_atual) #Gera um novo estado a partir do estado atual do jogo

      for novo_estado in novos_estados:
          if novo_estado not in lf:  # Verifica se o novo estado não esta presente em listaFechada
              novo_caminho = caminho + [novo_estado]
              la.append((novo_estado, novo_caminho))

  print("Solução não encontrada")
  return None


def aiMoverBloco(bloco, origem, destino):

  if bloco in origem and bloco == origem[-1]:
      origem.pop()
      destino.append(bloco)
      return True
  return False



def gerarEstados(estado):
    novas_configuracoes = []
    torres = estado

    # Tenta mover o bloco de cada torre para as outras duas
    for i in range(3):
        if len(torres[i]) > 0:  # Se blocos na torre for maior que zero
          bloco = torres[i][-1]  # O bloco do topo da torre
          for j in range(3):
                if i != j:  #Evita que o bloco seja movimentado para a mesma torre
                    
                    novo_estado = deepcopy(torres)
                    aiMoverBloco(bloco, novo_estado[i], novo_estado[j])
                    novas_configuracoes.append(novo_estado)
    
    return novas_configuracoes


def estadoIgual(estado):
    # Vê se alguma das torres contém o estado final
    return estado[0] == estadoFinal or estado[1] == estadoFinal or estado[2] == estadoFinal

def printTorre_AI(estado):
  #Coloca as torres no formato visual adequado
  torre_1, torre_2, torre_3 = estado
  
  for i in range(2, -1, -1):
        valores = [
            f"[{torre_1[i]}]" if i < len(torre_1) else "[ ]",   
            f"[{torre_2[i]}]" if i < len(torre_2) else "[ ]",
            f"[{torre_3[i]}]" if i < len(torre_3) else "[ ]"
        ]
        print(" ".join(valores)) #O .join junta os elementos da lista em uma unica String com um espaço entre cada elemento
  print("")

#PLAYER ---------------------------------------------------------------------------------------------------------------------------------------------

def moverBloco(bloco, final):
  torres = {"1": torre_1, "2": torre_2, "3": torre_3}

  for torre in torres.values():
    if bloco in torre and bloco == torre[-1]:
      torre.pop()
      print(f"Bloco {bloco} movido para a Torre_{final}")
      torres[final].append(bloco) #Adiciona o bloco na torre indicada pelo usuário em {final}
      return

  print("Bloco não encontrado ou não está na Torre correta")


def printTorre():

  for i in range(2, -1, -1):
        valores = [
            f"[{torre_1[i]}]" if i < len(torre_1) else "[ ]",   # Colocar o valor i da torre se o tamanho da torre for maior que o i. Se não colocar vazio
            f"[{torre_2[i]}]" if i < len(torre_2) else "[ ]",
            f"[{torre_3[i]}]" if i < len(torre_3) else "[ ]"
        ]
        print(" ".join(valores)) #O .join junta os elementos da lista em uma unica String com um espaço entre cada elemento
  print("")

def printTorre_U(torre): # Use um argumento unico do tipo array para printar uma torre unitária

  for i in range(2, -1, -1):
        valores = [
            f"[{torre[i]}]" if i < len(torre) else "[ ]",   # Colocar o valor i da torre se o tamanho da torre for maior que o i. Se não colocar vazio
        ]
        print(" ".join(valores))
  print("")

def definirEstado(estado,l1,l2,l3):
  estado.append(l1)
  estado.append(l2)
  estado.append(l3)


# Chama a função principal
#player()
AI()