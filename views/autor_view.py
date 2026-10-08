"""View do Autor (PESSOA 1). Só print/input, nada de banco aqui."""


class AutorView:
    def exibir_menu(self):
        print("\nGerenciar Autor")
        print("1. Cadastrar autor")
        print("2. Listar autores")
        print("3. Atualizar autor")
        print("4. Excluir autor")
        print("5. Voltar ao menu principal")
        return input("Escolha uma opção: ").strip()

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

    def ler_dados_autor(self):
        """Pede nome e nacionalidade. Retorna (nome, nacionalidade)."""
        # TODO
        raise NotImplementedError

    def ler_id(self, acao):
        """Pede o id do autor para a ação (atualizar/excluir). Retorna int."""
        # TODO
        raise NotImplementedError

    def mostrar_autores(self, autores):
        """Imprime a lista de autores."""
        # TODO
        raise NotImplementedError
