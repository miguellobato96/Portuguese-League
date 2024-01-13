import matplotlib.pyplot as plt  # Library for graphical representation of the table


# Logo
def logo():
    print(
        """
 ___  ___   ___ ___ ___ _ __ 
/ __|/ _ \ / __/ __/ _ \ '__|
\__ \ (_) | (_| (_|  __/ |   
|___/\___/ \___\___\___|_|                                                                        
        """
    )


# Creates a dictionary corresponding to the table
def read_table():
    # Opens the table file and creates an array with an index for each line
    with open('league_table.txt', 'r') as file:
        tab_arr = file.readlines()

    # Saves the headers present in the first line
    titles = tab_arr[0].strip().split(",")

    # Creates an empty dictionary
    tab = {}

    # For each line saved in the array starting from index 1:
    for line in tab_arr[1:]:
        # Splits each word by comma, creating an array where each index is a word
        data = line.split(",")

        # Saves the team name
        equipa = data[0]
        # Saves the rest of the information
        games, wins, losses, draws, goals_scored, goals_conceded, goals_diff, points = map(int, data[1:9])

        # Fills the dictionary:
        tab[equipa] = {
            'G': games,
            'W': wins,
            'L': losses,
            'D': draws,
            'GS': goals_scored,
            'GC': goals_conceded,
            'GD': goals_diff,
            'Pts': points
        }

    return titles, tab


titles, tab = read_table()


# Updates the table with changes made by the user
def tab_update():
    with open('league_table.txt', 'w') as file:
        # Writes headers
        file.write(",".join(titles) + "\n")

        # Writes data for each team
        for team, data in tab.items():
            file.write(
                f"{team},{data['G']},{data['W']},{data['L']},{data['D']},{data['GS']},{data['GC']},{data['GD']},"
                f"{data['Pts']}\n")


# Graphically displays the table
def display_table(tab):
    # Sorts the teams based on points and goal difference (DG)
    sorted_teams = sorted(tab.items(), key=lambda x: (x[1]['Pts'], x[1]['GD']), reverse=True)

    # Extracts data for the table
    team = [team[0].replace("_", " ") for team in sorted_teams]
    games = [team[1]['G'] for team in sorted_teams]
    wins = [team[1]['W'] for team in sorted_teams]
    draws = [team[1]['D'] for team in sorted_teams]
    losses = [team[1]['L'] for team in sorted_teams]
    goals_scored = [team[1]['GS'] for team in sorted_teams]
    goals_conceded = [team[1]['GC'] for team in sorted_teams]
    goals_diff = [team[1]['GD'] for team in sorted_teams]
    points = [team[1]['Pts'] for team in sorted_teams]

    # Table
    plt.figure(figsize=(12, 6))
    plt.title("1st Division Portuguese League Standings")
    plt.axis("off")

    # Define table data
    table_data = [team, games, wins, draws, losses, goals_scored, goals_conceded, goals_diff, points]

    # Transpose table data for correct plotting
    table_data = list(map(list, zip(*table_data)))

    # Define headers
    table_headers = ["Teams", "G", "W", "D", "L", "GS", "GC", "GD", "Pts"]

    # Table columns
    plt.table(cellText=table_data, loc="center", cellLoc="center", colLabels=table_headers, colWidths=[0.125] * 9)

    plt.show()


# Resets the table
def reset_table_file():
    with open('league_table.txt', 'w') as file:
        file.write("Team,G,W,L,D,GS,GC,GD,Pts\n")

        teams = [
            "SL_Benfica", "Sporting_CP", "FC_Porto", "SC_Braga", "Moreirense_FC",
            "Vitoria_SC", "FC_Famalicao", "SC_Farence", "Boavista_FC", "Portimonense",
            "Gil_Vicente_FC", "Estrela_Amadora", "Estoril_Praia", "FC_Vizela",
            "Casa_Pia_AC", "Rio_Ave_FC", "GD_Chaves", "FC_Arouca"
        ]

        for team in teams:
            file.write(f"{team}, 0, 0, 0, 0, 0, 0, 0, 0\n")


# Reads credentials.txt
def read_credentials():
    # Creates an empty dictionary
    credentials = {}

    # Opens the 'credentials.txt' file in read mode
    with open('credentials.txt', 'r') as file:
        # Iterates through each line in the file
        for line in file:
            # Splits the line into username and password, using a comma as a delimiter
            username, password = map(str.strip, line.split(","))

            # Adds the username and corresponding password to the credentials dictionary
            credentials[username] = password

    return credentials


'''
This method PREVENTS the user from authenticating with a password
that exists in the file BUT does not match the provided username
'''

