def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        aux = i - 1
        while aux >= 0 and vetor[aux] > chave:
            vetor[aux + 1] = vetor[aux]
            aux -= 1
        vetor[aux + 1] = chave
    return vetor	

def bucketSort(x):
	arr = []
	slot_num = 10 
	for i in range(slot_num):
		arr.append([])

	# Coloque os elementos da matriz em diferentes buckets
	for j in x:
		index_b = int(slot_num * j)
		arr[index_b].append(j)

	# ordena os buckets
	for i in range(slot_num):
		arr[i] = insertion_sort(arr[i])

	# concatena o resultado
	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			x[k] = arr[i][j]
			k += 1
	return x

lista = [0.897, 0.565, 0.656,
	0.1234, 0.665, 0.3434]
print("Sua lista não ordenada")
print(lista)

bucketSort(lista)
print("Lista ordenada com Bucket Sort: ")
print(lista)



"""lista = []
n = int(input("Digite qual vai ser o tamanho da sua lista: "))
for i in range(n):
    aux = int(input("Digite o " + str(i) + "º valor: "))
    lista.append(aux)
print("Sua lista não ordenada")
print(lista)

bucketSort(lista)
print("Lista ordenada com Bucket Sort: ")
print(lista)
"""
