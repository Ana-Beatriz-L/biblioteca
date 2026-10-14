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
        nome = input("Nome do autor: ").strip()
        nacionalidade = input("Nacionalidade: ").strip()
        return nome, nacionalidade

    def ler_id(self, acao):
        try:
            return int(input(f"Informe o ID do autor a {acao}: "))
        except ValueError:
            print("ID inválido! Deve ser um número inteiro.")
            return None

    def mostrar_autores(self, autores):
        print("\n=== Lista de Autores ===")
        if not autores:
            print("Nenhum autor encontrado.")
        else:
            for autor in autores:
                print(
                    f"ID do Autor: {autor.id} | Nome: {autor.nome} | "
                    f"Nacionalidade: {autor.nacionalidade}"
                )
