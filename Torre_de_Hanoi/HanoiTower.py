def torre(n, inicial, final, auxiliar):
  if n == 1:
    print(f"Mover disco de {inicial} -> {final}")
    return

  torre(n-1, inicial, auxiliar, final)
  print(f"Mover disco de {inicial} -> {final}")
  torre(n-1, auxiliar, final, inicial)

if __name__ == "__main__":
  n = (int(input("Insira o número de discos: ")))
  torre(n, "A", "C", "B")
