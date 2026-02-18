import mysql.connector

def linha():
    print(25 * "-=")

def mensagem_de_erro_valor_nao_inteiro():
    print("Erro: Por favor, digite apenas números inteiros.")

def mensagem_de_erro_por_limite(inicio, final):
    print(f"Erro, valor deve estar entre {inicio} e {final}. ")

def menu(nome_tabela_escolhida):
    linha()
    print("PROJETO FRONTEIRA")
    print(f"Tabela Atual: {nome_tabela_escolhida}")
    print("1 - Selecionar Banco de Dados")
    print("2 - Ver Lista de Passageiros e informações")
    print("3 - Ver informações personalizadas dos passageiros")
    print("4 - Ver Passageiros Irregulares")
    print("5 - Adicionar lista/pessoas e informações dos passageiros")
    print("6 - Sair do Programa")
    print("")

    while True:
        try:
            opcao = int(input("Escolha sua opção: "))
            if 1 <= opcao <= 6:
                break
            else:
                mensagem_de_erro_por_limite(1,6)
        except ValueError:
            mensagem_de_erro_valor_nao_inteiro()

    linha()

    return opcao

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="passageiros"
    )