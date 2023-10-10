'''
lista = [0,1,2,3,4,5]
while True:
    try:
        i = int(input("Diga um número:"))
        print(lista[i])
        break
    except ValueError:
        print("Você não digitou um inteiro!")
    except IndexError:
        print(f"Deve ser entre 0 e {len(lista)-1}")
    except Exception as e:
        print(e)
    else:
        print("Operação realizada com sucesso!")
        break
    finally:
        print("N sirvo pra muita coisa")
'''
'''
#Reescreva utilizando tratamento de exceções:
while True:
    a = int(input("Diga o primeiro numero: "))
    b = int(input("Diga o segundo numero: "))
    if a != 0:
        print(b/a)
        break
    else:
        print("O primeiro número não pode ser zero!")

times = {
    "são paulo": "campeão",
    "corinthians": "sem tite",
    "palmeiras": "sem mundial",
    "santos": "idoso rebaixado"
}
time = input("Diga seu time: ")
while time not in times.keys():
    print(f"Vc deve digitar um desses: {times.keys()}")
    time = input("Diga seu time: ")
print(f"Você é um {times[time]}")


while True:
    try:
        flag = "primeiro"
        a = float(input("Diga o primeiro numero: "))
        flag = "segundo"
        b = float(input("Diga o segundo numero: "))
        resultado = b/a
    except ValueError:
        print(f"O {flag} numero está errado")
    except ZeroDivisionError:
        print("O primeiro número não pode ser zero!")
    else:
        print(resultado)
        break

times = {
    "são paulo": "campeão",
    "corinthians": "sem tite",
    "palmeiras": "sem mundial",
    "santos": "idoso rebaixado"
}
while True:
    time = input("Diga seu time: ")
    try:
        print(f"Vc deve digitar um desses: {times[time]}")
        break
    except KeyError:
        print(f"Você deve digitar um desses: {times.keys()}")
'''
