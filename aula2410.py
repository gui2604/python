def acha_menor(lista):
    menor = float('inf')
    indice_do_menor = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_do_menor = i
    return indice_do_menor

def selection_sort_terrivel(lista):
    ordenada = []
    for i in range(len(lista)): #while lista: (uma lista vazia retorna um booleano 0 False)
        indice = acha_menor(lista)
        menor = lista.pop(indice)
        ordenada.append(menor)
        print(lista)
        print(ordenada)
        print()
    return ordenada

lista1 = [4,2,6,1,7,8,0]
#selection_sort_terrivel(lista1)

def selection_sort_muitoruim(lista):
    for i in range(len(lista)):
        indice_sublista = acha_menor(lista1[i:])
        indice_lista = indice_sublista + i
        print(f"O número {lista[indice_lista]}, na sublista {lista[i:]} está no índice {indice_sublista}, porém na lista original {lista} está no {indice_lista}")
        aux = lista[i]
        lista[i] = lista[indice_lista]
        lista[indice_lista] = aux
    return lista

#print(selection_sort_muitoruim(lista1))
#lista1.sort()
#print(lista1)

#faça um código que receba uma lista e printa vizinho a vizinho
#faça um código que troque vizinhos consecutivos

def bubble_sort_ruim(lista):
    for j in range(len(lista)):
        trocas = 0
        for i in range(len(lista) - 1 - j):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                trocas += 1
            print(lista)
        if trocas == 0:
            break
    return lista

#bubble_sort_ruim(lista1)

def binary_search_sqrt(num):
    inicio = 0
    fim = num
    chute = (inicio + fim) / 2
    qtd = 0
    while abs(chute**2 - num) >= 0.001:
        if chute**2 > num:
            fim = chute
        else:
            inicio = chute
        qtd += 1
        chute = (inicio + fim) / 2
    print(chute, chute**2, num, qtd)
binary_search_sqrt(1080)

def acha_raiz(numero):
    inicio = 0
    fim = numero
    raiz = (inicio + fim) / 2
    qtd = 0
    while abs(raiz**2 - numero) >= 0.001:
        if raiz**2 > numero:
            fim = raiz
        else:
            inicio = raiz
        qtd += 1
        raiz = (inicio + fim) / 2
    print(raiz, raiz**2, numero, qtd)
