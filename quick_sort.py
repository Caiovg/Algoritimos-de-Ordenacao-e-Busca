def troca(lista, pos1, pos2):
    """ Troca a posição de dois itens em uma lista """
    temp = lista[pos1]
    lista[pos1] = lista[pos2]
    lista[pos2] = temp

def particiona(lista, comeco, fim):
    """ Divide uma lista """
    pivo = lista[comeco]
    while True:
        while lista[comeco] < pivo:
            comeco = comeco + 1

        while lista[fim] > pivo:
            fim = fim - 1

        if comeco >= fim:
            return fim

        troca(lista, comeco, fim)

        comeco = comeco + 1
        fim = fim - 1


def quick_sort(lista, comeco, fim):
    """ Algoritmo de quick sort """
    if comeco < fim:
        part = particiona(lista, comeco, fim)
        quick_sort(lista, comeco, part)
        quick_sort(lista, part + 1, fim)


lista = []
n = int(input("Digite qual vai ser o tamanho da sua lista: "))
for i in range(n):
    aux = int(input("Digite o " + str(i) + "º valor: "))
    lista.append(aux)
print("Sua lista não ordenada")
print(lista)

quick_sort(lista, 0, len(lista) - 1)
print("Lista ordenada com quick sort: ")
print(lista)
