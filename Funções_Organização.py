import mysql.connector

def linha():
    print(25 * "-=")

def menu():
    linha()
    print("PROJETO FRONTEIRA")
    print("1 - Ver Lista de Passageiros e informações")
    print("2 - Ver informações personalizadas dos passageiros")
    print("3 - Análise da Lista de Passageiros")
    print("4 - Adicionar lista e informações dos passageiros")
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