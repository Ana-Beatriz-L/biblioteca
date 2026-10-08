"""View do menu principal (PESSOA 1)."""


class MenuPrincipalView:
    def exibir_menu(self):
        print("\nMenu Principal")
        print("1. Gerenciar autor")
        print("2. Gerenciar livro")
        print("3. Sair")
        return input("Escolha uma opção: ").strip()

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
