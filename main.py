from Funções_Organização import *
from Funções_do_Banco_de_Dados import *

while True:
    opcao = menu()
    match opcao:
        case 1:
            try:
                conn = conectar()
                cursor = conn.cursor()

                cursor.execute("SELECT * FROM pessoas")
                resultado = cursor.fetchall()

                print(f"{'ID':<4} | {'CPF':<20} | {'NOME':<20} | {'Sexo':<5} | {'Nascimento'} | {'Estado Civil':<14} |{'Profissão':<12} | {'Nacionalidade':<12} | {'Malas':<4} | {'Possui_Drogas':<4}")

                for linha in resultado:
                    print(f"{linha[0]:<4} | {linha[1]:<20} | {linha[2]:<20} | {linha[3]:<5} | {linha[4]} | {linha[5]:<14} | {linha[6]:<12} | {linha[7]:<12} | {linha[8]:<4} | {linha[9]:<4}")

            except mysql.connector.Error as err:
                print(f"Erro ao conectar ao banco: {err}")
            finally:
                if 'coon' in locals() and conn.is_connected:
                    cursor.close()
                    conn.close()
            
        case 2: 
            menu_opcao_2()
        case 3:
            menu_opcao_3()
        case 4:
            # Adicionar lista e informações dos passageiros (Adicionar novo banco de dados)
            pass