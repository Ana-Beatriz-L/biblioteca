from database import get_connection

class Autor:
    _conexao = None
    def __init__(self, nome, nacionalidade, id=None):
        self.id = id
        self.nome = nome
        self.nacionalidade = nacionalidade

    @classmethod
    def _obter_conexao(cls):
        if cls._conexao is None or getattr(cls._conexao, "closed", 0):
            cls._conexao = get_connection()
        return cls._conexao

    def salvar(self):
        conexao = self._obter_conexao()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO autor (nome, nacionalidade) "
                "VALUES (%s, %s) RETURNING id_autor;",
                (self.nome, self.nacionalidade),
            )
            self.id = cursor.fetchone()[0]
            conexao.commit()
            cursor.close()
            return self.id
        except Exception:
            conexao.rollback()
            raise

    @classmethod
    def listar_todos(cls):
        conexao = cls._obter_conexao()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "SELECT id_autor, nome, nacionalidade "
                "FROM autor ORDER BY id_autor;"
            )
            linhas = cursor.fetchall()
            cursor.close()
            return [cls(nome, nacionalidade, id) for id, nome, nacionalidade in linhas]
        except Exception:
            conexao.rollback()
            raise

    @classmethod
    def buscar_por_id(cls, id):
        conexao = cls._obter_conexao()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "SELECT id_autor, nome, nacionalidade "
                "FROM autor WHERE id_autor = %s;",
                (id,),
            )
            linha = cursor.fetchone()
            cursor.close()
            if linha is None:
                return None
            return cls(linha[1], linha[2], linha[0])
        except Exception:
            conexao.rollback()
            raise

    def atualizar(self):
        conexao = self._obter_conexao()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "UPDATE autor SET nome = %s, nacionalidade = %s "
                "WHERE id_autor = %s;",
                (self.nome, self.nacionalidade, self.id),
            )
            alterado = cursor.rowcount > 0
            conexao.commit()
            cursor.close()
            return alterado
        except Exception:
            conexao.rollback()
            raise

    @classmethod
    def excluir(cls, id):
        conexao = cls._obter_conexao()
        try:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM autor WHERE id_autor = %s;", (id,))
            excluido = cursor.rowcount > 0
            conexao.commit()
            cursor.close()
            return excluido
        except Exception:
            conexao.rollback()
            raise
