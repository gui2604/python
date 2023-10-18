#Guilherme Barreto Santos - rm97674

#Exercício 1:
frase = "Concluímos que chegamos à conclusão que não concluímos nada. Por isso, conclui-se que a conclusão será concluída quando todas tiverem concluído que já é tempo de concluir uma conclusão."

def formatacao(frase):
    letras_acentuadas = {"áàã": "a", "éè": "e", "íì": "i"}
    for vogais_acentuadas in letras_acentuadas.keys():
        for vogal_zuada in vogais_acentuadas:
            frase = frase.replace(vogal_zuada, letras_acentuadas[vogais_acentuadas])
    frase = frase.lower()
    for char_especial in ".,!@#$%&*-~()[]{}:;?/|'^":
        frase = frase.replace(char_especial, '')
    frase = frase.split(" ")
    return frase

def contagem(lista):
    contagem = {}
    for palavra in lista:
        if palavra not in contagem:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    return contagem

def print_dic(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            print_dic(dic[key])
        else:
            print(f"{key} : {dic[key]}")

print(print_dic(contagem(formatacao(frase))))
print()

#Exercício 2:
carros = {
    "model": ["Mazda RX4", "Mazda RX4 Wag", "Datsun 710", "Hornet 4 Drive", "Hornet Sportabout", "Valiant", "Duster 360", "Merc 240D", "Merc 230", "Merc 280", "Merc 280C", "Merc 450SE", "Merc 450SL", "Merc 450SLC", "Cadillac Fleetwood", "Lincoln Continental", "Chrysler Imperial", "Fiat 128", "Honda Civic", "Toyota Corolla", "Toyota Corona", "Dodge Challenger", "AMC Javelin", "Camaro Z28", "Pontiac Firebird", "Fiat X1-9", "Porsche 914-2", "Lotus Europa", "Ford Pantera L", "Ferrari Dino", "Maserati Bora", "Volvo 142E"],
    "mpg": [21.0, 21.0, 22.8, 21.4, 18.7, 18.1, 14.3, 24.4, 22.8, 19.2, 17.8, 16.4, 17.3, 15.2, 10.4, 10.4, 14.7, 32.4, 30.4, 33.9, 21.5, 15.5, 15.2, 13.3, 19.2, 27.3, 26.0, 30.4, 15.8, 19.7, 15.0, 21.4],
    "cyl": [6, 6, 4, 6, 8, 6, 8, 4, 4, 6, 6, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 8, 8, 8, 8, 4, 4, 4, 8, 6, 8, 4],
    "disp": [160.0, 160.0, 108.0, 258.0, 360.0, 225.0, 360.0, 146.7, 140.8, 167.6, 167.6, 275.8, 275.8, 275.8, 472.0, 460.0, 440.0, 78.7, 75.7, 71.1, 120.1, 318.0, 304.0, 350.0, 400.0, 79.0, 120.3, 95.1, 351.0, 145.0, 301.0, 121.0],
    "hp": [110, 110, 93, 110, 175, 105, 245, 62, 95, 123, 123, 180, 180, 180, 205, 215, 230, 66, 52, 65, 97, 150, 150, 245, 175, 66, 91, 113, 264, 175, 335, 109],
    "drat": [3.9, 3.9, 3.85, 3.08, 3.15, 2.76, 3.21, 3.69, 3.92, 3.92, 3.92, 3.07, 3.07, 3.07, 2.93, 3.0, 3.23, 4.08, 4.93, 4.22, 3.7, 2.76, 3.15, 3.73, 3.08, 4.08, 4.43, 3.77, 4.22, 3.62, 3.54, 4.11],
    "wt": [2.62, 2.875, 2.32, 3.215, 3.44, 3.46, 3.57, 3.19, 3.15, 3.44, 3.44, 4.07, 3.73, 3.78, 5.25, 5.424, 5.345, 2.2, 1.615, 1.835, 2.465, 3.52, 3.435, 3.84, 3.845, 1.935, 2.14, 1.513, 3.17, 2.77, 3.57, 2.78],
    "qsec": [16.46, 17.02, 18.61, 19.44, 17.02, 20.22, 15.84, 20.0, 22.9, 18.3, 18.9, 17.4, 17.6, 18.0, 17.98, 17.82, 17.42, 19.47, 18.52, 19.9, 20.01, 16.87, 17.3, 15.41, 17.05, 18.9, 16.7, 16.9, 14.5, 15.5, 14.6, 18.6],
    "vs": [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    "am": [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    "gear": [4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 4, 4, 4, 3, 3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 4],
    "carb": [4, 4, 1, 1, 2, 1, 4, 2, 2, 4, 4, 3, 3, 3, 4, 4, 4, 1, 2, 1, 1, 2, 2, 4, 2, 1, 2, 2, 4, 6, 8, 2]
}
for key in carros.keys():
    print(key)
print()

for i in range(len(carros["hp"])):
    print(carros["hp"][i])
print()

def buscar_maior(lista):
    maior = float('-inf')
    indice_do_maior = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indice_do_maior = i
    return indice_do_maior

def buscar_menor(lista):
    menor = float('inf')
    indice_do_menor = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_do_menor = i
    return indice_do_menor

def forca_opcao(mensagem, lista):
    pergunta = input(mensagem)
    while pergunta not in lista:
        print("Digite uma opção válida!")
        pergunta = input(mensagem)
    return pergunta

def cadastrar():
    for key in carros.keys():
        info = input(f"Digite o/a {key} do carro\nR:")
        carros[key].append(info)
    print("Carro cadastrado com sucesso!")
    return

def excluir():
    for i in range(len(carros["model"])):
        print(f"{i}: {carros['model'][i]}")

    opcao = int(forca_opcao(f"Qual carro deseja excluir?\n Digite o número correspondente do carro. Apenas 0 a {len(carros['model']) - 1}\nR:", [str(i) for i in range(len(carros['model']))]))
    for key in carros.keys():
        carros[key].pop(opcao)
    print("Carro excluído com sucesso!")
    return

print("Boas vindas ao menu de carros!")
while True:
    resposta = int(forca_opcao("Você quer: 1- consultar o carro mais potente ou 2- consultar o carro menos potente, 3- cadastrar um novo carro, 4- excluir um carro existente. Digite as opções (1, 2, 3 ou 4)\nR:", ["1","2", "3", "4"]))
    if resposta == 1:
        u = buscar_maior(carros["hp"])
        for key in carros.keys():
            print(f"{key}: {carros[key][u]}")
    elif resposta == 2:
        u = buscar_menor(carros["hp"])
        for key in carros.keys():
            print(f"{key}: {carros[key][u]}")
    elif resposta == 3:
        cadastrar()
    else:
        excluir()
    parar = forca_opcao("quer continuar consultando(s/n)?", ["s", "n"])
    if parar == "n":
        break

