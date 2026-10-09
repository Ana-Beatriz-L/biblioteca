class LivroView:
    def exibir_menu(self):
        print("\nGerenciar Livro")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Atualizar livro")
        print("4. Excluir livro")
        print("5. Voltar ao menu principal")
        return input("Escolha uma opção: ").strip()

    def mostrar_mensagem(self, texto):
        print(texto)

    def ler_dados_livro(self):
        """Devolve tudo como texto; o controller é quem valida."""
        titulo = input("Título: ").strip()
        ano = input("Ano de publicação: ").strip()
        autor_id = input("ID do autor: ").strip()
        return titulo, ano, autor_id

    def ler_id(self, acao):
        """Pede o ID do livro. Devolve int ou None se digitou algo inválido."""
        try:
            return int(input(f"Informe o ID do livro a {acao}: "))
        except ValueError:
            print("ID inválido! Deve ser um número inteiro.")
            return None

    def mostrar_livros(self, lista):
        print("\n=== Lista de Livros ===")
        if not lista:
            print("Nenhum livro encontrado.")
        else:
            for livro in lista:
                print(
                    f"ID do Livro: {livro[0]} | Título: {livro[1]} | "
                    f"Ano: {livro[2]} | Autor: {livro[3]} | ID do Autor: {livro[4]}"
                )