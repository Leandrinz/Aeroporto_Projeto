from Funções_Organização import *
from funcoes_banco_dados import *
nome_tabela_escolhida = menu_opcao_1()
while True:
    opcao = menu(nome_tabela_escolhida)
    match opcao:
        case 1:
            nome_tabela_escolhida = menu_opcao_1()
        case 2:
            try:
                conn = conectar()
                cursor = conn.cursor()

                cursor.execute(f"SELECT * FROM {nome_tabela_escolhida}")
                resultado = cursor.fetchall()

                print(f"{'ID':<4} | {'CPF':<20} | {'NOME':<20} | {'Sexo':<5} | {'Nascimento'} | {'Estado Civil':<14} |{'Profissão':<12} | {'Nacionalidade':<12} | {'Malas':<4} | {'Possui_Drogas':<4}")

                for linha in resultado:
                    print(f"{linha[0]:<4} | {linha[1]:<20} | {linha[2]:<20} | {linha[3]:<5} | {linha[4]} | {linha[5]:<14} | {linha[6]:<12} | {linha[7]:<12} | {linha[8]:<4} | {linha[9]:<4}")

            except mysql.connector.Error as err:
                print(f"Erro ao conectar ao banco: {err}")
            finally:
                if 'conn' in locals() and conn.is_connected:
                    cursor.close()
                    conn.close()
            
        case 3: 
            menu_opcao_3(nome_tabela_escolhida)
        case 4:
            menu_opcao_4(nome_tabela_escolhida)
        case 5:
            menu_opcao_5()
        case 6:
            break

print("Programa Finalzado...")