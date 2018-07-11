#Calculadora de investimentos
import os

def menu():
    print("Bem-vindo à calculadora de investimentos")

    print("\n1 - Investimento com juros simples")
    print("2 - Investimento com juros compostos")
    print("9 - Sair do sistema")

    opcao = input("\nDigite a opção desejada (1/2/9): ")

    if opcao == '1':
        js()
    elif opcao == '2':
        jc()
    elif opcao == '9':
        sair()
    else:
        print("\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
        padrao()

def js():
    valorInvestido = input("Digite o valor a ser investido: ")
    tempo = input("Digite o tempo do investimento: ")
    juro = input("Digite o juro da aplicação (em %): ")
    renda = float(valorInvestido) *(float(juro)/100) * int(tempo)
    retorno = renda + (float(valorInvestido))

    print("\nO retorno PREVISTO para seu investimento, conforme os dados inseridos no sistema é de R$ %f" %retorno)
    padrao()

def jc():
    valorInvestido = input("Digite o valor a ser investido: ")
    tempo = input("Digite o tempo do investimento: ")
    juro = input("Digite o juro da aplicação (em %): ")
    i = 0

    while (i < int(tempo)):
        i+=1
        renda = float(valorInvestido) * (float(juro) / 100) * int(tempo)
        valorInvestido = renda + (float(valorInvestido))

    print("\nO retorno PREVISTO para seu investimento, conforme os dados inseridos no sistema é de R$ %f" %valorInvestido)
    padrao()

def sair():
    print("\nObrigado por utilizar nossa calculadora. Até logo!")
    exit()

def padrao():
    os.system("PAUSE")
    os.system("CLS")
    menu()

print("\n\nAVISO: ESTA CALCULADORA NÃO É, DE NENHUMA FORMA OU MANEIRA, GARANTIA DE QUE OS DADOS AQUI COLOCADOS")
print("SERÃO OS RETORNOS DO INVESTIMENTO. ELE APENAS REALIZA OS CÁLCULOS COM BASE NOS DADOS COLOCADOS NO SISTEMA E NÃO")
print("DEVEM SER USADOS COMO A ÚNICA FONTE SOBRE O RETORNO DO INVESTIMENTO. O AUTOR DO SOFTWARE NÃO SE RESPONSABILIZA")
print("PELOS DADOS INSERIDOS NO SISTEMA E SE ISENTA DE QUALQUER INCONFORMIDADE QUE POSSA OCORRER NA SAÍDA DAS INFORMAÇÕES.\n\n")

padrao()

menu()