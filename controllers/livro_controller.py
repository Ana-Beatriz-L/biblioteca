"""Controller do Livro (PESSOA 2). Liga a view ao model."""
from models.autor import Autor
from models.livro import Livro
from views.livro_view import LivroView


class LivroController:
    def __init__(self):
        self.view = LivroView()

    def menu(self):
        """Submenu em loop até o usuário escolher 'Voltar'."""
        while True:
            opcao = self.view.exibir_menu()
            if opcao == "1":
                self.cadastrar()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.atualizar()
            elif opcao == "4":
                self.excluir()
            elif opcao == "5":
                break
            else:
                self.view.mostrar_mensagem("Opção inválida.")

    def cadastrar(self):
        # TODO: ler dados, validar ano e se o autor existe (Autor.buscar_por_id)
        raise NotImplementedError

    def listar(self):
        # TODO: Livro.listar_com_autor() -> view.mostrar_livros()
        raise NotImplementedError

    def atualizar(self):
        # TODO: ler id, verificar se existe, ler novos dados, validar, atualizar
        raise NotImplementedError

    def excluir(self):
        # TODO: ler id, excluir
        raise NotImplementedError
