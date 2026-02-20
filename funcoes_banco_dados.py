from Funções_Organização import *

def menu_opcao_1(conn = None):
    if conn is None:
        conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES")

    tabelas = cursor.fetchall()

    print("--- TABELAS EXISTENTES ---")
    if not tabelas:
        print("Nenhuma tabela encontrada!")
        return None
    else:
        print(f"{'ID':<4} | {'TABELA':<12}")
        for i, tabela in enumerate(tabelas, start=1):
            print(f"{i:<4} | {tabela[0]:<12}")
        while True:
            try:
                tabela_desejada = int(input("\nDigite o ID da tabela desejada: "))

                if 1 <= tabela_desejada <= i:
                    break
                else:
                    print(f"Erro, escolha um número entre 1 e {i}.")
            except ValueError:
                mensagem_de_erro_valor_nao_inteiro()

        for i, tabela in enumerate(tabelas, start=1):
            if (i == tabela_desejada):
                nome_tabela_desejada = tabela[0]
                print(f"Tabela Escolhida -> {nome_tabela_desejada}")
                break
    return nome_tabela_desejada
        

def menu_opcao_3(nome_tabela_escolhida, conn = None):
    if conn is None:
        conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, nome FROM {nome_tabela_escolhida}")
    resultado = cursor.fetchall()
    total_linhas = len(resultado)
    
    if total_linhas == 0:
        print(f"Nenhum registro encontrado. Assegure-se de fazer registros na {nome_tabela_escolhida} antes de buscar informações nela.")
        return None

    print(f"{'ID':<4} | {'Nome':<12}")

    for linha in resultado:
        print(f"{linha[0]:<4} | {linha[1]:<12}")

    while True:
        try:
            passageiro_escolhido = int(input("Digite o id do Passageiro Escolhido: "))

            if 1 <= passageiro_escolhido <= total_linhas:
                break
            else:
                mensagem_de_erro_por_limite(1, total_linhas)
        except ValueError:
            mensagem_de_erro_valor_nao_inteiro()

    cursor.execute(f"Select * from {nome_tabela_escolhida} where id = {passageiro_escolhido}")
    resultado = cursor.fetchall()

    print(f"{'ID':<4} | {'CPF':<20} | {'NOME':<20} | {'Sexo':<5} | {'Nascimento'} | {'Estado Civil':<14} | {'Profissão':<12} | {'Nacionalidade':<12} | {'Malas':<4} | {'Possui_Drogas':<4}")

    for linha in resultado:
        for linha in resultado:
            print(f"{linha[0]:<4} | {linha[1]:<20} | {linha[2]:<20} | {linha[3]:<5} | {linha[4]} | {linha[5]:<14} | {linha[6]:<12} | {linha[7]:<12}  | {linha[8]:<4}  | {linha[9]:<4}")

def menu_opcao_4(nome_tabela_escolhida, conn = None):
    if conn is None:
        conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"Select * from {nome_tabela_escolhida} where Possui_Drogas = TRUE")
    resultado = cursor.fetchall()

    print(f"{'ID':<4} | {'CPF':<20} | {'NOME':<20} | {'Sexo':<5} | {'Nascimento'} | {'Estado Civil':<14} |{'Profissão':<12} | {'Nacionalidade':<12} | {'Malas':<4} | {'Possui_Drogas':<4}")

    for linha in resultado:
        print(f"{linha[0]:<4} | {linha[1]:<20} | {linha[2]:<20} | {linha[3]:<5} | {linha[4]} | {linha[5]:<14} | {linha[6]:<12} | {linha[7]:<12} | {linha[8]:<4} | {linha[9]:<4}")
    
    print("IRREGULARIDADE: TRÁFICO INTERNACIONAL DE DROGAS!!!")


