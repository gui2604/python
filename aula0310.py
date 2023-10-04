'''
travalinguas = "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."

travalinguas = travalinguas.replace(".", "")
#print(travalinguas)
travalinguas = travalinguas.lower()
#print(travalinguas)
travalinguas = travalinguas.split(" ")
#print(travalinguas)
#nome = "Danilo"
#nome = nome.lower()
#nome[0] = "d"

#percorre a lista do travalinguas que foi convertida em lista no "split", logo ele percorrerá por palavras, se nao der o split, ele percorre por letras por percorrer uma string, nao uma lista.
palavras = {}
for palavra in travalinguas:
    if palavra not in palavras.keys():
        palavras[palavra] = 1
    else:
        palavras[palavra] += 1
    print(palavras)


travalingua1 = "O rato roeu a rica roupa do rei de Roma! A rainha raivosa rasgou o resto e depois resolveu remendar!"
travalingua2 = "Se percebeste, percebeste. Se não percebeste, faz que percebeste para que eu perceba que tu percebeste. Percebeste?"

def conta_palavras(travalinguas):
    for char in '!@#"$%&*()_.,><?-/':
        travalinguas.replace(char, '')
    travalinguas = travalinguas.lower().split(" ")
    return travalinguas

print(conta_palavras(travalingua1))
print(conta_palavras(travalingua2))

palavras = {}
for palavra in conta_palavras(travalingua1):
    if palavra not in palavras.keys():
        palavras[palavra] = 1
    else:
        palavras[palavra] += 1
    print(palavras)

palavras = {}
for palavra in conta_palavras(travalingua2):
    if palavra not in palavras.keys():
        palavras[palavra] = 1
    else:
        palavras[palavra] += 1
    print(palavras)

def conta_palavras(travalinguas):
    for char in '!@#"$%&*()_.,><?-/':
        travalinguas.replace(char, '')
    travalinguas = travalinguas.lower().split(" ")
    return travalinguas

nome "danilo é humilde, esse danilo"
sentenca = ''
for palavra in nome.replace(',', '').split(" "):
    if palavra != "danilo":
        sentenca += palavra + ' '
    else:
        palavra = palavra.replace("d", "D")
        sentenca += palavra + ' '
print(sentenca)

frase = "não é íntegro ômega três no último mês"
letras_zuadas = {"ãàáâ" : "a", "éêè" : "e", "íîì" : "i", "óôõò" : "o", "úù" : "u"}
for letra_zuada in letras_zuadas.keys():
    for letra in letra_zuada:
        frase = frase.replace(letra, letras_zuadas[letra_zuada])
print(frase)

import pandas as pd
dados = pd.read_csv("dado_mg.csv") #sep=";" ja soluciona o problema
print(dados)
print("ALO1")
print(dados.columns[0].split(";"))
print("ALO2")
print(dados.values[0][0].split(";"))
print("ALO3")
print(dados.values[0])
print("ALO4")
print(dados.values[0][0])
print("ALO5")
print(dados.values[1][0].split(";"))

dados_processados = {}
j = 0
for key in dados.columns[0].split(";"):
    dados_processados[key] = []
    for i in range(3):
        dados_processados[key].append(dados.values[i][0].split(";")[j])
    j += 1
dados_processados = pd.DataFrame(dados_processados)
print(dados_processados)

lista = ['a', 'b', 'c']
while True:
    try:
        i = int(input("diga um numero:"))
        print(lista[i])
        #print(1+"3")
        #break
        letra = lista[i]
    #o except especifica uma exceção caso o try não funcione
    except ValueError:
        print("seu bobão era pra ser um número")
        raise #força o erro do código (não serve para UX, mas para testes do DEV)
        raise ValueError("Você é muito bobão") #customizar mensagem de erro
    except IndexError:
        print(f"Tem que ser 0 e {len(lista)-1}")
    except NameError:
        print("taçguma variável não foi definida")
    #essa estrutura é para não crachar código e exibir qual é a exceção encontrada pelo erro causado exibindo-o após armazenado na variável "e"
    except Exception as e:
        print(e)
    #o else só é executado quando o "try" funciona
    else:
        print(letra)
        print("operação realizada com sucesso")
        break
    #o finally é executado sempre, independentemente da exceção que cair, mesmo se houver um break
    finally:
        print("sou printado sempre e não sirvo pra muita coisa")

#reescreva este código usando try except
while True:
    num1 = float(input("Diga um número: "))
    num2= float(input("Diga o segundo número: "))

    if num1 != 0:
        print(num2/num1)
        break
    else:
        print("nao pode dividir por zero seu bobão")
'''

while True:
    try:
        num1 = float(input("Diga um número: "))
        num2 = float(input("Diga o segundo número: "))
        print(num2/num1)
    except ValueError:
        print("Digite números válido!")
    except ZeroDivisionError:
        print("Não pode dividir números por zero, digite outro valor para num2!")
    else:
        print("Volte sempre à calculadora!")
        break
    #finally:
        #print("Você realizou um cálculo")