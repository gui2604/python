'''
frase = "a aranha arranha a rã. a rã arranha a aranha. nem a aranha arranha a rã. nem a rã arranha a aranha"
frase = frase.replace(".", "")
frase = frase.lower()
#print(frase)
#print("a" == "A") #o python diferencia maiúsculas e minúsculas (False)
#print(type(frase))
frase = frase.split(" ") #cria uma lista separando palavras em elementos da lista por meio dos espaços em branco
#print(type(frase))
#print(frase)

trava = {}
for palavra in frase:
    if palavra in trava.keys():
        trava[palavra] += 1
    else:
        trava[palavra] = 1
print(trava)
'''
#se for funcionário pergunte qual operação deseja realizar:
# 1- Cadastrar um novo whiskey
# 2- Atualizar o preço de um whiskey
# 3- Atualizar o estoque de um whiskey
# 4- Deletar um whiskey da tabela
import pandas as pd
whiskeys = {
    'tipo': ['bourbon', 'blended', 'scotch', 'single malt', 'double malt'],
    "Nacionalidade": ["chileno", "argentino", "françês", "italiano", "jundiaiense"],
    '%alcoolico': [41, 50, 35, 33, 28],
    'safra': [1958, 1962, 1970, 1994, 2002],
    'idade': [15, 12, 8, 8, 10],
    'preço': [100, 130, 20, 25, 50],
    'estoque': [3, 1, 5, 4, 2]
}
def ve_opcoes_whiskeys():
    opcoes = [str(i) for i in range(len(whiskeys["tipo"]))]
    return opcoes
opcoes = [str(i) for i in range(len(whiskeys["tipo"]))]
'''
opcoes = []
for i in range(len(whiskeys["tipo"])):
    opcoes.append(str(i))
'''
compra = {
    "nome": "",
    "endereço": {
        "rua": "",
        "numero": "",
        "cep": "",
        "bairro": "",
        "cidade": ""
    },
    "garrafas": {},
    "valor total": 0
}
#print(pd.DataFrame(whiskeys))
def forca_opcao(mensagem, lista_opcoes):
    resposta = input(mensagem)
    if resposta not in lista_opcoes:
        print("Opção Inválida, digite novamente!")
        return forca_opcao(mensagem, lista_opcoes)
    return resposta

def printa_dic(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dic(dic[key])
        else:
            print(f"{key}: {dic[key]}")
    return

def checa_estoque(opcao):
    if whiskeys["estoque"][opcao] == 0:
        return False
    whiskeys["estoque"][opcao] -= 1
    return True

def cadastrar():
    for key in whiskeys.keys():
        info = input(f"Diga o novo {key}: ")
        whiskeys[key].append(info)
    print(pd.DataFrame(whiskeys))
    return
def alterar(preco_estoque):
    print(f"De que whiskey vc irá alterar o {preco_estoque}")
    for i in range(len(whiskeys["tipo"])):
        print(f"{i} - {whiskeys[key][i]}")
    qual = int(forca_opcao(f"De que whiskey vc irá alterar o {preco_estoque}?", opcoes))
    novo = input(f"Diga o novo {preco_estoque}")
    whiskeys[preco_estoque][qual] = novo
    return

def remover():
    for i in range(len(whiskeys["tipo"])):
        print(f"{i} - {whiskeys[key][i]}")
    qual = int(forca_opcao((f"Qual será removida?", opcoes)))
pergunta = (forca_opcao("Você é (1)Cliente ou (2)Funcionário?", ["1","2"]))

if pergunta == "1":
    nome = input("Qual seu nome?")
    compra["nome"] = nome
    for key in compra["endereço"].keys():
        info = input(f"Diga seu {key}:")
        compra["endereço"][key] = info
    print(f"Seja bem vindo {nome}")
    while True:
        print("Essas são nossas opções de whiskeys:")
        for i in range(len(whiskeys["tipo"])):
            print(f"{i}: {whiskeys['tipo'][i]}")
        opcao = int(forca_opcao("Qual vinho lhe interessou mais?", opcoes))
        if whiskeys["estoque"][opcao] == 0:
            print(f"Não temos mais estoque do whiskey {whiskeys['tipo'][opcao]}!!!")
            continue
        print("As informações do whiskey escolhidas são:")
        for key in whiskeys.keys():
            print(f"{key}:{whiskeys[key][opcao]}")
        comprar = forca_opcao("Você vai comprar (s/n)", ["s", "n"])
        if comprar == "s":
            compra["valor total"] += whiskeys["preço"][opcao]
            tipo = whiskeys["tipo"][opcao]
            whiskeys["estoque"][opcao] -= 1
            if tipo not in compra["garrafas"].keys():
                compra["garrafas"][tipo] = 1
            else:
                compra["garrafas"][tipo] += 1
        continuar = forca_opcao("Quer comprar mais?(s/n)", ["s", "n"])
        if continuar == "n":
            print("Obrigado. Volte sempre! Resumo da sua compra:")
            printa_dic(compra)
            break
elif pergunta == "2":
    while True:
        opcao = forca_opcao("O que deseja fazer?\n1- Cadastrar um novo whiskey\n2- Atualizar o preço de um whiskey\n3- Atualizar o estoque de um whiskey\n4- Deletar um whiskey da tabela", ["1","2","3","4"])
        if opcao == "1":
            for key in whiskeys.keys():
                info = input(f"digite o/a {key} do novo whiskey:")
                whiskeys[key].append(info)
                print(f"Whiskey cadastrado com sucesso!")
                print(pd.DataFrame(whiskeys))
        elif opcao == "2":
            for i in range(len(whiskeys["tipo"])):
                print(f"{i}: {whiskeys['tipo'][i]}")
            opcao = forca_opcao("qual whiskey você quer atualizar o preço?", ve_opcoes_whiskeys())
            whiskeys["preço"][opcao] = input(f"digite o novo preço do whiskey {whiskeys['tipo'][opcao]}")
            print("Preço atualizado com sucesso!")
            print(pd.DataFrame(whiskeys["preço"]))
        elif opcao == "3":
            for i in range(len(whiskeys["tipo"])):
                print(f"{i}: {whiskeys['tipo'][i]}")
            opcao = forca_opcao("qual whiskey você quer atualizar o estoque?", ve_opcoes_whiskeys())
            whiskeys["preço"][opcao] = input(f"digite o novo valor de estoque do whiskey {whiskeys['tipo'][opcao]}")
            print(f"Estoque do whiskey {whiskeys['tipo'][opcao]} alterado com sucesso!")
            print(pd.DataFrame(whiskeys["estoque"]))
        else:
            for i in range(len(whiskeys["tipo"])):
                print(f"{i}: {whiskeys['tipo'][i]}")
            opcao = int(forca_opcao("qual whiskey você quer deletar o estoque?", ve_opcoes_whiskeys()))
            for key in whiskeys.keys():
                whiskeys[key].pop(opcao)
            print(pd.DataFrame(whiskeys))
            print("Whiskey deletado com sucesso")
        continuar = forca_opcao("Quer realizar mais operações(s/n)?", ["s", "n"])
        if continuar == "n":
            break

