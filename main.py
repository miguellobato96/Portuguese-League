# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                              Tabela de Classificação 1ª Divisão Liga Portuguesa                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
Gestão de Tabela de Liga de Futebol

Este programa foi criado para gerir a tabela de classificação da 1ª Divisão da liga de futebol portuguesa. 
Oferece funcionalidades para atualizar os resultados dos jogos, exibir graficamente a tabela atual e lidar com autenticação de usuário.

Utilização:
1. Lê e atualiza uma tabela da liga armazenada em 'tabela_classificacao.txt'.
2. O usuário é solicitado a fazer autenticação usando credenciais armazenadas em 'credenciais.txt'.
3. Após uma autenticação bem-sucedida, o usuário pode inserir o resultado do jogo para atualizar a tabela da liga.
4. A tabela atualizada é então exibida graficamente usando a biblioteca matplotlib.

Observação:
- Os nomes das 3 equipas "principais" são insensíveis a maiúsculas e minúsculas e podem ser inseridos de diversas formas para maior conveniência,
todas as outras terão de ser escritas exatamente como se encontram no ficheiro inicial.
- Tem algumas funcionalidades limitadas e temos outras que queremos implementar. A aguardar updates futuros.
"""
# Biblioteca para componente gráfica
import matplotlib.pyplot as plt

# Função que "zera" a tabela
def reset_table_file():
    team_lines = "{},{},{},{},{},{},{},{},{}\n"

    with open('tabela_classificacao.txt', 'w') as file:
        file.write("Clube,J,V,D,E,GM,GS,DG,Pts\n")
        
        teams = [
            "SL_Benfica", "Sporting_CP", "FC_Porto", "SC_Braga", "Moreirense_FC",
            "Vitoria_SC", "FC_Famalicao", "SC_Farence", "Boavista_FC", "Portimonense",
            "Gil_Vicente_FC", "Estrela_Amadora", "Estoril_Praia", "FC_Vizela",
            "Casa_Pia_AC", "Rio_Ave_FC", "GD_Chaves", "FC_Arouca"
        ]

        for team in teams:
            file.write("team, 0, 0, 0, 0, 0, 0, 0, 0\n")

# Chamar função quando quiser reescrever ficheiro
# reset_table_file()

# # # # # # # # # # # # # # # # # # # # # #
# Cria dicionário correspondente à tabela #
# # # # # # # # # # # # # # # # # # # # # #

# Abre ficheiro tabela e cria um array, com um index para cada linha
with open('tabela_classificacao.txt', 'r') as file:
    tab_arr = file.readlines()

# Guarda os cabeçalhos, que se encontram na primeira linha
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
             'GM' : golos_marcados,
             'GS' : golos_sofridos,
             'DG' : dif_golos,
             'Pts': pontos
        }

# Função que reescreve tabela_classificacao.txt
def tab_update():
      with open('tabela_classificacao.txt', 'w') as file:   
        # Escreve cabeçalhos
        file.write(",".join(titles) + "\n")

        # Escreve os dados para cada equipa
        for team, data in tab.items():
            file.write(f"{team},{data['J']},{data['V']},{data['D']},{data['E']},{data['GM']},{data['GS']},{data['DG']},{data['Pts']}\n")

# Função que recebe o nome da equipa à qual o user se refere e retorna a key correspondente
def input_key(team):
    if team.lower() in ("slb", "benfas", "ben", "benfica", "sport lisboa e benfica", "slbenfica", "sl_benfica"):
        return "SL_Benfica"
    elif team.lower() in ("scp", "sporting", "sporting clube de portugal", "spo", "sport", "sportingcp", "sporting_cp"):
        return "Sporting_CP"
    elif team.lower() in ("porto", "fc porto", "port", "porto futebol clube", "fcp", "futebol clube do porto", "fcporto", "fc_porto"):
        return "FC_Porto"
    else:
        return team

# Função que mostra a gráficamente a tabela
def display_table(tab):
    # Ordena as equipas com base nos pontos e diferença de golos (DG)
    sorted_teams = sorted(tab.items(), key=lambda x: (x[1]['Pts'], x[1]['DG']), reverse=True)

    # Extrai os dados para tabela
    equipa = [team[0].replace("_"," ") for team in sorted_teams]
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

# Abre ficheiro de credenciais registadas e guarda os valores dentro de um array
with open('credenciais.txt') as file:
    cred = file.readlines()

# Cria um array para os users, e outro array para as passwords
user_data, pw_data = [], []    
for line in cred:
    u, p = line.split(",")    
    user_data.append(u)
    pw_data.append(p)

# Numero de tentativas
tentativas = 3

# Pede nome e password
request_credentials = True
while request_credentials == True:
    user_input, pw_input = input("Username: "), input("Password: ")

    # Se as credenciais estiverem corretas, autentica
    if user_input in user_data and pw_input in pw_data:
        request_credentials = False

        # Pede inputs
        team_A = input("Digite o nome de uma equipa: ")
        goals_A = int(input(f"Digite o número de golos marcados pelo {team_A}: "))

        team_B = input("Digite o nome da outra equipa: ")
        goals_B = int(input(f"Digite o número de golos marcados pelo {team_B}: "))

        # Guarda a key 
        input_key_A = input_key(team_A)
        input_key_B = input_key(team_B)

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

        # Display
        display_table(tab)
            
    # Decrementa número de tentativas 
    else:
        tentativas -= 1
        # Quando as tentativas se esgotarem, nega acesso
        if tentativas == 0:
            request_credentials = False
            print("Acesso negado.")
        # Pede login novamente, mostra número de tentativas restantes
        else: 
            print(f"Tente outra vez. Tem {tentativas} tentativas.")
