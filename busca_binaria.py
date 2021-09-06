def busca_binaria(lista, chave):
    inicio = 0
    fim = len(lista)-1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == chave:     # Encontrou elemento
            return meio
        elif chave > lista[meio]:    # Busca na segunda metade
            inicio = meio + 1
        else:                        # Busca na primeira metade
            fim = meio - 1
    return -1                        # Não encontrou o elemento



lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(busca_binaria(lista, 3))
