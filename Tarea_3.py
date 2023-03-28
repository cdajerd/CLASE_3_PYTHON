#Act 1 Imprimir al reves un string
text = input ("Introduzca su texto \n") 
mirror = text[::-1]
print (mirror)

#Act 2 Reordenar los Stacks
arr1 = [3, 2, 1]
arr2 = [4, 5]
arr3 = []

i = 0
while i < arr1.__len__():
        if arr1[i] == 1:
            arr3.append(arr1[i])
            arr1.pop(i)
        elif not arr1[i] % 2:
            arr2.append(arr1[i])
            arr1.pop(i)
        else:
            i += 1

i = 0
while i < arr2.__len__():
        if arr2[i] == 1:
            arr3.append(arr2[i])
            arr2.pop(i)
        elif arr2[i] % 2:
            arr1.append(arr2[i])
            arr2.pop(i)
        else:
            i += 1

print(arr1, arr2, arr3, sep='\n')

#Act 3 Implementar Bubble Sort

def bubbleSort(lista):
	n = len(lista)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if lista[j] > lista[j + 1]:
				swapped = True
				lista[j], lista[j + 1] = lista[j + 1], lista[j]
		
		if not swapped:
			return


lista = input('Por favor introduzca la lista de números separados por coma:\n')
lista = [int(n) for n in lista.split(sep=',')]

bubbleSort(lista)
print(lista)