class Initialize():

    def show_menu(self):
        print('\n')

        print(50 * '-')
        print('Bem-vindo ao Hospital!')
        print(50 * '-')

        print('1 - Pacientes')
        print('2 - Consultas')
        print('3 - Procedimentos')
        print('4 - Sair') 

    def choose_option(self):
        option = input('\nEscolha uma das opções: ')

        if option != '1' and option != '2' and option != '3' and option != '4':
            print('\nOpção inválida!')

        return option

    def to_go_out(self):
        print('\nObrigado, volte sempre!')

if __name__ == "__main__":
    init = Initialize()
    option = ''

    while option != '4':
        init.show_menu()
        option = init.choose_option()

        if option == '1':
            pass

        elif option == '2':
            pass

        elif option == '3':
            pass

        elif option == '4':
            init.to_go_out()
