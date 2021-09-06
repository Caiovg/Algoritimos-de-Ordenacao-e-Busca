def busca_linear(lista, chave):
    for i in range(len(lista)):     # Percorre lista do índice 0 a n–1
        if lista[i] == chave:
            return i                # Encontrou elemento na posição i
    return -1                       # Não encontrou o elemento

lista = [0, 1, 3, 5, 6, 7, 8, 9, 10, 11, 12]

print(busca_linear(lista, 1))

