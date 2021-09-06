def heap_sort(data):
    length = len(data)
    index = length // 2
    parent = 0
    child = 0
    temp = 0
    while True:
        if index > 0:
            index -= 1
            temp = data[index]
        else:
            length -= 1
            if length == 0:
                return
            temp = data[length]
            data[length] = data[0]

        parent = index
        child = index * 2 + 1

        while child < length:
            if (child + 1) < length and data[child + 1] > data[child]:
                child += 1
            if data[child] > temp:
                data[parent] = data[child]
                parent = child
                child = parent * 2 + 1
            else:
                break
        data[parent] = temp


lista = []
n = int(input("Digite qual vai ser o tamanho da sua lista: "))
for i in range(n):
    aux = int(input("Digite o " + str(i) + "º valor: "))
    lista.append(aux)
print("Sua lista não ordenada")
print(lista)

heap_sort(lista)
print("Lista ordenada com heap sort: ")
print(lista)
