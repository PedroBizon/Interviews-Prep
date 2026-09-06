def busca_binaria_iterativa(lista_ordenada, alvo):
    inicio = 0
    fim = len(lista_ordenada) - 1

    while inicio <= fim:
        meio = (inicio+fim) // 2
        
        if lista_ordenada[meio] == alvo:
            return meio

        if lista_ordenada[meio] > alvo:
            fim = meio

        else:
            inicio = meio + 1

    return None


def testes():
    lista1 = range(0, 100, 2)
    lista2 = range(0,100)
    lista3 = range(0, 10000)
    lista4 = range(0, 100000, 10)
    
    print(busca_binaria_iterativa(lista1, 12))
    print(busca_binaria_iterativa(lista2, 50))
    print(busca_binaria_iterativa(lista3, 9000))
    print(busca_binaria_iterativa(lista2, 12345))

testes()