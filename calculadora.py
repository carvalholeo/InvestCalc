#Calculadora de investimentos
import os

def menu():
    print("Bem-vindo à calculadora")

    print("\n1 - Cálculo com juros simples")
    print("2 - Cálculo com juros compostos")
    print("3 - Cálculo de retorno sobre investimento (ROI)")
    print("9 - Sair do sistema")

    opcao = input("\nDigite a opção desejada (1/2/3/9): ")

    if opcao == '1':
        js()
    elif opcao == '2':
        jc()
    elif opcao == '3':
        roi()
    elif opcao == '9':
        sair()
    else:
        print("\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
        padrao()

def js():
    valorPresente = input("Digite o valor a ser investido: ")
    periodo = input("Digite o tempo do investimento: ")
    juros = input("Digite o juro da aplicação (em %): ")
    valorFuturo = float(valorPresente) * (1 + ((float(juros)/100) * int(periodo)))
    retorno(valorFuturo)

def jc():
    valorPresente = input("Digite o valor a ser investido: ")
    periodo = input("Digite o tempo do investimento: ")
    juros = input("Digite o juro da aplicação (em %): ")
    valorFuturo = float(valorPresente) * (1 + ((float(juros)/100)))**int(periodo)
    retorno(valorFuturo)

def roi():
    investimento = input("Digite o valor investido: ")
    retReal = input("Digite o retorno obtido no investimento: ")
    roi = ((float(retReal) - float(investimento)) / float(investimento)) * 100
    retorno(roi,'roi')

def sair():
    print("\nObrigado por utilizar a calculadora. Até logo!")
    exit()

def padrao(counter = 0):
    if (counter == 0):
        print("\n\nAVISO: ESTA CALCULADORA NÃO É, DE NENHUMA FORMA OU MANEIRA, GARANTIA DE QUE OS DADOS AQUI COLOCADOS SERÃO OS RETORNOS DO INVESTIMENTO OU OUTRAS INFORMAÇÕES. ELE APENAS REALIZA OS CÁLCULOS COM BASE NOS DADOS COLOCADOS NO SISTEMA E NÃO DEVEM SER USADOS COMO A ÚNICA FONTE SOBRE O RETORNO DO INVESTIMENTO. O AUTOR DO SOFTWARE NÃO SE RESPONSABILIZA PELOS DADOS INSERIDOS NO SISTEMA E SE ISENTA DE QUALQUER INCONFORMIDADE QUE POSSA OCORRER NA SAÍDA DAS INFORMAÇÕES.\n\n")
        counter += 1

    os.system("PAUSE")
    os.system("CLS")
    menu()

def retorno(retorno,tipo = 'padrao'):
    if (tipo == 'padrao'):
        print('\nO resultado do cálculo solicitado, conforme os dados inseridos no sistema, é de R$ {:.2f}'.format(retorno))
    elif (tipo == 'roi'):
        print('\nO resultado do cálculo solicitado, conforme os dados inseridos no sistema, é de ' + str(retorno)  + '%')
    print("\n\n")
    padrao(1)
    return

padrao()
