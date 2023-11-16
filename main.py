import json

def forca_opcao(mensagem, lista):
    pergunta = input(mensagem)
    while not pergunta in lista:
        print("Digite uma opção válida!")
        pergunta = input(mensagem)
    return pergunta

def print_dic(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            print(f"últimos dados medidos do {key}:")
            print_dic(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return

def fazer_login(usuario, senha, crm):
    i = 1
    while (usuario != "usuario123" or senha != "senha123" or crm != "123") and i != 3:
        print(f"Usuário e Senha incorretos ou CRM não encontrado. Digite novamente {i} de 3 tentativas restante.")
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        crm = input("CRM:\nR:")
        i += 1
        if i == 3 and (usuario != "usuario123" or senha != "senha123"):
            print(f"Usuário ou Senha incorretos. Limite máximo de tentativas excedido: {i} de 3 tentativas utilizadas.")
            return False
    return True

def cadastrar_paciente():
    print("Cadastro de pacientes:")
    novo_paciente = {}
    for key in pacientes[0].keys():
        if type(pacientes[0][key]) is not str:
            if type(pacientes[0][key]) is float:
                while True:
                    try:
                        info = float(input(f"Diga o/a novo {key}: "))
                        novo_paciente[key] = info
                        break
                    except ValueError:
                        print("Precisa ser um número com ponto")
                    except Exception as e:
                        print(e)
                        raise
            elif type(pacientes[0][key]) is dict:
                while True:
                    try:
                        with open("dadosComodos.json", "r") as arquivo:
                            dados_comodos = json.load(arquivo)
                            novo_paciente[key] = dados_comodos[key]
                            print(f"Os {key} do paciente registrados: {dados_comodos[key]} coletados do arquivo json foram cadastrados com sucesso!")
                            break
                    except FileNotFoundError:
                        print(f"Arquivo não encontrado! Pode estar inválido, verifique o caminho ou formato.")
                        raise
                    except Exception as e:
                        print(e)
                        raise
            else:
                while True:
                    try:
                        info = int(input(f"Diga o/a novo {key}: "))
                        novo_paciente[key] = info
                        break
                    except ValueError:
                        print("Precisa ser um número inteiro")
                    except Exception as e:
                        print(e)
                        raise
        else:
            info = input(f"Diga o/a novo {key}: ")
            novo_paciente[key] = info
    pacientes.append(novo_paciente)
    print("Paciente cadastrado com sucesso!")
    return

def alterar_paciente():
    print("Alterar dados de paciente:")
    for i in range(len(pacientes)):
        print(f"Paciente de número:({i}) - Nome do Paciente:{pacientes[0]['nome']}\n")
    opcao = int(forca_opcao(f"Digite o número correspondente do paciente que deseja alterar os dados, apenas 0 a {len(pacientes) - 1}\nR:", [str(i) for i in range(len(pacientes))]))
    for key in pacientes[0].keys():
        if type(pacientes[0][key]) is not str:
            if type(pacientes[0][key]) is float:
                while True:
                    try:
                        info = float(input(f"Diga o/a nova {key}: "))
                        pacientes[opcao][key] = info
                        break
                    except ValueError:
                        print("Precisa ser um número com ponto")
            elif type(pacientes[opcao][key]) is dict:
                try:
                    with open("novosDadosComodos.json", "r") as arquivo:
                        dados_comodos = json.load(arquivo)
                        pacientes[opcao][key] = dados_comodos[key]
                        print(f"Os {key} do paciente registrados: {dados_comodos[key]} coletados do arquivo json foram cadastrados com sucesso!")
                        break
                except FileNotFoundError:
                    print(f"Arquivo não encontrado! Pode estar inválido, verifique o caminho ou formato.")
                    raise
                except Exception as e:
                    print(e)
                    raise
            else:
                while True:
                    try:
                        info = int(input(f"Diga o/a novo {key}: "))
                        pacientes[opcao][key] = info
                        break
                    except ValueError:
                        print("Precisa ser um número inteiro")
        else:
            info = input(f"Diga o/a novo {key}: ")
            pacientes[opcao][key] = info
    print("Dados de paciente alterado com sucesso!")
    return

def deletar_paciente():
    print("Deletar paciente:")
    for i in range(len(pacientes)):
        print(f"Paciente de número:({i}) - Nome do Paciente:{pacientes[0]['nome']}\n")
    opcao = int(forca_opcao(f"Digite o número correspondente do paciente que deseja deletar do registro, apenas 0 a {len(pacientes) - 1}\nR:", [str(i) for i in range(len(pacientes))]))
    pacientes.pop(opcao)
    print("Paciente excluído com sucesso!")
    return

def consultar_paciente():
    print("Consultar Paciente:")
    for i in range(len(pacientes)):
        print(f"({i}) - {pacientes[i]['nome']}\n")
    opcao = int(forca_opcao(f"Digite o número correspondente do paciente que deseja consultar os dados, apenas 0 a {len(pacientes) - 1}\nR:", [str(i) for i in range(len(pacientes))]))
    print_dic(pacientes[opcao])
    return

pacientes = [
    {
        "nome": "João",
        "idade": 25,
        "endereco": "Rua X, Nº Y",
        "telefone": 11942792555,
        "email": "joao@email.com",
        "comodos": {
            "cozinha": {
                "luminosidade": 800,
                "temperatura": 35.7,
                "umidade": 50
            },
            "sala_de_estar": {
                "luminosidade": 500,
                "temperatura": 24.9,
                "umidade": 40
            }
        },
        "peso": 70.0,
        "altura": 1.75
    }
]

print("Boas vindas ao software da HealthGuard EnviroMonitor!")
usuario = input("Digite seu usuário\nR:")
senha = input("Digite sua senha\nR:")
crm = input("Digite seu CRM\nR:")
if fazer_login(usuario, senha, crm):
    while True:
        resposta = int(forca_opcao("Digite uma opção: 1- Cadastrar um paciente, 2- Alterar dados de um paciete, 3- Deletar um paciente, 4- Consultar os dados de um paciente, 5- Consultar todo o banco de dados de pacientes cadastrados ou 0- Sair\nR: ", ["1","2", "3", "4", "5", "0"]))
        if resposta == 1:
            cadastrar_paciente()
        elif resposta == 2:
            alterar_paciente()
        elif resposta == 3:
            deletar_paciente()
        elif resposta == 4:
            consultar_paciente()
        elif resposta == 5:
            for p in range(len(pacientes)):
                print_dic(pacientes[p])
        else:
            break
        parar = forca_opcao("quer continuar realizando operações(s/n)?", ["s", "n"])
        if parar == "n":
            break
    #Gerar arquivo externo com o registro completo do dicionário de paciente
    pacientes_json = json.dumps(pacientes, indent=1)
    with open("dadosPacientes.json", "w") as arquivo_json:
        arquivo_json.write(pacientes_json)
    print("Arquivo de registro de pacientes gerado!")
else:
    print("Conta bloqueada, entre em contato com o suporte para desbloqueio de conta.")