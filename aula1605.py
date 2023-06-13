'''
num = 2
def par_ou_impar(numero):
    print(numero)
    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é ímpar")
    return
par_ou_impar(5)
#print(numero) vai dar erro, pq numero é uma variável global, não local
'''
'''
#função que verifica vogal sem parâmetro
def vogal_ou_consoante():
    letra = input("Digite uma letra: ")
    if (letra == "a" or letra == "o" or letra == "i" or letra == "o" or letra == "u"):
        print(f"{letra} é vogal")
    else:
        print(f"{letra} é consoante")
    return 
vogal_ou_consoante()
'''
'''
#função que verifica vogal com parâmetro
def vogal_ou_consoante(letra):

    if (letra == "a" or letra == "o" or letra == "i" or letra == "o" or letra == "u"):
        return True
    else:
        return False

letra_digitada = vogal_ou_consoante(input("digite uma letra: "))
print(letra_digitada)
'''
'''
#correção usando lista
def vogal_ou_n(letra):
    if letra in ["a","e","i","o","u"]:
        print(f"{letra} é vogal")
    else:
        print(f"{letra} é consoante")
    return
vogal_ou_n("a")
vogal_ou_n("b")
vogal_ou_n("c")
vogal_ou_n("e")
vogal_ou_n("f")
print(" ")
for letra in "danilo":
    vogal_ou_n(letra)
'''
'''
def vogal_ou_n(letras):
    qnt_vogais = 0
    for letra in letras:
        if letra in ["a","e","i","o","u"]:
            qnt_vogais += 1
            print(f"{letra} é vogal")
        else:
            print(f"{letra} é consoante")
    return qnt_vogais

qnt = vogal_ou_n("danilo")
print(qnt)
#print(qnt_vogais) esse print da erro pq essa variável pode ser usada apenas dentro da função
'''
'''
#recebe 2 numeros, retorna a soma
#recebe 2 numeros, retorna a subtracao
#recebe 2 numeros, retorna a multiplicação
#recebe 2 numeros, retorna a divisão

def soma(num1,num2):
    return num1 + num2
def subtracao(num1,num2):
    return num1 - num2
def multiplicacao(num1,num2):
    return num1 * num2
def divisao(num1,num2):
    return num1 / num2 

#qtd = int(input("qnts operacoes vc quer fazer?"))
res = soma(2,3)
print(res)
res = subtracao(2,3)
print(res)
res = multiplicacao(2,3)
print(res)
res = divisao(2,3)
print(res)
'''
'''
#pergunte qual operação o usuário quer fazer e chame a função correspondente, verifique se ele digitou numeros validos fazendo uma função pra isso

def soma(num1,num2):
    return num1 + num2

def subtracao(num1,num2):
    return num1 - num2

def multiplicacao(num1,num2):
    return num1 * num2

def divisao(num1,num2):
    return num1 / num2

def verificar_se_numero(num):
    if num.isnumeric():
        num = int(num)
        return num
    else:
        while not num.isnumeric():
            num = input("digite um numero valido:")
        num = int(num)
        return num

def checa_pergunta(opcoes_cadastradas):
    pergunta = input("qual operação você quer fazer 1-soma 2-subtracao 3-multiplicacao 4-divisao: ")
    while not pergunta in opcoes_cadastradas:
        pergunta = input("qual operação você quer fazer 1-soma 2-subtracao 3-multiplicacao 4-divisao: ")
    return pergunta

pergunta = checa_pergunta(["1","2","3","4"])

if pergunta == "1":
    num1 = verificar_se_numero(input("digite o primeiro numero: "))
    num2 = verificar_se_numero(input("digite o segundo numero: "))
    operacao = soma(num1,num2)
    print(f"a soma vale: {operacao}")
elif pergunta == "2":
    num1 = verificar_se_numero(input("digite o primeiro numero: "))
    num2 = verificar_se_numero(input("digite o segundo numero: "))
    operacao = subtracao(num1, num2)
    print(f"a subtracao vale: {operacao}")
elif pergunta == "3":
    num1 = verificar_se_numero(input("digite o primeiro numero: "))
    num2 = verificar_se_numero(input("digite o segundo numero: "))
    operacao = multiplicacao(num1, num2)
    print(f"a multiplicacao vale: {operacao}")
else:
    num1 = verificar_se_numero(input("digite o primeiro numero: "))
    num2 = verificar_se_numero(input("digite o segundo numero: "))
    operacao = divisao(num1, num2)
    print(f"a divisao vale: {operacao}")
'''
'''
lista_de_vinhos = ["rose","branco","tinto"]
msg = "qual vinho vc quer? (rose, branco, tinto)"
vinho = checa_pergunta(msg, lista_de_vinhos)
'''
'''
# função c/ 2 parametros: sao listas com nomes e preços
# percorre a lista de preços, encontre o mais caro e seu índice
# retorne o vinho com o maior índice

def checar(lista1,lista2):
    maior_num = float('-inf')
    for i in range(len(lista1)):
        if lista1[i] > maior_num:
            maior_num = lista1[i]
            indice_do_maior = i
    return lista2[indice_do_maior]

precos = [100,300,200]
nomes = ["tinto","rose","branco"]
print(f"{checar(precos,nomes)}, é o vinho de maior valor")
'''
'''
#versao do professor do ex acima
def acha_maior(valores,nomes):
    maior = valores[0]
    local_maior = 0
    for i in range(len(valores)):
        if valores[i] > maior:
            maior = valores[i]
            local_maior = i
    return nomes[local_maior]

vinhos = ["tinto","rose","branco","suave","fedido","cheiroso"]
precos = [100,200,150,75,237,50]

vinho_mais_caro = acha_maior(precos, vinhos)
print(vinho_mais_caro)
'''
'''
#agora faça uma função que ache também o vinho mais barato;
#depois, pergunte ao usuário se ele quer achar o vinho mais caro ou o mais barato e faça o que ele pedir chamando a função correspondente.
def checar_maior(lista1,lista2):
    maior_num = float('-inf')
    for i in range(len(lista1)):
        if lista1[i] > maior_num:
            maior_num = lista1[i]
            indice_do_maior = i
    return lista2[indice_do_maior]

def checar_menor(lista1,lista2):
    menor_num = float('inf')
    for i in range(len(lista1)):
        if lista1[i] < menor_num:
            menor_num = lista1[i]
            indice_do_menor = i
    return lista2[indice_do_menor]

precos = [100,200,150,75,237,50]
vinhos = ["tinto","rose","branco","suave","fedido","cheiroso"]

pergunta = input("voce quer achar o vinho mais: 1-caro ou 2-barato? ")
while not pergunta in ["1","2"]:
    pergunta = input("voce quer achar o vinho mais: 1-caro ou 2-barato? Escolha uma opção válida! ")
if pergunta == "1":
    print(f"{checar_maior(precos,vinhos)} é o mais caro")
else:
    print(f"{checar_menor(precos,vinhos)} é o mais barato")
'''
'''
#ache media função
def ache_media(valores):
    soma = 0
    for valor in valores:
        soma += valor
    return soma / len(valores)

vinhos = ["tinto","rose","branco","suave","fedido","cheiroso"]
precos = [100,200,150,75,237,50]

a = ache_media(precos)
print(a)
'''


def meu_input_numerico():
    num = input("diga um numero: ")
    if num.isnumeric():
        num = int(num)
        return num
    else:
        return meu_input_numerico()
numero = meu_input_numerico()
print(numero)