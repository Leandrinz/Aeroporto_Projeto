from Funções_Organização import *

def menu_opcao_2():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM pessoas")
    resultado = cursor.fetchall()

    print(f"{'ID':<4} | {'Nome':<12}")

    for linha in resultado:
        print(f"{linha[0]:<4} | {linha[1]:<12}")

    passageiro_escolhido = int(input("Digite o id do Passageiro Escolhido: "))

    cursor.execute(f"Select * from pessoas where id = {passageiro_escolhido}")
    resultado = cursor.fetchall()

    print(f"{'ID':<4} | {'CPF':<20} | {'NOME':<20} | {'Sexo':<5} | {'Nascimento'} | {'Estado Civil':<14} |{'Profissão':<12} | {'Nacionalidade':<12} | {'Malas':<4} | {'Possui_Drogas':<4}")

    for linha in resultado:
        for linha in resultado:
            print(f"{linha[0]:<4} | {linha[1]:<20} | {linha[2]:<20} | {linha[3]:<5} | {linha[4]} | {linha[5]:<14} | {linha[6]:<12} | {linha[7]:<12} | {linha[8]:<4} | {linha[9]:<4}")