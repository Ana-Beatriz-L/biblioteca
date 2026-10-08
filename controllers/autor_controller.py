"""Controller do Autor (PESSOA 1). Liga a view ao model."""
from models.autor import Autor
from views.autor_view import AutorView


class AutorController:
    def __init__(self):
        self.view = AutorView()

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
        # TODO: view.ler_dados_autor() -> Autor(...).salvar() -> mensagem
        raise NotImplementedError

    def listar(self):
        # TODO: Autor.listar_todos() -> view.mostrar_autores()
        raise NotImplementedError

    def atualizar(self):
        # TODO: ler id, verificar se existe, ler novos dados, atualizar
        raise NotImplementedError

    def excluir(self):
        # TODO: ler id, excluir; tratar erro se o autor tiver livros
        raise NotImplementedError
