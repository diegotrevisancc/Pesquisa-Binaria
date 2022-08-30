def cria_lista ():
    lista =[]    
    for index in range(0, 101):
        lista.append(index)
    return lista

def pesquisa_binaria (list): 
    contador = 0
    baixo = 0
    alto = len(list) - 1
    meio = baixo + alto //2
    tentativa = "n"

    while tentativa == "n":
        contador += 1
        tentativa = input("{} é o seu número? Sim(s) ou Não(n) " .format(meio))
        if tentativa =="s":
            break
        tamanho = input("É maior(1) ou menor(2)? ") 
        if tamanho == "1":
            alto = meio 
            meio = (baixo + alto)//2 
        elif tamanho == "2":
            baixo = meio 
            meio = (baixo + alto) //2 
    
    print("Número de passos: {}".format(contador))
    print("Número escolhido: {}" .format(meio))
lista = cria_lista()
pesquisa_binaria(lista)
