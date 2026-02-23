import funcoes_banco_dados as banco 
from unittest.mock import patch, MagicMock
import pytest
import builtins
from funcoes_banco_dados import *

@pytest.fixture
def usuario_com_droga():
    pessoa_ilegal = (1, "12345678911", "Leandro", "M", "2006/07/24", "Solteiro", "Estudante", "Brasil", 3, 1)
    return pessoa_ilegal

@pytest.fixture
def usuario_sem_droga():
    pessoa_legal = (2, "98765432112", "João bom", "M", "1990/10/23", "C","Pastor", "Brasil", 2, 0)

# 1) Testes menu_opção_1:

def test_menu_opcao_1_sucesso(): 
    
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = [("clientes",), ("Produtos",)]

    
    with patch("builtins.input", return_value="1"):
        resultado = banco.menu_opcao_1(mock_conn) 

    assert resultado == "clientes"

def test_menu_opcao_1_erro_e_depois_acerto():
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = [("clientes",)]

    with patch("builtins.input", side_effect=["99", "1"]):
        resultado = menu_opcao_1(mock_conn)
        
    assert resultado == "clientes"

def test_tabela_vazia_menu_1():

    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = []

    resultado = banco.menu_opcao_1(mock_conn)
    assert resultado == None


# 2) Testes menu_opção_3:
def test_menu_opcao_3_sucesso():
    
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.side_effect = [
        [(1, "João"), (2, "Maria")],
        [(1, "12345678911", "João", "M", "1990", "C", "Dev", "BR", 1, 0)]
    ]

    with patch("builtins.input", return_value="1"), \
         patch("builtins.print"):
        
        banco.menu_opcao_3("passageiros", mock_conn)
    
    chamadas_sql = [call[0][0] for call in mock_cursor.execute.call_args_list]

    assert "SELECT id, nome FROM passageiros" in chamadas_sql[0]
    assert "where id = 1" in chamadas_sql[1]

def test_menu_opcao_3_erro_e_depois_acerto():
    
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.side_effect = [
        [(1, "João"), (2, "Maria")],
        [(2, "12345678911", "Maria", "F", "90", "C", "Dev", "Brasil", 2, 0)]
    ]

    with patch("builtins.input", side_effect = ["99", "2"]):
        banco.menu_opcao_3("tabela", mock_conn)
    
    assert mock_cursor.execute.call_count == 2

def test_tabela_vazia_menu_3():
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = []

    resultado = banco.menu_opcao_3("tabela", mock_conn)

    assert resultado == None


# 3) Testes menu_opção 4

def test_sucesso_menu_opcao_4(usuario_com_droga):
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = [usuario_com_droga]

    with patch("builtins.print"):
        banco.menu_opcao_4("passageiros", mock_conn)
    
    chamada_sql = mock_cursor.execute.call_args[0][0]

    assert "from passageiros" in chamada_sql.lower()

    assert "possui_drogas = true" in chamada_sql.lower()

    assert mock_cursor.fetchall.called


def test_menu_opcao_4_tabela_vazia():
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = []

    resultado = banco.menu_opcao_4("Passageiros", mock_conn)

    assert resultado == None


# 4) Testes menu_opção_5

def test_menu_opcao_5_sucesso(mocker):
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = [('viagens',)]

    mocker.patch('builtins.input', side_effect=['1', '1', '12345678901', 'Ana', 'F', '1995/10/10', 'Solteira', 'Designer', 'Brasil', '1', '0'])

    mocker.patch('builtins.print')

    menu_opcao_5(mock_conn)

    assert mock_conn.commit.called

    args, _ = mock_cursor.execute.call_args
    assert "Insert into" in args[0]


def test_menu_opcao_5_erro_banco(mocker):
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = [('viagens',)]

    mock_cursor.execute.side_effect = [None, None, Exception("Erro de Integridade: CPF duplicado")]

    mocker.patch('builtins.input', side_effect=[
        '1', '1', '12345678901', 'Ana', 'F', '1995/10/10', 'Solteira', 'Designer', 'Brasil', '1', '0'
    ])

    with pytest.raises(Exception):
        menu_opcao_5(mock_conn)

def test_menu_opcao_5_tabela_vazia():
    mock_conn = MagicMock()
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = []

    resultado = banco.menu_opcao_5(mock_conn)

    assert resultado == None