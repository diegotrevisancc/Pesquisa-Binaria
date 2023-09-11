#Implementação de pesquisa binária com recursão
def binarySearch(n, list, passos):
  half = (len(list) - 1) // 2
  selected = list[half]
  passos += 1
  if selected == n:
    print("Passos", passos)
    return selected
  elif selected > n:
    list = list[:half]
    return binarySearch(n, list, passos)
  else:
    list = list[half+1:]
    return binarySearch(n, list, passos)

binarySearch(42, list(range(101)), 0)
