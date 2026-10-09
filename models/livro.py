from database import get_connection


class LivroModel:
    def __init__(self):
        self.conexao = None
        try:
            self.conexao = get_connection()
        except Exception as e:
            print("Erro ao conectar ao banco:", e)

    def _rollback(self):
        """Desfaz a transação em caso de erro (evita o banco travar)."""
        try:
            self.conexao.rollback()
        except Exception:
            pass

    def listar_livros(self):
        """Retorna (id, titulo, ano_publicacao, nome_do_autor) usando JOIN."""
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "SELECT l.id_livro, l.titulo, l.ano_publicacao, a.nome, a.id_autor "
                "FROM livro l JOIN autor a ON a.id_autor = l.autor_id "
                "ORDER BY l.id_livro;"
            )
            livros = cursor.fetchall()
            cursor.close()
            return livros
        except Exception as e:
            print("Erro ao listar livros:", e)
            self._rollback()
            return []

    def autor_existe(self, autor_id):
        """True se existe um autor com esse id."""
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "SELECT 1 FROM autor WHERE id_autor = %s;",
                (autor_id,),
            )
            existe = cursor.fetchone() is not None
            cursor.close()
            return existe
        except Exception as e:
            print("Erro ao verificar autor:", e)
            self._rollback()
            return False

    def livro_existe(self, id_livro):
        """True se existe um livro com esse id."""
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "SELECT 1 FROM livro WHERE id_livro = %s;",
                (id_livro,),
            )
            existe = cursor.fetchone() is not None
            cursor.close()
            return existe
        except Exception as e:
            print("Erro ao verificar livro:", e)
            self._rollback()
            return False

    def inserir_livro(self, titulo, ano_publicacao, autor_id):
        """Retorna True se salvou, False se deu erro."""
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "INSERT INTO livro (titulo, ano_publicacao, autor_id) "
                "VALUES (%s, %s, %s);",
                (titulo, ano_publicacao, autor_id),
            )
            self.conexao.commit()
            cursor.close()
            return True
        except Exception as e:
            print("Erro ao inserir livro:", e)
            self._rollback()
            return False

    def atualizar_livro(self, id_livro, titulo, ano_publicacao, autor_id):
        """Retorna True se atualizou, False se deu erro."""
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "UPDATE livro SET titulo = %s, ano_publicacao = %s, autor_id = %s "
                "WHERE id_livro = %s;",
                (titulo, ano_publicacao, autor_id, id_livro),
            )
            self.conexao.commit()
            cursor.close()
            return True
        except Exception as e:
            print("Erro ao atualizar livro:", e)
            self._rollback()
            return False

    def excluir_livro(self, id_livro):
        """Retorna True se excluiu, False se deu erro."""
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "DELETE FROM livro WHERE id_livro = %s;",
                (id_livro,),
            )
            self.conexao.commit()
            cursor.close()
            return True
        except Exception as e:
            print("Erro ao excluir livro:", e)
            self._rollback()
            return False