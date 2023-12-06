# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                              Tabela de Classificação 1ª Divisão Liga Portuguesa                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
Gestão de Tabela de Liga de Futebol

Este programa foi criado para gerir a tabela de classificação da 1.ª Divisão da liga de futebol portuguesa.
Oferece funcionalidades para atualizar os resultados dos jogos, exibir graficamente a tabela atual e lidar com
autenticação de utilizador.

Utilização:
1. Lê e atualiza uma tabela da liga armazenada em 'tabela_classificacao.txt'.
2. O utilizador é solicitado a fazer autenticação usando credenciais armazenadas em 'credenciais.txt'.
3. Após uma autenticação bem-sucedida, o utilizador pode inserir o resultado do jogo para atualizar a tabela da liga.
4. A tabela atualizada é então exibida graficamente usando a biblioteca matplotlib.

Observação:
- Os nomes das 3 equipas "principais" são insensíveis a maiúsculas e minúsculas e podem ser inseridos de diversas formas
 para maior conveniência,
todas as outras terão de ser escritas exatamente como se encontram no ficheiro inicial.
- Tem algumas funcionalidades limitadas e temos outras que queremos implementar. A aguardar ‘updates’ futuros.
"""

# Biblioteca para componente gráfica
import matplotlib.pyplot as plt


def logo():
    print(
        """
 ___  ___   ___ ___ ___ _ __ 
/ __|/ _ \ / __/ __/ _ \ '__|
\__ \ (_) | (_| (_|  __/ |   
|___/\___/ \___\___\___|_|                                                                        
        """
    )


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


# Chamar função quando quiser reescrever ficheiro
# reset_table_file()

# # # # # # # # # # # # # # # # # # # # # #
# Cria dicionário correspondente à tabela #
# # # # # # # # # # # # # # # # # # # # # #

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
    elif team.lower() in ("sc_feirense", "feirense"):
        return "SC_Feirense"
    elif team.lower() in ("boavista_fc", "boavista"):
        return "Boavista_FC"
    elif team.lower() in ("portimonense", "portimonense sc"):
        return "Portimonense"
    elif team.lower() in ("gil_vicente_fc", "gil vicente"):
        return "Gil_Vicente_FC"
    elif team.lower() in ("estrela_amadora", "estrela", "estrelas"):
        return "Estrela_Amadora"
    elif team.lower() in ("estoril_praia", "estoril"):
        return "Estoril_Praia"
    elif team.lower() in ("fc_vizela", "vizela"):
        return "FC_Vizela"
    elif team.lower() in ("casa_pia_ac", "casa pia"):
        return "Casa_Pia_AC"
    elif team.lower() in ("rio_ave_fc", "rio ave"):
        return "Rio_Ave_FC"
    elif team.lower() in ("gd_chaves", "chaves", "gd_chave", "chave"):
        return "GD_Chaves"
    elif team.lower() in ("fc_arouca", "arouca"):
        return "FC_Arouca"
    else:
        return False


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


# # # # # # # # #
# Autenticação  #
# # # # # # # # #


# Abre ficheiro de credenciais registadas e guarda os valores num array
with open('credenciais.txt') as file:
    cred = file.readlines()

# Cria um array para os ‘users’, e outro para as senhas
user_data, pw_data = [], []
for line in cred:
    u, p = line.split(",")
    user_data.append(u)
    pw_data.append(p)

# Numero de tentativas
tentativas = 3

# Pede nome e password
request_credentials = True
while request_credentials:
    user_input, pw_input = input("Username: "), input("Password: ")

    # Se as credenciais estiverem corretas, autentica
    if user_input in user_data and pw_input in pw_data:
        request_credentials = False

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
                while True:
                    goals_A = input(f"Digite o número de golos marcados pelo {team_A}: ")
                    try:
                        goals_A = int(goals_A)
                        if goals_A >= 0:
                            break
                        else:
                            print("Por favor, insira um número inteiro positivo para os golos.")
                    except ValueError:
                        print("Por favor, insira um número inteiro para os golos.")

                # Input do nome da equipa B
                team_B = ""
                input_key_B = False
                while not input_key_B:
                    team_B = input("Digite o nome da outra equipa: ")
                    input_key_B = input_key(team_B)

                # Input de golos da equipa B
                while True:
                    goals_B = input(f"Digite o número de golos marcados pelo {team_B}: ")
                    try:
                        goals_B = int(goals_B)
                        if goals_B >= 0:
                            break
                        else:
                            print("Por favor, insira um número inteiro positivo para os golos.")
                    except ValueError:
                        print("Por favor, insira um número inteiro para os golos.")

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
                    tab[input_key_A]['J'] += 1
                    tab[input_key_A]['V'] += 1
                    tab[input_key_A]['Pts'] += 3

                    tab[input_key_B]['J'] += 1
                    tab[input_key_B]['D'] += 1

                # Vitória B & Derrota A
                elif goals_B > goals_A:
                    tab[input_key_B]['J'] += 1
                    tab[input_key_B]['V'] += 1
                    tab[input_key_B]['Pts'] += 3

                    tab[input_key_A]['J'] += 1
                    tab[input_key_A]['D'] += 1

                # Empate para ambos
                else:
                    tab[input_key_A]['J'] += 1
                    tab[input_key_A]['E'] += 1
                    tab[input_key_A]['Pts'] += 1

                    tab[input_key_B]['J'] += 1
                    tab[input_key_B]['E'] += 1
                    tab[input_key_B]['Pts'] += 1

                # Update
                tab_update()

            elif choice == "2":
                # Display
                display_table(tab)

            elif choice == '3':
                sure = input("Tem a certeza? (s/n)")
                if sure in ("s", "sim"):
                    # Reset table
                    tab.clear()
                    reset_table_file()
                    print("Valores de tabela reiniciados!")

            print("Fechando programa... Até já!")

    # Decrementa número de tentativas
    else:
        tentativas -= 1
        # Quando as tentativas se esgotarem, nega acesso
        if tentativas == 0:
            request_credentials = False
            print("Acesso negado.")
        # Pede ‘login’ novamente, mostra número de tentativas restantes
        else:
            print(f"Tente outra vez. Tem {tentativas} tentativas.")
