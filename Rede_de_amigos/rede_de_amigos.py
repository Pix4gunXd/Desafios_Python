amizades = {
    'A': ['B', 'C'],
    'B': ['A', 'E'],
    'C': ['A', 'D', 'F'],
    'D': ['C', 'F'],
    'E': ['B', 'F', 'G'],
    'F': ['C', 'D', 'E' ],
    'G': ['E']
}

la = ['A'] # Referenciar pelo index[0] para pegar estado atual
lf = []

rodando = True



estadoFinal = 'G'

def AI():
  print("1st: LA: ", la)
  print("1st: LF: ", lf)

  # Verificar menor número de pessoas entre A e G
  for i in range(5):
    lf.insert(0, la[0]) # Começa com A
    la.pop(0) #Remove de la o elemento 0



    for j in amizades[lf[0]]: #No elemento atual
      if j not in lf: #Verifica se elemento esta na lista fechada
        if j == estadoFinal:
          lf.insert(0, j)
          print("Finalizado")
          return
        else:
          la.insert(0, j)

    print("\nLA: ", la)
    print("LF: ", lf , "\n")

  print("\nLA: ", la)
  print("LF: ", lf , "\n")






# MAIN:
AI()
