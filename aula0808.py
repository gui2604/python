#Revisão
'''
lista = ["Danilo", "Allen", "Cordeiro", "Israel", "Francisco"]

#for nome in lista:
#   print(nome)
for i in range(len(lista)):
    #print(i) - printar os índices
    #print(lista[i]) - printar os professores
    print(f"O {lista[i]} está no índice {i}")
'''
'''
#Verificar senha do usuário c/ tentativas ilimitadas
senha = "12345"
senha_usuario = input("Diga sua senha: ")
while senha_usuario != senha:
    print("errou, digite novamente")
    senha_usuario = input("Diga sua senha: ")
print("Acesso Liberado")
'''
'''
#Verificar senha do usuário com tentativas
senha = input("Digite sua senha: ")
i = 1
while senha != "123" and i < 3:
    senha_usuario = input(f"Errado, digite novamente {3-i} tentativas restante: ")
    i += 1
if senha == "123":
    print("acesso concedido")
else:
    print("bloqueado")
'''
'''
#Verifica senha c/ 3 tentativas usando for e break
senha = "123"
for i in range(3):
    senha_usuario = input("Diga sua senha: ")
    if senha == senha_usuario:
        print("acesso liberado")
        break


lista = ["Danilo", "Allen", "Cordeiro", "Israel", "Francisco"]

if "Danilo" in lista:
    print(True)
print(lista.index("Danilo"))

for nome in lista:
    if nome == "Danilo":
        print("Encontrei")

i = 0
for nome in lista:
    if nome == "Danilo":
        print(f"Encontrei no {i}")
    i += 1


#Achar o carro mais caro
precos = [50, 100, 1000, 200, 300]
carros = ["up", "ka", "celta", "uno", "kombi"]


def acha_maior(valores):
    maior_preco = float('-inf')
    for i in range(len(valores)):
        if valores[i] > maior_preco:
            maior_preco = valores[i]
            indice_maior = i
    return indice_maior
local_maior = acha_maior(precos)
print(f"O carro mais caro é o {carros[local_maior]}, valendo R${precos[local_maior]},00")

teste = [1,2,3,4,5]
local_maior_teste = acha_maior(teste)
print(local_maior_teste)
'''
'''
# declara 2 listas com qlq coisa dentro
# monte uma lista com os elementos em comum entre as duas

primeira = [1, 2, 3, 4, 5]
segunda = [3, 4, 5, 6, 7, 8, 9, 10]

def encontre_comuns(lista1, lista2):
    comum = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            #print(f"estou verificando se {lista1[i]}=={lista2[j]}")
            if lista1[i] == lista2[j]:
                comum.append(lista1[i])
    return comum
#lista_comum = encontre_comuns(primeira, segunda)
#print(lista_comum)
print(encontre_comuns(primeira, segunda))
'''
'''
#inverta a lista
lista = ["a","b","c","d","e","f","g","h","i","j"]
n = len(lista) - 1
lista_invertida = []
while n != -1:
    lista_invertida.append(lista[n])
    n -= 1
print(lista_invertida)

#inverta a lista sem criar outra lista (para não ocupar o dobro da memória)
numeros = [1,2,3,4,5,6,7,8,9,10,11]

def inverte_lista(lista):
    j = len(lista) - 1
    for i in range(int(j/2)):
        aux = lista[i]
        lista[i] = lista[j - i]
        lista[j - i] = aux
    return lista
print(inverte_lista(numeros))

#inveter com recursos de python:

numeros.reverse()
print(numeros)

print(numeros[::-1])
'''
'''
# fazendo imagem com matriz
tam = 10
matriz = [[1 for i in range(tam)]] for j in range(tam)]
for i in range(tam):
    for j in range(tam):
        if i < j:
            matriz[i][j] = 0

import matplotlib.pyplot as plt
plt.imshow(matriz)
plt.colorbar()
plt.show()
'''
'''
# Matrizes (lista de listas)
#matriz = [[1,2,3],[4,5,6],[7,8,9]]
#print(matriz[1][0])

# para acessar uma linha da matriz, o primeiro índice é fixo, para acessar uma coluna, o segundo índice é fixo.
#exercício: altere todos os elementos da matriz para 0.

matriz = [[1,2,3,11],[4,5,6,11],[7,8,9,11]] #obrigatoriamente as listas terão a mesma quantidade de elementos
for i in range(len(matriz)):
    for j in range(len(matriz[0])): #O "matriz[0] é necessário ao invés de apenas "matriz" porque dessa forma só serve apenas para matrizes quadradas
        matriz[i][j] = 0
print(matriz)
'''
'''
#declare uma matriz apenas de zeros, e abaixo da diagonal da matriz, troque os zeros para numeros um
matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
'''
'''
for k in range(len(matriz)):
    print(matriz[k])
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i < j:
            matriz[i][j] = 1
print(matriz)
for l in range(len(matriz)):
    print(matriz[l])
'''
'''
#printando a matriz com numpy
matriz = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
import numpy as np
matriz = np.array(matriz)
print(matriz)
'''
