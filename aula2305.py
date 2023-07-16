'''
#percorre a lista por elemento (for salario in salarios)
def i_erre(salarios):
    for salario in salarios:
        if salario < 2112:
            print(f"O IR de R${salario} é isento")
        elif salario < 2826:
            print(f"O IR de R${salario} é 7,5%")
        elif salario < 3751:
            print(f"O IR de R${salario} é 15%")
        elif salario < 4664:
            print(f"O IR de R${salario} é 22,5%")
        else:
            print(f"O IR de R${salario} é 27,5%")
    return

salarios = [1000, 10000, 1500, 3000, 4000]
i_erre(salarios)
'''
'''
#percorre a lista por índice e depois acessa o elemento pelo índice correspondente
def i_erre(salarios):
    for i in range(len(salarios)):
        if salarios[i] < 2112:
            print(f"O IR de R${salarios[i]} é isento")
        elif salarios[i] < 2826:
            print(f"O IR de R${salarios[i]} é 7,5%")
        elif salarios[i] < 3751:
            print(f"O IR de R${salarios[i]} é 15%")
        elif salarios[i] < 4664:
            print(f"O IR de R${salarios[i]} é 22,5%")
        else:
            print(f"O IR de R${salarios[i]} é 27,5%")
    return
salarios = [1000, 10000, 1500, 3000, 4000]
i_erre(salarios)
'''
'''
opcoes = ["continuar", "encerrar"]
def verifica_opcoes(msg, lista_opcoes):
    var = input(msg)
    while not var in lista_opcoes:
        print("errou")
        var = input(msg)
    return var
opcao = verifica_opcoes("vc quer encerrar ou continuar", opcoes)
print(opcao)
'''



