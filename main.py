# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                              Tabela de Classificação 1ª Divisão Liga Portuguesa                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from functions import *  # Import functions.py file

# Authentication
if read_credentials():
    authenticated = authenticate_user(read_credentials())
    # If the credentials are correct, authenticate
    if authenticated:
        choice = ""
        while choice != "4":
            titles, tab = read_table()
            logo()
            print("--- Menu ---")
            print("1. Enter New Result")
            print("2. View Table")
            print("3. Restart Table")
            print("4. Close Program")
            choice = input("Choose an option (1-4): ")

            if choice == "1":
                # Team A input
                team_A = ""
                input_key_A = False
                while not input_key_A:
                    team_A = input("Enter the name of a team: ")
                    input_key_A = input_key(team_A)

                # Team A goals input
                goals_A = get_goals_input(team_A)

                # Team B input
                team_B = ""
                input_key_B = False
                while not input_key_B:
                    team_B = input("Enter the name of the other team: ")
                    input_key_B = input_key(team_B)

                # Team B goals input
                goals_B = get_goals_input(team_B)

                # Update values for each team
                update_scores(input_key_A, goals_A, input_key_B, goals_B)

                # Update
                tab_update()

            elif choice == "2":
                # Display
                display_table(tab)

            elif choice == "3":
                sure = input("Are you sure? (y/n)")
                if sure.lower() in ("y", "yes"):
                    # Reset table
                    tab.clear()
                    reset_table_file()
                    print("Table values reset!")

            elif choice == "4":
                print("Closing program... See you soon!")

            else:
                print("Invalid option!")
