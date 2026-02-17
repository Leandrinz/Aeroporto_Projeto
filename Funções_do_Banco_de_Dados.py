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

def menu_opcao_3():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("Select * from pessoas where Possui_Drogas = TRUE")
    resultado = cursor.fetchall()

    print(f"{'ID':<4} | {'CPF':<20} | {'NOME':<20} | {'Sexo':<5} | {'Nascimento'} | {'Estado Civil':<14} |{'Profissão':<12} | {'Nacionalidade':<12} | {'Malas':<4} | {'Possui_Drogas':<4}")

    for linha in resultado:
        print(f"{linha[0]:<4} | {linha[1]:<20} | {linha[2]:<20} | {linha[3]:<5} | {linha[4]} | {linha[5]:<14} | {linha[6]:<12} | {linha[7]:<12} | {linha[8]:<4} | {linha[9]:<4}")
    
    print("IRREGULARIDADE: TRÁFICO INTERNACIONAL DE DROGAS!!!")


def menu_opcao_4():
    conn = conectar()
    cursor = conn.cursor()
    # 1 - Pedir o nome da tabela
    nome_tabela = str(input("Informe o nome da lista: "))

    # 2 - Pedir quantas pessoas serão adicionadas nessa tabela
    quantidade_pessoas = int(input("Quantas pessoas serão adicionadas: "))

    
    # 3 - Pedir as informações de cada uma
    
    for contador in range(1, quantidade_pessoas + 1):
        cpf = int(input("Digite o CPF: "))
        
        nome = str(input("Digite o Nome: "))
        
        Sexo = str(input(f"Sexo de {nome}(M/F): "))
        
        Nascimento = str(input(f"Data de nascimento de {nome} (ex: 2000/05/20): "))
        
        Estado_civil = str(input(f"Estado civil de {nome}: "))
        
        Profissao = str(input(f"Profissão de {nome}: "))
        
        Nacionalidade = str(input(f"Nacionalidade de {nome}: "))
        
        Quantidade_de_malas = int(input(f"Quantidade de malas de {nome}: "))
        
        Possui_Drogas = int(input(f"{nome} possui drogas?\n 1 - Sim \n 2 - Não\nResposta: "))


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