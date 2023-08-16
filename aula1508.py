def printa_elementos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"Matriz[{i}][{j}] = {matriz[i][j]}")
    return

def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

def cria_matriz(linhas,colunas, elem):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(elem)
    return matriz

def soma_matriz(matriz1, matriz2):
    if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
        matriz = cria_matriz(len(matriz1),len(matriz1),0)
        for i in range(len(matriz1)):
            for j in range(len(matriz1[0])):
                matriz[i][j] = matriz1[i][j] + matriz2[i][j]
        return matriz
    else:
        print("Impossível somar matrizes de tamanhos diferentes!")
        return
'''
#crie uma matriz 10x10, mude todos os elementos das linhas pares para 1
matriz1 = cria_matriz(10,10)

for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        if i % 2 == 0:
            matriz1[i][j] = 1
mostra_matriz(matriz1)

#altere as colunas ímpares para 2
matriz1 = cria_matriz(10,10)
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        if j % 2 == 1:
            matriz1[i][j] = 2
mostra_matriz(matriz1)

#outra forma mais eficiente
matriz1 = cria_matriz(10,10)
for j in range(1,len(matriz1[0]), 2):
    for i in range(len(matriz1)):
        matriz1[i][j] = 2

import matplotlib.pyplot as plt
plt.imshow(matriz1)
plt.colorbar()
plt.figure()
tam = 10
matriz2 = cria_matriz(tam, tam)
plt.imshow(matriz2, "hot")
plt.colorbar()
plt.show()

matriz1 = cria_matriz(5,5,2)
matriz2 = cria_matriz(5,5,3)
print("Matriz1:")
mostra_matriz(matriz1)
print("Matriz2:")
mostra_matriz(matriz2)
print("Matriz1 + Matriz2: ")
mostra_matriz(soma_matriz(matriz1,matriz2))
'''
''''
#cria uma matriz de 10x10 e troque os zeros abaixo da diagonal por 1
matriz1 = cria_matriz(10,10,0)
from time import time
t1 = time()
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        if i > j:
            matriz1[i][j] = 1
t2 = time()
print(t2 - t1)
#mostra_matriz(matriz1)

#cria uma matriz de 10x10 e troque os zeros abaixo da diagonal por 1, mais eficiente
matriz1 = cria_matriz(10,10,0)
t1 = time()
for i in range(len(matriz1)):
    for j in range(i):
        if i > j:
            matriz1[i][j] = 1
t2 = time()
print(t2 - t1)
#mostra_matriz(matriz1)
'''
'''
#construa um tabuleiro de xadrez
xadrez = cria_matriz(8,8,2)
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if i%2==0:
            if j%2==0:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1
        else:
            if j%2 == 0:
                xadrez[i][j] = 1
            else:
                xadrez[i][j] = 0
mostra_matriz(xadrez)

#forma mais otimizada de construir um tabuleiro de xadrez:
matriz1 = cria_matriz(8,8,0)
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        if (i + j) % 2 == 1:
            matriz1[i][j] = 1
mostra_matriz(matriz1)
import matplotlib.pyplot as plt
plt.imshow(matriz1)
plt.colorbar()
plt.show()
'''
#Faça a matriz transposta (inverter linha com coluna)
matriz1 = [[1,2,3],[4,5,6],[7,8,9]]
#matrizT = [[1,4,7],[2,5,8],[3,6,9]]
for i in range(len(matriz1)):
    for j in range(i):
            aux = matriz1[i][j]
            matriz1[i][j] = matriz1[j][i]
            matriz1[j][i] = aux
mostra_matriz(matriz1)
