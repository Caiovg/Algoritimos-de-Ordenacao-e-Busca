def selection_sort(vetor, indice):
    """
    vetor: lista. Lista que será ordenada
    indice: int. Indice do elemento a ser ordenado na lista
    """
    if indice >= len(vetor) - 1:
        return -1

    # minIndice guarda a posicao onde esta o menor valor em relacao ao indice
    min_indice = indice

    for i in range(indice + 1, len(vetor)):
        if vetor[i] < vetor[min_indice]:
            min_indice = i

    temp = vetor[indice]
    vetor[indice] = vetor[min_indice]
    vetor[min_indice] = temp

    selection_sort(vetor, indice + 1)

    return vetor


lista = []
n = int(input("Digite qual vai ser o tamanho da sua lista: "))
for i in range(n):
    aux = int(input("Digite o " + str(i) + "º valor: "))
    lista.append(aux)
print("Sua lista não ordenada")
print(lista)


lista = selection_sort(lista, 0)
print("Lista ordenada com selection sort: ")
print(lista)

