# ✈️ Sistema de Gerenciamento de Passageiros

Este projeto é um sistema interativo em Python integrado com MySQL para o gerenciamento e cadastro de passageiros. O foco principal do desenvolvimento foi a criação de um fluxo de dados seguro, utilizando estruturas de tratamento de exceções (`try-except`) e validações dinâmicas para garantir a integridade das informações no banco de dados.

## 🚀 Funcionalidades

* **Seleção Dinâmica de Tabelas**: O sistema lista as tabelas existentes e permite a seleção via ID, com limite validado automaticamente pelo número de registros encontrados.
* **Cadastro Blindado**:
    * **CPF**: Validação de formato (11 dígitos) e tipo (apenas números), preservando zeros à esquerda através de manipulação de strings.
    * **Sexo**: Normalização de entrada com `.upper()` e restrição aos valores 'M' ou 'F'.
    * **Dados Numéricos**: Uso de `try-except` para impedir que entradas não inteiras (letras ou símbolos) travem o programa em campos como "Quantidade de Malas" e "Possui Drogas".
* **Integração MySQL**: Criação automática de tabelas (se não existirem) e inserção de dados utilizando `mysql-connector`.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **MySQL**
* **Biblioteca `mysql-connector-python`**

## 📋 Como o Sistema Valida os Dados?

O projeto utiliza um padrão de "Loop de Validação Único" para cada entrada:
1.  O programa solicita o dado dentro de um `while True`.
2.  Se for um dado numérico, o `try` captura falhas de conversão (`ValueError`).
3.  Um `if` verifica se o valor está dentro do intervalo lógico (ex: entre 0 e 1 para booleanos ou limites da tabela).
4.  O loop só é interrompido (`break`) quando o dado é 100% confiável e validado.

---

## ✅ Etapas concluídas / ⏳ Pendentes

- [x] Conexão com Banco de Dados MySQL.
- [x] Listagem e seleção dinâmica de tabelas existentes.
- [x] Lógica de criação de novas tabelas via input do usuário.
- [x] Blindagem de inputs de CPF (formato string de 11 dígitos).
- [x] Blindagem de inputs de Sexo (normalização upper/match 'M' ou 'F').
- [x] Tratamento de exceções `try-except` para todos os campos inteiros (Malas/ID/Drogas).
- [x] Loop de repetição para permitir múltiplos cadastros em uma única execução.
- [x] **Implementação de testes unitários com Pytest (Próxima etapa).**
