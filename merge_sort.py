def merge_sort(data):
    if len(data) < 2:
        return
    mid = len(data) // 2

    left_data = data[:mid]
    right_data = data[mid:]

    merge_sort(left_data)
    merge_sort(right_data)

    left_index = 0
    right_index = 0
    data_index = 0

    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index += 1
        data_index += 1

    while left_index < len(left_data):
        data[data_index] = left_data[left_index]
        left_index += 1
        data_index += 1

    while right_index < len(right_data):
        data[data_index] = right_data[right_index]
        right_index += 1
        data_index += 1


lista = []
n = int(input("Digite qual vai ser o tamanho da sua lista: "))
for i in range(n):
    aux = int(input("Digite o " + str(i) + "º valor: "))
    lista.append(aux)
print("Sua lista não ordenada")
print(lista)

merge_sort(lista)
print("Lista ordenada com merge sort: ")
print(lista)
