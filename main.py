# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                              Tabela de Classificação 1ª Divisão Liga Portuguesa                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from functions import *  # Import ficheiro functions.py

# Autenticação
if read_credentials():
    authenticated = authenticate_user(read_credentials())
    # Se as credenciais estiverem corretas, autentica
    if authenticated:
        choice = ""
        while choice != "4":
            titles, tab = read_table()
            logo()
            print("--- Menu ---")
            print("1. Introduzir Novo Resultado")
            print("2. Consultar Tabela")
            print("3. Reiniciar Tabela")
            print("4. Fechar Programa")
            choice = input("Escolha uma opção (1-4): ")

            if choice == "1":
                # Input do nome da equipa A
                team_A = ""
                input_key_A = False
                while not input_key_A:
                    team_A = input("Digite o nome de uma equipa: ")
                    input_key_A = input_key(team_A)

                # Input de golos da equipa A
                goals_A = get_goals_input(team_A)

                # Input do nome da equipa B
                team_B = ""
                input_key_B = False
                while not input_key_B:
                    team_B = input("Digite o nome da outra equipa: ")
                    input_key_B = input_key(team_B)

                # Input de golos da equipa B
                goals_B = get_goals_input(team_B)

                # Update valores correspondentes a cada equipa
                update_scores(input_key_A, goals_A, input_key_B, goals_B)

                # Update
                tab_update()

            elif choice == "2":
                # Display
                display_table(tab)

            elif choice == "3":
                sure = input("Tem a certeza? (s/n)")
                if sure in ("s", "sim"):
                    # Reset table
                    tab.clear()
                    reset_table_file()
                    print("Valores de tabela reiniciados!")

            elif choice == "4":
                print("Fechando programa... Até já!")

            else:
                print("Opção inválida!")
