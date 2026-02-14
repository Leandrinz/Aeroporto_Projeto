CREATE DATABASE Passageiros;

Use Passageiros; 

CREATE Table pessoas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    CPF VARCHAR(11) UNIQUE,
    nome VARCHAR(30) NOT NULL,
    Sexo ENUM('M', 'F'),
    nascimento DATE,
    estado_civil VARCHAR(30),
    profissao VARCHAR(30),
    nacionalidade VARCHAR(20) DEFAULT 'Brasil',
    Quantidade_Malas INT,
    Possui_Drogas BOOLEAN DEFAULT FALSE
) DEFAULT CHARSET  utf8;


INSERT into pessoas VALUES
(DEFAULT, '12345678901', 'Ana Silva', 'F', '1992-05-15', 'Solteiro(a)', 'Engenheira', 'Brasil', '2', FALSE),
(DEFAULT, '23456789012', 'Bruno Costa', 'M', '1985-11-30', 'Casado(a)', 'Professor', 'Brasil', '1', TRUE),
(DEFAULT, '34567890123', 'Carlos Souza', 'M', '1978-02-22', 'Divorciado(a)', 'Médico', 'Brasil', '3', FALSE),
(DEFAULT, '45678901234', 'Daniela Lima', 'F', '2000-08-10', 'Solteiro(a)', 'Designer', 'Brasil', '1', FALSE),
(DEFAULT, '56789012345', 'Eduardo Alves', 'M', '1995-03-12', 'Casado(a)', 'Advogado', 'Portugal', '2', FALSE),
(DEFAULT, '67890123456', 'Fernanda Rocha', 'F', '1988-07-25', 'Solteiro(a)', 'Arquiteta', 'Brasil', '0', TRUE),
(DEFAULT, '78901234567', 'Gabriel Nunes', 'M', '1990-12-05', 'Casado(a)', 'Programador', 'Brasil', '2', FALSE),
(DEFAULT, '89012345678', 'Helena Martins', 'F', '1982-01-18', 'Viúvo(a)', 'Cientista', 'Brasil', '4', FALSE),
(DEFAULT, '90123456789', 'Igor Pereira', 'M', '1997-06-30', 'Solteiro(a)', 'Chef', 'Brasil', '1', TRUE);

SELECT * from pessoas;