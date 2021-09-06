def bubble_sort(lista, size):
    """
    Argumentos:
    data: lista. Lista que será ordenada
    lista: int. Tamanho da lista]
    """
    swap = False
    for i in range(0, size - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            swap = True
    if swap:
        bubble_sort(lista, size - 1)

lista = []
n = int(input("Digite qual vai ser o tamanho da sua lista: "))
for i in range(n):
    aux = int(input("Digite o " + str(i) + "º valor: "))
    lista.append(aux)
print("Sua lista não ordenada")
print(lista)


bubble_sort(lista, len(lista))
print("Lista ordenada com bubble sort: ")
print(lista)
