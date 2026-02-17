import mysql.connector

def linha():
    print(25 * "-=")

def menu():
    linha()
    print("PROJETO FRONTEIRA")
    print("1 - Ver Lista de Passageiros e informações")
    print("2 - Ver informações personalizadas dos passageiros")
    print("3 - Ver Passageiros Irregulares")
    print("4 - Adicionar lista e informações dos passageiros")
    print("5 - Sair do Programa")
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