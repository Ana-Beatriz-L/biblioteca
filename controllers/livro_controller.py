from datetime import date

from models.livro import LivroModel
from views.livro_view import LivroView


class LivroController:
    def __init__(self):
        self.model = LivroModel()
        self.view = LivroView()

    def menu(self):
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
                self.view.mostrar_mensagem("Opção inválida. Tente novamente.")

    def _validar_dados(self, titulo, ano, autor_id):
        if not titulo:
            self.view.mostrar_mensagem("O título é obrigatório!")
            return None

        ano_atual = date.today().year
        try:
            ano_int = int(ano)
        except ValueError:
            ano_int = 0
        if not 1 <= ano_int <= ano_atual:
            self.view.mostrar_mensagem(
                f"Ano inválido! Digite um número inteiro entre 1 e {ano_atual}."
            )
            return None

        try:
            autor_int = int(autor_id)
        except ValueError:
            autor_int = None
        if autor_int is None or not self.model.autor_existe(autor_int):
            self.view.mostrar_mensagem(
                "Autor não encontrado! Confira o ID ou cadastre o autor primeiro."
            )
            return None

        return ano_int, autor_int

    def cadastrar(self):
        try:
            titulo, ano, autor_id = self.view.ler_dados_livro()
            dados = self._validar_dados(titulo, ano, autor_id)
            if dados is None:
                return
            ano_int, autor_int = dados
            if self.model.inserir_livro(titulo, ano_int, autor_int):
                self.view.mostrar_mensagem("Livro cadastrado com sucesso!")
            else:
                self.view.mostrar_mensagem("Não foi possível cadastrar o livro.")
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro ao cadastrar livro: {e}")

    def listar(self):
        try:
            livros = self.model.listar_livros()
            self.view.mostrar_livros(livros)
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro ao listar livros: {e}")

    def atualizar(self):
        try:
            id_livro = self.view.ler_id("atualizar")
            if id_livro is None:
                return
            if not self.model.livro_existe(id_livro):
                self.view.mostrar_mensagem("Livro não encontrado!")
                return
            titulo, ano, autor_id = self.view.ler_dados_livro()
            dados = self._validar_dados(titulo, ano, autor_id)
            if dados is None:
                return
            ano_int, autor_int = dados
            if self.model.atualizar_livro(id_livro, titulo, ano_int, autor_int):
                self.view.mostrar_mensagem("Livro atualizado com sucesso!")
            else:
                self.view.mostrar_mensagem("Não foi possível atualizar o livro.")
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro ao atualizar livro: {e}")

    def excluir(self):
        try:
            id_livro = self.view.ler_id("excluir")
            if id_livro is None:
                return
            if not self.model.livro_existe(id_livro):
                self.view.mostrar_mensagem("Livro não encontrado!")
                return
            if self.model.excluir_livro(id_livro):
                self.view.mostrar_mensagem("Livro excluído com sucesso!")
            else:
                self.view.mostrar_mensagem("Não foi possível excluir o livro.")
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro ao excluir livro: {e}")