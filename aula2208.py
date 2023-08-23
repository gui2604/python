import random #para gerar uma matriz com números aleatórios (random.radint(0,10))
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
'''
def printa_elementos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"matriz[{i}][{j}] = {matriz[i][j]}")
    return

def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

def cria_matriz(linhas, colunas, elem):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(elem)
    return matriz

def cria_matriz_random(linhas, colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(random.randint(0,10))
    return matriz

def soma_lista(lista):
    soma = 0
    for elem in lista:
        soma += elem
    return soma

def encontrar_maior_dict(lista):
    maior = float('-inf')
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice_do_maior = i
    return indice_do_maior

'''
#crie uma matriz 5x10, preencha todas as linhas pares com 1 ao invés de 0
#crie outra matriz 5x10, preencha todas as colunas pares com 1 ao invés de 0
matriz1 = cria_matriz(5, 10, 0)
for i in range(len(matriz1)): #for i in range(0, len(matriz), 2)
    for j in range(len(matriz1[0])):
        if i % 2 == 0: #remove o if
            matriz1[i][j] = 1
mostra_matriz(matriz1)
print()
matriz2 = cria_matriz(5, 10, 0)
for i in range(len(matriz2)):
    for j in range(len(matriz2[0])): #for i in range(0,len(matriz[0]),2):
        if j % 2 == 0: #remove o if
            matriz2[i][j] = 1
mostra_matriz(matriz2)


#Faça a matriz transposta (inverter linha com coluna)
matriz1 = [[1,2,3],[4,5,6],[7,8,9]]
#matrizT = [[1,4,7],[2,5,8],[3,6,9]]
for i in range(len(matriz1)):
    for j in range(i):
            aux = matriz1[i][j]
            matriz1[i][j] = matriz1[j][i]
            matriz1[j][i] = aux
mostra_matriz(matriz1)

#forma mais otimizada de construir um tabuleiro de xadrez:
matriz1 = cria_matriz(8,8,0)
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        if (i + j) % 2 == 1:
            matriz1[i][j] = 1
mostra_matriz(matriz1)

#Multiplicação de Matrizes
pesos = [1,2,3,2,1]
alunos = cria_matriz_random(5,10)
media_alunos = []

soma_pesos = soma_lista(pesos)

for j in range(len(alunos[0])):
    soma = 0
    for i in range(len(pesos)):
        soma += pesos[i] * alunos[i][j]
    media = soma / soma_pesos
    media_alunos.append(media)
print("Pesos das notas:")
print(pesos)
print("Notas dos Alunos:")
mostra_matriz(alunos)
print("Media de cada aluno:")
print(media_alunos)

# DICIONÁRIOS
jogo = {'são paulo': 'vencedor', 'corinthians': 'perdedor'}
jogo['palmeiras'] = 'sem mundial' #adiciona
jogo['são paulo'] = 'trimundial' #sobrescreve
time = input('pra que time vc torce?\nR:')
print(f"Você é um {jogo[time]}")

saudacoes = {
    'oi': ['olá', 'salve', 'eae', 'fmz'],
    'tchau': ['e o pix?', 'flw', 'tmj', 'vaza']
            }
print(saudacoes.keys())
while True:
    resposta = input("diga oi ou tchau\nR: ")
    if resposta in saudacoes.keys():
        print(random.choice(saudacoes[resposta]))
    elif resposta == "sair":
        break
    else:
        print("Fala dnv")

#crie um dicionário vazio e adicione membros da família e seus respectivos nomes
familia = {}
familia["pai"] = "joao"
familia["mae"] = "elisabete"
familia["irmao"] = "fulano"
familia["primo"] = "ciclano"
for key in familia.keys():
    print(f"O nome do(a) seu(sua) {key} é {familia[key]}")
'''

# declara um dicionario com uma chave de carros e outra chave de preços
#encontre o carro mais caro

loja = {
    "carros": ["gol", "polo", "celta", "meriva"],
    "precos": [300, 100, 1000, 50]
}
indice_maior = encontrar_maior_dict(loja["precos"])
carro = loja["carros"][encontrar_maior_dict(loja["precos"])]
print(f"O carro mais caro é o {carro}")
import pandas as pd
loja["potencia"] = [10,20,30,100000,10]
print(f"A potencia do carro mais caro é {lojas['potencia'][indice_maior]}")
