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

    def _validar_dados(self, nome, nacionalidade):
        if not nome:
            self.view.mostrar_mensagem("O nome é obrigatório!")
            return False
        if not nacionalidade:
            self.view.mostrar_mensagem("A nacionalidade é obrigatória!")
            return False
        return True

    def cadastrar(self):
        try:
            nome, nacionalidade = self.view.ler_dados_autor()
            if not self._validar_dados(nome, nacionalidade):
                return
                Autor(nome, nacionalidade).salvar()
                self.view.mostrar_mensagem("Autor cadastrado com sucesso!")
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro ao cadastrar autor: {e}")

    def listar(self):
        try:
            autores = Autor.listar_todos()
            self.view.mostrar_autores(autores)
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro ao listar autores: {e}")

    def atualizar(self):
        try:
            id_autor = self.view.ler_id("atualizar")
            if id_autor is None:
                return
            autor = Autor.buscar_por_id(id_autor)
            if autor is None:
                self.view.mostrar_mensagem("Autor não encontrado!")
                return
            nome, nacionalidade = self.view.ler_dados_autor()
            if not self._validar_dados(nome, nacionalidade):
                return
            autor.nome = nome
            autor.nacionalidade = nacionalidade
            if autor.atualizar():
                self.view.mostrar_mensagem("Autor atualizado com sucesso!")
            else:
                self.view.mostrar_mensagem("Não foi possível atualizar o autor.")
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro ao atualizar autor: {e}")

    def excluir(self):
        try:
            id_autor = self.view.ler_id("excluir")
            if id_autor is None:
                return
            if Autor.buscar_por_id(id_autor) is None:
                self.view.mostrar_mensagem("Autor não encontrado!")
                return
            try:
                excluido = Autor.excluir(id_autor)
            except Exception:
                self.view.mostrar_mensagem(
                    "Não foi possível excluir! O autor possui livros cadastrados. "
                    "Exclua ou altere esses livros primeiro."
                )
                return
            if excluido:
                self.view.mostrar_mensagem("Autor excluído com sucesso!")
            else:
                self.view.mostrar_mensagem("Não foi possível excluir o autor.")
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro ao excluir autor: {e}")