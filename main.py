from controllers.autor_controller import AutorController
from controllers.livro_controller import LivroController
from views.menu_principal import MenuPrincipalView


def main():
    view = MenuPrincipalView()
    autor_controller = AutorController()
    livro_controller = LivroController()

    while True:
        opcao = view.exibir_menu()
        if opcao == "1":
            autor_controller.menu()
        elif opcao == "2":
            livro_controller.menu()
        elif opcao == "3":
            view.mostrar_mensagem("Encerrando o sistema. Até logo!")
            break
        else:
            view.mostrar_mensagem("Opção inválida.")


if __name__ == "__main__":
    main()
