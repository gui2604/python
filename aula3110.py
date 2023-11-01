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
    print(chute, "|", chute**2, "|", num, "|", qtd)
#binary_search_sqrt(1080)

def raiz_binaria(num, precisao):
    inicio = 0
    fim = num
    chute = (inicio + fim) / 2
    while abs(chute ** 2 - num) >= precisao:
        if chute ** 2 > num:
            fim = chute
        else:
            inicio = chute
        chute = (inicio + fim) / 2
    return chute

def checa_numero():
    num = input("diga um numero: ")
    while not num.isnumeric():
        num = input("diga um numero: ")
    return num

def checha_numero_recursivo():
    num = input("diga um numero: ")
    if not num.isnumeric():
        return checha_numero_recursivo()
    return num

def raiz_binaria_recursiva(num, precisao, inicio, fim):
    chute = (inicio + fim) / 2
    if abs(chute ** 2 - num) >= precisao:
        if chute ** 2 > num:
            fim = chute
            return raiz_binaria_recursiva(num, precisao, inicio, fim)
        else:
            inicio = chute
            return raiz_binaria_recursiva(num, precisao, inicio, fim)
    return chute

#print(raiz_binaria_recursiva(25, 0.001, 0, 25)**2)
def binary_search_list(lista, alvo, inicio, fim):
    index_chute = (fim + inicio) // 2
    if lista[index_chute] == alvo:
        return index_chute
    else:
        if lista[index_chute] > alvo:
            fim = index_chute
        else:
            inicio = index_chute
        return binary_search_list(lista, alvo, inicio, fim)

#lista = [4, 2, 6, 7, 1, 0, 3, 5]
#lista.sort()
#print(lista)
#print()
#print(binary_search_list(lista, 7, 0, len(lista)))

def acha_indice(num, inicio, fim, lista):
    indice_chute = (inicio + fim) // 2
    if lista[indice_chute] != num:
        fim = indice_chute
    else:
        inicio = indice_chute
        return acha_indice(num, inicio, fim, lista)
    return indice_chute

def quicksort(lista):
    if lista:
        pivo = lista[0]
        lista_menor = []
        lista_maior = []
        for i in range(1, len(lista)):
            if lista[i] < pivo:
                lista_menor.append(lista[i])
            else:
                lista_maior.append(lista[i])
        return quicksort(lista_menor) + [pivo] + quicksort(lista_maior)
    return lista

def quicksort_(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [elem for elem in lista if elem < pivo]
        maiores = [elem for elem in lista if elem > pivo]
        menores_ordenados = quicksort_(menores)
        maiores_ordenados = quicksort_(maiores)
        print(maiores_ordenados, pivo, menores_ordenados)
        return maiores_ordenados + [pivo] + maiores_ordenados
#lista = [4, 2, 6, 7, 1, 0, 3, 5]
#print(quicksort(lista))

#arquivos externos
#with open('teste.txt', 'w') as file:
#with open('teste.json', 'w') as file:
    #frase = '\nai8sudhausdhn'
    #matriz = [[0 for i in range(10)] for j in range(10)]
    #dic = {str(i): i for i in range(10)}
    #file.writelines(str(matriz))
    #file.writelines(str(dic))
    #for elem in file: #.readlines()
        #print(elem)
    #file.write(frase)

#carrega o json
import json
with open('teste.json', 'r') as teste:
    teste = json.load(teste)
    print(teste.keys())