def menu_opcao_5():
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute("SHOW TABLES")

    tabelas = cursor.fetchall()
    total_linhas = len(tabelas)
    print("--- TABELAS EXISTENTES ---")
    if not tabelas:
        print("Nenhuma tabela encontrada!")
    else:
        print(f"{'ID':<4} | {'TABELA':<12}")
        print(f"{'0':<4} | {'Criar nova tabela':<12}")
        for i, tabela in enumerate(tabelas, start=1):
            print(f"{i:<4} | {tabela[0]:<12}")
        
        while True:
            try:
                tabela_desejada = int(input("\nDigite o ID da tabela desejada ou 0 Para criar uma nova tabela: "))
                if 0 <= tabela_desejada <= total_linhas:
                    break
                else:
                    mensagem_de_erro_por_limite(0, total_linhas)
            except ValueError:
                mensagem_de_erro_valor_nao_inteiro()

        for i, tabela in enumerate(tabelas, start=1):
            if (tabela_desejada == 0):
                break
            if (i == tabela_desejada):
                nome_tabela_desejada = tabela[0]
                print(f"Tabela Escolhida -> {nome_tabela_desejada}")
                break

    if (tabela_desejada == 0):

        nome_tabela = str(input("Informe o nome da lista: "))
    else:
        nome_tabela = nome_tabela_desejada
    while True:
        try:
            quantidade_pessoas = int(input("Quantas pessoas serão adicionadas: "))
            if quantidade_pessoas >= 1:
                break
            else:
                print("Erro: Digite um valor válido.")
        except ValueError:
            mensagem_de_erro_valor_nao_inteiro()

    
    for contador in range(1, quantidade_pessoas + 1):
        while True:
            cpf = input("Digite o CPF (Apenas números): ")
            if len(cpf) == 11 and cpf.isdigit():
                break
            else:
                print("Erro: O CPF deve conter exatamente 11 números!")
                
        nome = str(input("Digite o Nome: "))
        
        while True:
            Sexo = str(input(f"Sexo de {nome}(M/F): ")).upper()
            if Sexo in ['M', 'F']:
                break
            else:
                print("Erro: Digite apenas 'M' ou 'F'!!!")
        
        Nascimento = str(input(f"Data de nascimento de {nome} (ex: 2000/05/20): "))
        
        Estado_civil = str(input(f"Estado civil de {nome}: "))
        
        Profissao = str(input(f"Profissão de {nome}: "))
        
        Nacionalidade = str(input(f"Nacionalidade de {nome}: "))
        
        while True:
            try:
                Quantidade_de_malas = int(input(f"Quantidade de malas de {nome}: "))
                if Quantidade_de_malas >= 1:
                    break
                else:
                    print("Erro: Digite um valor válido.")
            except ValueError:
                mensagem_de_erro_valor_nao_inteiro()
        
        while True:
            try:
                Possui_Drogas = int(input(f"{nome} possui drogas?\n 1 - Sim \n 0 - Não\nResposta: "))
                if Possui_Drogas in [0, 1]:
                    break
                else:
                    print("Erro: O valor deve ser 1 ou 0")
            except ValueError:
                mensagem_de_erro_valor_nao_inteiro()


        cursor.execute(f"""Create TABLE if not exists  {nome_tabela} 
        (id INT AUTO_INCREMENT PRIMARY KEY,
        CPF VARCHAR(11) UNIQUE,
        nome VARCHAR(30) NOT NULL,
        Sexo ENUM('M', 'F'),
        nascimento DATE,
        estado_civil VARCHAR(30),
        profissao VARCHAR(30),
        nacionalidade VARCHAR(20) DEFAULT 'Brasil',
        Quantidade_Malas INT,
        Possui_Drogas BOOLEAN DEFAULT FALSE
        ) DEFAULT CHARSET  utf8;""")

        cursor.execute(f"""Insert into {nome_tabela} values
        (default, '{cpf}', '{nome}', '{Sexo}', '{Nascimento}', '{Estado_civil}', '{Profissao}', '{Nacionalidade}', {Quantidade_de_malas}, {Possui_Drogas} )""")

        conn.commit()

    cursor.close()
    conn.close()