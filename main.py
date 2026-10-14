from controllers.autor_controller import AutorController
from controllers.livro_controller import LivroController
from views.menu_principal import MenuPrincipalView


def gerenciar_autor(autor_controller):
    autor_controller.menu()
 
 
def gerenciar_livro(livro_controller):
    livro_controller.menu()
 
 
def sair(view):
    view.mostrar_mensagem("Encerrando o sistema. Até logo!")
 
 
def opcao_invalida(view):
    view.mostrar_mensagem("Opção inválida.")


def executar_menu(view, autor_controller, livro_controller):
    """Menu principal em loop até o usuário escolher 'Sair'."""
    while True:
        opcao = view.exibir_menu()
        if opcao == "1":
            gerenciar_autor(autor_controller)
        elif opcao == "2":
            gerenciar_livro(livro_controller)
        elif opcao == "3":
            sair(view)
            break
        else:
            opcao_invalida(view)
 
def main():
    view = MenuPrincipalView()
    autor_controller = AutorController()
    livro_controller = LivroController()
    executar_menu(view, autor_controller, livro_controller)
 
 
if __name__ == "__main__":
    main()
