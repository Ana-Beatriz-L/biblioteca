# Sistema de Biblioteca 
 
Aplicação de linha de comando em Python para gerenciar autores e livros de uma biblioteca universitária. O projeto usa a arquitetura **MVC (Model-View-Controller)**, **orientação a objetos** e banco de dados **PostgreSQL**.
 
## Integrantes
 
| Nome |
|------|
| Ana Beatriz Lima Araujo | 
| Nathalia Gonçalves Silva | 
 
## Funcionalidades
 
- **Autores:** cadastrar, listar, atualizar e excluir
- **Livros:** cadastrar, listar (com o nome do autor), atualizar e excluir
- Menus em loop: os submenus só fecham quando o usuário escolhe "Voltar ao menu principal"
- Validação de dados (ano numérico, autor existente, campos obrigatórios)
## Tecnologias
 
- Python 3.10 ou superior
- PostgreSQL 13 ou superior
- Bibliotecas: `psycopg2-binary` (conexão com o banco) e `python-dotenv` (leitura do arquivo `.env`)
