'''
#Checkpoint2 - correção

print("Bem vindo à vinheria!")
endreco = input("Diga seu endereco:")
ano = input("Diga seu ano de nascimento")
while not ano.isnumeric():
    ano = input("Diga seu ano de nascimento deve ser um numero: ")
ano = int(ano)
if 2023 - ano < 18:
    print("que feio nao pode")
else:
    valor = 0
    qnt_tinto = 0
    qnt_suave = 0
    qnt_rose = 0
    while True:
        opcao = input("qual vinho vc quer? (tinto, suave, rosé)")
        while not (opcao == "tinto" or opcao == "suave" or opcao == "rosé"):
            opcao = input("tem que ser uma dessas: (tinto, suave, rosé)")

        qtd = input(f"Quantas garrafas de {opcao} vc quer?")
        while not qtd.isnumeric():
            qtd = input(f"Qts garrafas de {opcao} vc quer?")
        qtd = int(qtd)

        if opcao == "tinto":
            valor += 30*qtd
            qnt_tinto += qnt
        elif opcao == "suave":
            valor += 40*qtd
            qnt_suave += qnt
        else:
            valor += 50*qtd
            qnt_rose += qnt
        pergunta = input("você quer continuar comprando?(s/n)")
        while not (pergunta == "s" or pergunta == "n"):
            pergunta = input("voce quer continuar comprando?(s/n)")
        if pergunta == "s":
            continue
        else:
            break
    if valor > 500:
        print(f"voce recebeu frete grátis!")
    else:
        valor += 10
    print(f"Valeu, vc gastou R${valor},00 em {qnt_tinto} tinto, {qnt_suave} e {qnt_rose}, e será entregue em {endereco}")
'''


#aula0905
'''
#conte a quantidade de pares na lista
numeros = [234,546,567,567,2343,54234]
pares = 0
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        pares += 1
print(f"O numero de pares é {pares}")

#outra forma:
qnt = len([par for par in numeros if par%2 == 0])

#outra forma(2):
qnt = 0
num in numeros:
    if num%2 ==0:
    qnt += 1
'''
'''
#printe a soma das duas listas elemento a elemento
#adicione a soma elemento a elemento a uma terceira lista
num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = [11,12,13,14,15,16,17,18,19,20]
for i in range (len(num1)):
    print(num1[i] + num2[i])
    
num3 =[]
for i in range(len(num1)):
    num3.append(num1[i] + num2[i])
print(num3)
'''
'''
#conte a quantidade de vogais na lista
letras = ["a","b","c","d","i","o","h"]
vogal = 0
for i in range(len(letras)):
    if (letras[i] == "a" or letras[i] == "e" or letras[i] == "i" or letras[i] == "o" or letras[i] == "u"):
        vogal += 1
print(vogal)

#outra forma utilizando lista no for:
for letra in letras:
    if letra in ["a","e","i","o","u"]:
        vogais += 1
'''
'''
#ache a posição do danilo
profs = ["allen","isreal","danilo","yan","luciano","ana","cordeiro"]
for i in range (len(profs)):
    if profs[i] == "danilo":
        print(f"danilo está no índice {i}, ou seja, na {i+1}ª posição da lista")
'''
'''
#ache o carro mais caro e o mais barato
carros = ["ka","celta","golf","fusca"]
preco = [10,1000,200,5]

menor = float('inf')
maior = float('-inf')

for i in range(len(preco)):
    if preco[i] < menor:
        menor = preco[i]
        indice_menor = i
print(f"O carro de menor valor vale R${menor},00 e é o {carros[indice_menor]}")

for i in range(len(preco)):
    if preco[i] > maior:
        maior = preco[i]
        indice_maior = i
print(f"O carro de maior valor vale R${maior},00 e é o {carros[indice_maior]} ")
'''
'''
#inverta a lista
lista = ["a","b","c","d","i","o","h"]
n = len(lista) - 1
lista_invertida = []
while n != -1:
    lista_invertida.append(lista[n])
    n -= 1
print(lista_invertida)
'''
'''
# Funções

def teste_numerico():
    var = input("Diga um numero: ")
    while not var.isnumeric():
        var = input("Diga um numero: ")
    var = int(var)
    return var

a = teste_numerico()
print(a)
'''
'''
def teste_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

numeros = [12, 234, 43, 54, 7, 234423, 435354, 5, 6]
for numero in numeros:
    if teste_par(numero):
        print(f"{numero} é par")
    else:
        print(f" {numero} é ímpar")
'''
'''
#função teste par sem checar o input do usuario
def teste_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
for i in range(10):
    numero = int(input("Diga um número: "))
    if teste_par(numero):
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
'''
'''
#função dentro de função para checar o input do usuario

def teste_numerico(frase):
    var = input(frase)
    while not var.isnumeric():
        var = input(frase)
    var = int(var)
    return var


def teste_par(num):
    if num % 2 == 0:
        return True
    else:
        return False


for i in range(10):
    numero = teste_numerico("Diga um numero: ")
    if teste_par(numero):
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
'''








