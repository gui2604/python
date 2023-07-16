#percorre a lista por elemento (for salario in salarios)
def i_erre(salario):
    #for salario in salarios:
    if salario < 2112:
        print(f"O IR de R${salario} é isento, portanto paga {salario * 0}")
    elif salario < 2826:
        print(f"O IR de R${salario} é 7,5%, portanto paga {salario * 0.075}")
    elif salario < 3751:
        print(f"O IR de R${salario} é 15%, portanto paga {salario * 0.15}")
    elif salario < 4664:
        print(f"O IR de R${salario} é 22,5%, portanto paga {salario * 0.225}")
    else:
        print("O IR de R${} é 27,5%, portanto paga {}".format(salario, salario * 0.275))
    return
i_erre(4000)