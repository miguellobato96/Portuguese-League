import matplotlib.pyplot as plt


# Logótipo
def logo():
    print(
        """
 ___  ___   ___ ___ ___ _ __ 
/ __|/ _ \ / __/ __/ _ \ '__|
\__ \ (_) | (_| (_|  __/ |   
|___/\___/ \___\___\___|_|                                                                        
        """
    )


# Cria dicionário correspondente à tabela
def read_table():
    # Abre ficheiro tabela e cria um array, com um index para cada linha
    with open('tabela_classificacao.txt', 'r') as file:
        tab_arr = file.readlines()

    # Guarda os cabeçalhos presentes na primeira linha
    titles = tab_arr[0].strip().split(",")

    # Cria dicionário vazio
    tab = {}

    # Para cada linha guardada no array a partir do index 1:
    for line in tab_arr[1:]:
        # Separa cada palavra pela vírgula, criando um array onde cada index é uma palavra
        data = line.split(",")

        # Guarda o nome da equipa
        equipa = data[0]
        # Guarda a restante informação
        jogos, vitorias, derrotas, empates, golos_marcados, golos_sofridos, dif_golos, pontos = map(int, data[1:9])

        # Preenche o dicionário:
        tab[equipa] = {
            'J': jogos,
            'V': vitorias,
            'D': derrotas,
            'E': empates,
            'GM': golos_marcados,
            'GS': golos_sofridos,
            'DG': dif_golos,
            'Pts': pontos
        }

    return titles, tab


titles, tab = read_table()


# Função que reescreve tabela_classificacao.txt
def tab_update():
    with open('tabela_classificacao.txt', 'w') as file:
        # Escreve cabeçalhos
        file.write(",".join(titles) + "\n")

        # Escreve os dados para cada equipa
        for team, data in tab.items():
            file.write(
                f"{team},{data['J']},{data['V']},{data['D']},{data['E']},{data['GM']},{data['GS']},{data['DG']},"
                f"{data['Pts']}\n")


# Função que mostra a gráficamente a tabela
def display_table(tab):
    # Ordena as equipas com base nos pontos e diferença de golos (DG)
    sorted_teams = sorted(tab.items(), key=lambda x: (x[1]['Pts'], x[1]['DG']), reverse=True)

    # Extrai os dados para tabela
    equipa = [team[0].replace("_", " ") for team in sorted_teams]
    jogos = [team[1]['J'] for team in sorted_teams]
    vitorias = [team[1]['V'] for team in sorted_teams]
    empates = [team[1]['E'] for team in sorted_teams]
    derrotas = [team[1]['D'] for team in sorted_teams]
    golos_marcados = [team[1]['GM'] for team in sorted_teams]
    golos_sofridos = [team[1]['GS'] for team in sorted_teams]
    dif_golos = [team[1]['DG'] for team in sorted_teams]
    pontos = [team[1]['Pts'] for team in sorted_teams]

    # Tabela
    plt.figure(figsize=(12, 6))
    plt.title("Tabela de Classificação 1ª Divisão Liga Portuguesa")
    plt.axis("off")

    # Definir dados da tabela
    table_data = [equipa, jogos, vitorias, empates, derrotas, golos_marcados, golos_sofridos, dif_golos, pontos]

    # Transpor os dados da tabela para plotagem correta
    table_data = list(map(list, zip(*table_data)))

    # Definir cabeçalhos
    table_headers = ["Equipas", "J", "V", "E", "D", "GM", "GS", "DG", "Pts"]

    # Colunas da tabela
    plt.table(cellText=table_data, loc="center", cellLoc="center", colLabels=table_headers, colWidths=[0.125] * 9)

    plt.show()


# Função que "zera" a tabela
def reset_table_file():
    with open('tabela_classificacao.txt', 'w') as file:
        file.write("Clube,J,V,D,E,GM,GS,DG,Pts\n")

        teams = [
            "SL_Benfica", "Sporting_CP", "FC_Porto", "SC_Braga", "Moreirense_FC",
            "Vitoria_SC", "FC_Famalicao", "SC_Farence", "Boavista_FC", "Portimonense",
            "Gil_Vicente_FC", "Estrela_Amadora", "Estoril_Praia", "FC_Vizela",
            "Casa_Pia_AC", "Rio_Ave_FC", "GD_Chaves", "FC_Arouca"
        ]

        for team in teams:
            file.write(f"{team}, 0, 0, 0, 0, 0, 0, 0, 0\n")


# Funcção que lê credenciais.txt e cria dicionário
def read_credentials():
    credentials = {}

    with open('credenciais.txt', 'r') as file:
        for line in file:
            username, password = map(str.strip, line.split(","))
            credentials[username] = password

    return credentials


def authenticate_user(credentials):
    attempts = 3

    while attempts > 0:
        user_input, pw_input = input("Username: "), input("Password: ")

        if user_input in credentials and credentials[user_input] == pw_input:
            return True

        # Pede ‘login’ novamente, mostra número de tentativas restantes
        print(f"Tente outra vez. Tem {attempts} tentativas.")
        # Decrementa número de tentativas
        attempts -= 1

        # Quando as tentativas se esgotarem, nega acesso
        if attempts == 0:
            print("Acesso negado.")

    print("Authentication failed. No more attempts remaining.")
    return False


# Função que recebe o nome da equipa à qual o ‘user’ se refere e retorna a key correspondente
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
        return False


def get_goals_input(team_name):
    while True:
        goals_input = input(f"Digite o número de golos marcados pelo {team_name}: ")
        try:
            goals = int(goals_input)
            if goals >= 0:
                return goals
            else:
                print("Por favor, insira um número inteiro positivo para os golos.")
        except ValueError:
            print("Por favor, insira um número inteiro para os golos.")


def update_team_stats(team_key, result):
    tab[team_key]['J'] += 1
    tab[team_key][result] += 1

    if result == 'V':
        tab[team_key]['Pts'] += 3
    elif result == 'E':
        tab[team_key]['Pts'] += 1


def update_scores(input_key_A, goals_A, input_key_B, goals_B):
    # Golos Marcados
    tab[input_key_B]['GM'] += goals_B
    tab[input_key_A]['GM'] += goals_A

    # Golos Sofridos
    tab[input_key_A]['GS'] += goals_B
    tab[input_key_B]['GS'] += goals_A

    # Diferença de golos
    tab[input_key_A]['DG'] = tab[input_key_A]['GM'] - tab[input_key_A]['GS']
    tab[input_key_B]['DG'] = tab[input_key_B]['GM'] - tab[input_key_B]['GS']

    # Vitória A & Derrota B
    if goals_A > goals_B:
        update_team_stats(input_key_A, 'V')
        update_team_stats(input_key_B, 'D')
    # Vitória B & Derrota A
    elif goals_B > goals_A:
        update_team_stats(input_key_B, 'V')
        update_team_stats(input_key_A, 'D')
    # Empate para ambos
    else:
        update_team_stats(input_key_A, 'E')
        update_team_stats(input_key_B, 'E')
      
