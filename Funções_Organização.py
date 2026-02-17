import mysql.connector

def linha():
    print(25 * "-=")

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
    opcao = int(input("Digite sua Opção: "))
    linha()
    return opcao

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="passageiros"
    )