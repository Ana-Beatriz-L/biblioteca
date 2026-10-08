"""View do Livro (PESSOA 2). Só print/input, nada de banco aqui."""


class LivroView:
    def exibir_menu(self):
        print("\nGerenciar Livro")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Atualizar livro")
        print("4. Excluir livro")
        print("5. Voltar ao menu principal")
        return input("Escolha uma opção: ").strip()

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def ler_dados_livro(self):
        """Pede título, ano e id do autor. Retorna (titulo, ano, autor_id)."""
        # TODO
        raise NotImplementedError

    def ler_id(self, acao):
        """Pede o id do livro para a ação (atualizar/excluir). Retorna int."""
        # TODO
        raise NotImplementedError

    def mostrar_livros(self, livros):
        """Imprime a lista de livros (id, título, ano, nome do autor)."""
        # TODO
        raise NotImplementedError
