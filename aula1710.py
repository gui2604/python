'''
#correção cp
def obriga_opcao(msg,dicionario_opcoes):
    resposta = input(msg)
    while resposta not in dicionario_opcoes.keys():
        for key in dicionario_opcoes.keys():
            print(f"{key}:{dicionario_opcoes[key]}")
        resposta = input(msg)
    return resposta

def remover():
    dic = {str(i):carros['model'][i] for i in range(len(carros['model']))}
    #dic = {}
    #for i in range(len(carros['model'])):
        #dic[str(i)] = carros['model'][i]
    opcao = int(obriga_opcao("qual carro você deseja remover?", dic))
'''
'''
import pandas as pd
import requests

def login():
    usuario = obriga_opcao("Diga seu usuario : ",["Danilo"],3)
    if usuario:
        senha = obriga_opcao("Diga sua senha : ",['1234'],3)
    else:
        return False
    return senha and usuario

def altera_preco():
    for i in range(len(vinhos['tipo'])):
        print(f"{i} - {vinhos['tipo'][i]}")
    vinho = int(obriga_opcao("De que vinho vc vai alterar ? ",lista_vinhos))
    while True:
        try:
            preco = float(input("Diga o novo preÃ§o : "))
        except ValueError:
            print("Voce deve digitar um preçoo válido, Ex: 99.90")
        else:
            vinhos['preço'][vinho] = preco
            print("Alterado com sucesso")
            break
    return
def remove_produto():
    for i in range(len(vinhos['tipo'])):
        print(f"{i} - {vinhos['tipo'][i]}")
    vinho = int(obriga_opcao("Qual vinho vc vai remover ? ",lista_vinhos))
    for key in vinhos.keys():
        vinhos[key].pop(vinho)
    return
tipos = {key: type(vinhos[key][0] for key in vinhos.keys())}
def cadastra_produto():
    for key in vinhos.keys():
        if tipos[key] is not str:
            while True:
                info = input(f"Diga o/a novo/a {key}:")
                try:
                    flag = "tem que ser um numero"
                    if tipos[key] is int:
                        info = int(info)
                    else:
                        flag += " com ponto"
                        info = float(info)
                except ValueError:
                    print(flag)
                else:
                    vinhos[key].append(info)
                    break
        else:
            info = input(f"Diga o/a {key}")
            vinhos[key].append(info)

def cadastra_produto():
    """for key in vinhos.keys():
        if type(vinhos[key][0]) is not str:
            if type(vinhos[key][0]) is float:
                while True:
                    try:
                        info = float(input(f"Diga o/a novo/a {key} : "))
                        vinhos[key].append(info)
                    except:
                        print("precisa ser um numero com ponto")
            else:
                while True:
                    try:
                        info = int(input(f"Diga o/a novo/a {key} : "))
                        vinhos[key].append(info)
                    except:
                        print("precisa ser um numero inteiro")
        else:
            info = input(f"Diga o/a novo/a {key} : ")
            vinhos[key].append(info)
    return"""''

def obriga_opcao(msg,lista_opcoes,max_tentativas = None):
    resposta = input(msg)
    tentativas = 1
    while resposta not in lista_opcoes:
        print("Digite uma opÃ§Ã£o vÃ¡lida! ")
        resposta = input(msg)
        if max_tentativas:
            if tentativas>=max_tentativas-1:
                print("Sai Hacker")
                return False
            tentativas +=1
    return resposta
def printa_dicionarios(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dicionarios(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return
def cep():
    while True:
        cep = input("Diga seu cep")
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        if response.status_code == 200:
            printa_dicionarios(response.json())
            certo = obriga_opcao("TÃ¡ td certo ? (s/n) ",['s','n'])
            if certo == 's':
                response = response.json()
                num = input("Diga seu numero : ")
                response['nÃºmero'] = num
                return response

vinhos = {
    'tipo' : ['tinto', 'rosÃ©', 'seco', 'branco', 'suave'],
    '% alcoÃ³lico' : [11,15,12,13,10],
    'safra' : [1958,1962,1970,1994,2002],
    'preÃ§o' : [100.0,130.0,20.0,25.0,50.0],
    'Nacionalidade' : ['chileno','argentino','franÃ§Ãªs','italiano','jundiaiense'],
    'estoque' : [1,20,30,40,50]
}
compra = {
    'valor total' : 0,
    'endereÃ§o' : {},
    'vinhos' : {}
}
printa_dicionarios(compra)
print(pd.DataFrame(vinhos))
c_f = obriga_opcao("Voce Ã© cliente ou funcionÃ¡rio ? (c/f) ",['c','f'])
lista_vinhos = [str(i) for i in range(len(vinhos['tipo']))]

if c_f == 'c':
    print("Seja bem vindo!!! ")
    compra['endereÃ§o'] = cep()
    while True:
        print("Essas sÃ£o nossas opÃ§Ãµes de vinhos: ")
        for i in range(len(vinhos['tipo'])):
            print(f"{i} - {vinhos['tipo'][i]}")
        opcao = int(obriga_opcao("Por qual vc se interesou ?",lista_vinhos))
        for key in vinhos.keys():
            print(f"{key} : {vinhos[key][opcao]}")
        comprar = obriga_opcao("Voce quer levar ?(s/n)",['s','n'])
        if comprar == 's':
            if vinhos['estoque'][opcao]==0:
                print(f"Desculpa, nÃ£o temos mais estoque de {vinhos['tipo'][opcao]}")
                continue
            else:
                vinhos['estoque'][opcao]-=1
            compra['valor total'] += vinhos['preÃ§o'][opcao]
            nome = vinhos['tipo'][opcao]
            if nome not in compra['vinhos'].keys():
                compra['vinhos'][nome] = 1
            else:
                compra['vinhos'][nome] += 1

        continuar = obriga_opcao("Vc quer ver mais vinhos?(s/n) ",['s','n'])
        if continuar == 'n':
            print("Obrigado pela sua compra:")
            printa_dicionarios(compra)
            break
else:
    if login():
        while True:
            operacao = obriga_opcao("Qual operacao vc deseja realizar ?\n0-Alterar preÃ§o"
                                    "\n1-Remover produto\n2-Cadastrar produto"
                                    "\n3-Sair\n-> ",['0','1','2','3'])
            if operacao == '0':
                altera_preco()
            elif operacao == '1':
                remove_produto()
                lista_vinhos = [str(i) for i in range(len(vinhos['tipo']))]
            elif operacao == '2':
                cadastra_produto()
                lista_vinhos = [str(i) for i in range(len(vinhos['tipo']))]
            else:
                print("OperaÃ§Ã£o realizada com sucesso!")
                print(pd.DataFrame(vinhos))
                break
    else:
        print("Encerrando programa!")
'''
'''
def acha_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        candidato = lista[i]
        if candidato > maior:
            maior = candidato
            indice_maior = i
    return indice_maior
print(acha_maior("Guilherme"))
'''
'''
def acha_maior(lista):
    msg = "Deve ser uma lista de inteiros"
    if type(lista) is not list:
        raise TypeError(msg)
    for letra in lista:
        if type(letra) not in [float, int]:
            raise TypeError(msg)
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        candidato = lista[i]
        if candidato > maior:
            maior = candidato
            indice_maior = i
    return indice_maior
#print(acha_maior("Guilherme"))
#print(acha_maior([1,6,3,4,5]))
#print(acha_maior(["a","b","c"]))
'''
def buscar_menor(lista):
    menor = float('inf')
    indice_do_menor = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_do_menor = i
    return indice_do_menor

lista = [4,2,5,7,6,1,3]
'''
lista_ordenada = []

print(lista[2:])
#while len(lista) != 0:
while lista:
    menor = lista[buscar_menor(lista)]
    lista.pop(buscar_menor(lista))
    lista_ordenada.append(menor)
#print(lista)
#print(lista_ordenada)

teste1 = [1,2]
teste2 = []
print(bool(teste1))#True
print(bool(teste2))#False
'''

for i in range(len(lista)):
    indice_delay = buscar_menor(lista[i:])
    print(lista[i:])
    print(indice_delay)
    indice_real = indice_delay + i
    aux = lista[i]
    lista[i] = lista[indice_real]
    lista[indice_real] = aux
    print(lista)
    print()
