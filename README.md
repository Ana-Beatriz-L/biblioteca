# Sistema de Biblioteca

Aplicação de linha de comando em Python para gerenciar autores e livros de uma
biblioteca universitária. O projeto usa a arquitetura **MVC
(Model-View-Controller)**, orientação a objetos e PostgreSQL.

## Funcionalidades

- **Autores:** cadastrar, listar, atualizar e excluir.
- **Livros:** cadastrar, listar com o nome do autor, atualizar e excluir.
- Menus em loop com opção para voltar ao menu principal.
- Validação de ano, autor existente e campos obrigatórios.

## Tecnologias

- Python 3.10 ou superior.
- PostgreSQL 13 ou superior.
- `psycopg2-binary`, para conexão com o banco.
- `python-dotenv`, para carregar as configurações do arquivo `.env`.

## Como executar

### 1. Pré-requisitos

Instale:

- [Python](https://www.python.org/downloads/) 3.10 ou superior.
- [PostgreSQL](https://www.postgresql.org/download/) 13 ou superior.
- Git, caso o projeto ainda não esteja disponível no computador.

### 2. Obter o projeto

```bash
git clone https://github.com/Ana-Beatriz-L/biblioteca.git
cd biblioteca
```

Se o projeto já estiver na sua máquina, apenas entre na pasta dele:

```bash
cd caminho/para/biblioteca
```

### 3. Criar e ativar o ambiente virtual

No Linux ou macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

No Windows PowerShell:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
python -m pip install -r requirements.txt
```

### 5. Criar o banco de dados

Crie um banco chamado `biblioteca` no PostgreSQL. Pelo terminal, usando um
usuário que tenha permissão para criar bancos:

```bash
createdb -U postgres biblioteca
```

Depois, aplique o esquema das tabelas:

```bash
psql -U postgres -d biblioteca -f schema.sql
```

Também é possível executar o conteúdo de `schema.sql` pelo pgAdmin.

### 6. Configurar a conexão

Crie o arquivo `.env` a partir do exemplo:

```bash
cp .env.example .env
```

No Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Abra o arquivo `.env` e informe os dados corretos do seu PostgreSQL:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=biblioteca
DB_USER=postgres
DB_PASSWORD=sua_senha_do_postgres
```

Não publique o arquivo `.env`, pois ele contém credenciais. Ele já está
protegido pelo `.gitignore`.

### 7. Iniciar o programa

Com o ambiente virtual ativado e a partir da pasta do projeto:

```bash
python main.py
```

No menu principal:

1. Escolha **Autores** para cadastrar ou consultar autores.
2. Escolha **Livros** para cadastrar ou consultar livros.
3. Escolha **Sair** para encerrar o programa.

## Integrantes

| Nome |
|------|
| Ana Beatriz Lima Araujo |
| Nathalia Gonçalves Silva |
