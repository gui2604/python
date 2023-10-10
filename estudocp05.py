'''
1º Exercício:
	- tirar pontuação de frase
	- deixar tudo minúsculo
	- adicionar as palavras separadamente nas chaves de um dicionário
	'''

frase_qualquer = "~Olá! Você está bem? Espero que sim. O @céu está lindo hoje! #Vamos celebrar &festejar. Ei, você! Sim, você! 12345, 6789. Palavras?! Sim, palavras: 'alegria', 'amor', 'paz'. %$#@! Agora é ^hora de partir. Adeus!"

#função para retirar caracteres especiais e deixar minúsculo
def formatar(frase):
    for char_especial in '!@#~$%&*()_.,><?-/"':
        frase = frase.replace(char_especial, '')
    frase = frase.lower()
    return frase

 # função para remover acentos das palavras de uma frase e transformar cada palavra em um valor da lista
 def acentos(frase):
    letras_acentuadas = {"ãàáâ": "a", "éêè": "e", "íîì": "i", "óôõò": "o", "úù": "u"}
    for vogais_acentuadas in letras_acentuadas.keys(): #percurso pelas chaves do dicionário
         for vogal_acentuada in vogais_acentuadas: #percorre cada vogal de cada chave de vogais
             frase = frase.replace(vogal_acentuada, letras_acentuadas[vogais_acentuadas])
    frase = frase.split(" ")
    return frase

def formatacao(frase):
    dicionario_zuadas = {"ãàáâ": "a", "éêè": "e", "íîì": "i", "óôõò": "o", "úù": "u"} #dicionário com vogais acentudadas a serem substituídas por voagsi sem acento
    for char_especial in '!@#~$%&*()_.^,><?-/"': #loop nos caracteres especiais
        frase = frase.replace(char_especial, '') #cada caracter especiais sendo substituído por nada a cada loop
    frase = frase.lower() #transforma em minúsculo
    for chave_zuada in dicionario_zuadas.keys(): #percurso pelas chaves do dicionário
        for vogal_zuada in chave_zuada: #percorre cada vogal acentuada de cada chave de vogais
            frase = frase.replace(vogal_zuada, dicionario_zuadas[chave_zuada]) #substitui cada vogal zuada pelo valor de cada chave, que são as vogais sem acento
    frase = frase.split(" ") #transforma em uma lista
    return frase

print(frase_qualquer)
print(formatacao(frase_qualquer))
lista_de_palavras_formatadas = formatacao(frase_qualquer)

#- contar quantas tem de cada palavra nos valores das chaves

def contar(lista):
    contagem = {}
    for palavra in lista:
        if palavra not in contagem.keys(): #aqui "contagem" pode ser sem o método .keys(), mas é boas práticas colocá-lo para especificar que estamos percorrendo as chaves dele
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    return contagem

def print_dic(dic): #declara a função que printa as chaves do dicionário e seus valores
    for key in dic.keys(): #percorre as chaves do dicionário
        if type(dic[key]) is dict: #verifica se o valor da chave do dicionário é um dicionário
            print_dic(dic[key]) #caso o valor da chave do dicionário for um dicionário, vai chamar a função novamente repetindo o ciclo
        else: #caso o valor da chave do dicionário não for um dicionário
            print(f"{key} : {dic[key]}") #vai printar a chave com seu respectivo valor
    return #essa função não retorna nada, porque a saída de dados printando o dicionário ja acontece nos prints do else

print(print_dic(contar(lista_de_palavras_formatadas)))

'''
2º Exercício:
	Documento com especificações de carros
	- função que acha o carro com maior potencia
	- trazer todas as informações do carro que tem a maior potência
	- adicionar a funcionalidade de poder cadastrar um carro com todas as informações
	- adicionar a funcionalidade de poder excluir um carro cadastrado
'''
carros = {
    "marca": ["hb20", "polo", "celta", "fusca"],
    "potencia": [200, 1000, 100, 8000],
    "preco": [50, 100, 125, 15000],
    "ano": [1990, 2000, 2010, 1940],
    "montadora": ["hyundai", "wolks", "chevrolet", "wolkswagen"]
}
def forca_opcao(mensagem, lista):
    pergunta = input(mensagem)
    while not pergunta in lista:
        print("Digite uma opção válida!")
        pergunta = input(mensagem)
    return pergunta

# - função que acha o carro com maior potencia
def acha_maior_potencia():
    maior = carros["potencia"][0]
    indice_do_maior = 0
    for i in range(len(carros["potencia"])):
        if carros["potencia"][i] > maior:
            indice_do_maior = i
    return indice_do_maior

#- trazer todas as informações do carro que tem a maior potência
for key in carros.keys():
    print(f"{key} : {carros[key][acha_maior_potencia()]}")

# - adicionar a funcionalidade de poder cadastrar um carro com todas as informações
def cadastrar():
    print("Bem vindo ao cadastro de carros")
    for key in carros.keys():
        info = input(f"Digite o/a {key} do carro")
        carros[key].append(info)
    return

#- adicionar a funcionalidade de poder excluir um carro cadastrado
def excluir():
    print("Você está excluindo um carro")
    opcao = int(forca_opcao("Qual carro deseja excluir? 1-hb20 2-polo 3-celta 4-fusca", ["0","1","2","3"]))
    for key in carros.keys():
        carros[key].pop(opcao)
    return
