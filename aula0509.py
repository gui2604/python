#pergunte para o usuário se ele é cliente ou funcionário
#se for cliente, de as opções de whiskeys da casa e pergunte seu endereço, pergunte informações a respeito
#de qual ele quer ver, pergunte se vai comprar o whiskey escolhido no item anterior caso queira, adicione ao carrinho
#dele o vinho e seu preço
#import pandas as pd
whiskeys = {
    'tipo': ['bourbon', 'blended', 'scotch', 'single malt', 'double malt'],
    '%alcoolico': [41, 50, 35, 62, 37],
    'volume(ml)': [1000, 750, 50, 100, 2000],
    'idade': [15, 12, 8, 8, 10],
    'preço': [14, 23, 541, 65, 999],
    'marca': ['Jack Daniels', 'White Horse', 'Passport', 'Johnie Walker', 'Chanceler']
}
#print(pd.DataFrame(whiskeys))

def forca_opcao(msg, lista_opcoes):
    resposta = input(msg)
    while resposta not in lista_opcoes:
        print("Digite uma opção cadastrada!")
        resposta = input(msg)
    return resposta

compra = {
    'valor total': 0,
    'garrafas': {},
    'endereco': {
        'rua':'',
        'numero': '',
        'cep': '',
        'bairro': '',
        'cidade': ''
    },
    'nome': ''
}
pergunta = (forca_opcao("Você é (1)Cliente ou (2)Funcionário?", ["1","2"]))

if pergunta == "1":
    nome = input("Qual seu nome?")
    compra['nome'] = nome
    for key in compra['endereco'].keys():
        info = input(f"Diga seu/a {key}: ")
        compra['endereco'][key] = info
    print(f"Seja bem vindo {nome}")
    while True:
        print("As opções de whiskeys são:")
        for i in range(len(whiskeys['marca'])):
            print(f"{i}:{whiskeys['marca'][i]}")
        opcao = int(forca_opcao("Quer ver as informações de qual whiskey?", ["0","1","2","3","4"]))
        print("A informações do whiskey escolhidos são:")
        for key in whiskeys.keys():
            print(f"{key}:{whiskeys[key][opcao]}")
        comprar = (forca_opcao("Você vai levar (s/n)?", ["s","n"]))
        if comprar == "s":
            compra['valor total'] += whiskeys['preço'][opcao]
            marca = whiskeys['marca'][opcao]
            if marca not in compra['garrafas']:
                compra['garrafas'][marca] = 1
            else:
                compra['garrafas'][marca] += 1

        continuar = forca_opcao(("Você quer comprar mais whiskeys(s/n)?"), ['s','n'])
        if continuar == 'n':
            print("Resumo do seu pedido: ")
            for key in compra.keys():
                if type(compra[key]) is dict:
                    for key2 in compra[key].keys():
                        print(f"{key2}: {compra[key][key2]}")
                else:
                    print(f"{key}: {compra[key]}")
            break