# Asks the user for authentication data and compares it with the database
def authenticate_user(credentials):
    attempts = 3

    while attempts > 0:
        # Prompts the user for input for username and password
        user_input, pw_input = input("Username: "), input("Password: ")

        # Checks if the username is in the credentials and if the password is correct
        if user_input in credentials and credentials[user_input] == pw_input:
            return True
        
        # Decrements the number of attempts
        attempts -= 1
        # Prompts for 'login' again, shows the number of remaining attempts
        print(f"Try again. {attempts} attempts remaining.")
        

    # When attempts are exhausted, denies access
    print("Access denied.")

    return False


# Receives the team name to which the user refers and returns the corresponding key
def input_key(team):
    if team.lower() in ("slb", "benfas", "ben", "benfica", "sport lisboa e benfica", "slbenfica", "sl_benfica"):
        return "SL_Benfica"
    elif team.lower() in ("scp", "sporting", "sporting clube de portugal", "spo", "sport", "sportingcp", "sporting_cp"):
        return "Sporting_CP"
    elif team.lower() in (
            "porto", "fc porto", "port", "porto futebol clube", "fcp", "futebol clube do porto", "fcporto", "fc_porto"):
        return "FC_Porto"
    elif team.lower() in ("braga", "bracarenses", "braga sporting clube", "braga", "Braga fc", "Bragafc"):
        return "SC_Braga"
    elif team.lower() in ("Moreirenses", "Moreirense", "Moreira", "Moreiras",):
        return "Moreirense_FC"
    elif team.lower() in (
            "vitoria_sc", "vitoria", "vitoria sport clube", "vitória_sc", "vitória", "vitória sport clube"):
        return "Vitoria_SC"
    elif team.lower() in ("fc_famalicao", "famalicao", "fc_famalicão", "famalicão"):
        return "FC_Famalicao"
    elif team.lower() in ("sc_feirense", "feirense", "sc feirense", "feira"):
        return "SC_Feirense"
    elif team.lower() in ("boavista_fc", "boavista", "boavista fc", "boa vista"):
        return "Boavista_FC"
    elif team.lower() in ("portimonense", "portimonense sc", "porti"):
        return "Portimonense"
    elif team.lower() in ("gil_vicente_fc", "gil vicente", "vicente", "gil", "gil vicente fc"):
        return "Gil_Vicente_FC"
    elif team.lower() in ("estrela_amadora", "estrela", "estrelas", "estrela amadora", "amadora"):
        return "Estrela_Amadora"
    elif team.lower() in ("estoril_praia", "estoril", "estoril praia"):
        return "Estoril_Praia"
    elif team.lower() in ("fc_vizela", "vizela", "fc vizela"):
        return "FC_Vizela"
    elif team.lower() in ("casa_pia_ac", "casa pia", "casa pia ac"):
        return "Casa_Pia_AC"
    elif team.lower() in ("rio_ave_fc", "rio ave", "rio ave fc"):
        return "Rio_Ave_FC"
    elif team.lower() in ("gd_chaves", "chaves", "gd chaves", "chave"):
        return "GD_Chaves"
    elif team.lower() in ("fc_arouca", "arouca", "fc arouca"):
        return "FC_Arouca"
    else:
        print("That name is not registered with any club in the league.")
        return False


# Receives the team name entered by the user and asks for the number of goals scored until a valid value is entered
def get_goals_input(team_name):
    while True:
        goals_input = input(f"Enter the number of goals scored by {team_name}: ")
        try:
            goals = int(goals_input)
            if goals >= 0:
                return goals
            else:
                print("Please enter a positive integer for the goals.")
        except ValueError:
            print("Please enter an integer for the goals.")


# Receives the key corresponding to the team from the input, its result (V, D, E), and increments the values for the number of games and points
def update_team_stats(team_key, result):
    tab[team_key]['G'] += 1
    tab[team_key][result] += 1

    if result == 'W':
        tab[team_key]['Pts'] += 3
    elif result == 'D':
        tab[team_key]['Pts'] += 1


# Receives the final values of the names and goals of each team and updates the corresponding additional information
def update_scores(input_key_A, goals_A, input_key_B, goals_B):
    # Goals Scored
    tab[input_key_B]['GS'] += goals_B
    tab[input_key_A]['GS'] += goals_A

    # Goals Conceded
    tab[input_key_A]['GC'] += goals_B
    tab[input_key_B]['GC'] += goals_A

    # Goal Difference
    tab[input_key_A]['GD'] = tab[input_key_A]['GM'] - tab[input_key_A]['GS']
    tab[input_key_B]['GD'] = tab[input_key_B]['GM'] - tab[input_key_B]['GS']

    # Win A & Loss B
    if goals_A > goals_B:
        update_team_stats(input_key_A, 'W')
        update_team_stats(input_key_B, 'L')
    # Win B & Loss A
    elif goals_B > goals_A:
        update_team_stats(input_key_B, 'W')
        update_team_stats(input_key_A, 'L')
    # Draw for both
    else:
        update_team_stats(input_key_A, 'D')
        update_team_stats(input_key_B, 'D')
