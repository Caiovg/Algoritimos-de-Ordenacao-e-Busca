def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        aux = i - 1
        while aux >= 0 and vetor[aux] > chave:
            vetor[aux + 1] = vetor[aux]
            aux -= 1
        vetor[aux + 1] = chave
    return vetor



lista = []
n = int(input("Digite qual vai ser o tamanho da sua lista: "))
for i in range(n):
    aux = int(input("Digite o " + str(i) + "º valor: "))
    lista.append(aux)
print("Sua lista não ordenada")
print(lista)


lista = insertion_sort(lista)
print("Lista ordenada com insertion sort: ")
print(lista)
