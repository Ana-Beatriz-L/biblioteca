"""Model do Livro (PESSOA 2). Só acessa o banco, nada de print/input aqui."""
from database import get_connection


class Livro:
    def __init__(self, titulo, ano_publicacao, autor_id, id=None):
        self.id = id
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.autor_id = autor_id

    def salvar(self):
        """INSERT do livro; preenche self.id com o id gerado."""
        # TODO
        raise NotImplementedError

    @classmethod
    def listar_com_autor(cls):
        """JOIN com autor. Retorna tuplas (id, titulo, ano_publicacao, nome_autor)."""
        # TODO
        raise NotImplementedError

    @classmethod
    def buscar_por_id(cls, id):
        """Retorna um Livro ou None se não existir."""
        # TODO
        raise NotImplementedError

    def atualizar(self):
        """UPDATE do livro com base em self.id."""
        # TODO
        raise NotImplementedError

    @classmethod
    def excluir(cls, id):
        """DELETE do livro."""
        # TODO
        raise NotImplementedError
