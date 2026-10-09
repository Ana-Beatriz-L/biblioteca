"""Model do Autor (PESSOA 1). Só acessa o banco, nada de print/input aqui."""
from database import get_connection


class Autor:
    def __init__(self, nome, nacionalidade, id=None):
        self.id = id
        self.nome = nome
        self.nacionalidade = nacionalidade

    def salvar(self):
        """INSERT do autor; preenche self.id com o id gerado."""
        # TODO
        raise NotImplementedError

    @classmethod
    def listar_todos(cls):
        """Retorna uma lista de objetos Autor."""
        # TODO
        raise NotImplementedError

    @classmethod
    def buscar_por_id(cls, id):
        """Retorna um Autor ou None se não existir."""
        # TODO
        raise NotImplementedError

    def atualizar(self):
        """UPDATE do autor com base em self.id."""
        # TODO
        raise NotImplementedError

    @classmethod
    def excluir(cls, id):
        # TODO
        raise NotImplementedError
