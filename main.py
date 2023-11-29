# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Tabela de Classificação 1ª Divisão Liga Portuguesa  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # Cria dicionário correspondente à tabela # # # 
# Abre ficheiro tabela e cria um array, com um index para cada linha
with open('tabela_classificacao.txt', 'r') as file:
    tab_data = file.readlines()

# Guarda os cabeçalhos, que se encontram na primeira linha
# ... Separando pela vírugla e tirando os "espaços (\n)" e criando um array onde cada index é um cabeçalho 
titles = tab_data[0].strip().split(",")

# Cria dicionário vazio
tab = {}

# Para cada linha guardada no array a partir do index 1:
for line in tab_data[1:]:
        # Separa cada palavra pela vírgula, criando um array onde cada index é uma palavra
        data = line.split(",")

        # Guarda o nome da equipa
        equipa = data[0]
        # Guarda a restante informação
        # ... Não se usou .strip() anteriomente porque aqui, como estamos a "transformar" tudo em int, o IDE ignora o "\n"
        jogos, vitorias, derrotas, empates, pontos, golos = int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6])

        # Preenche o dicionário:
        # Cria uma key com o nome da equipa guardada e, como value, cria um dicionário com a restante informação
        # ... Onde cria novamente uma key com o valor correspondente para cada informação
        tab[equipa] = {
             'jogos': jogos,
             'vitorias': vitorias,
             'derrotas': derrotas,
             'empates': empates,
             'pontos': pontos,
             'golos' : golos
        }

# Função que reescreve tabela_classificacao.txt
def tab_update():
      with open('tabela_classificacao.txt', 'w') as file:
            # Escreve cabeçalhos
            for title in titles:
                file.write(f"{title},")
            file.write("\n")
            
            # Escreve os dados para cada equipa
            for team, data in tab.items():
                file.write(f"{team},{data['jogos']},{data['vitorias']},{data['derrotas']},{data['empates']},{data['pontos']},{data['golos']}\n")


def input_key(team):
    if team.lower() in ("slb", "benfas", "ben", "benfica", "sport lisboa e benfica"):
        return "SL_Benfica"
    elif team.lower() in ("scp", "sporting", "sporting clube de portugal", "spo", "sport"):
        return "Sporting_CP"
    elif team.lower() in ("porto", "fc porto", "port", "porto futebol clube", "fcp", "futebol clube do porto"):
        return "FC_Porto"
    else:
        return team
    

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

# Pede o nome e password
request_credentials = True
while request_credentials == True:
    user_input, pw_input = input("Username: "), input("Password: ")

    # Se as credenciais estiverem corretas, autentica
    if user_input in user_data and pw_input in pw_data:
        request_credentials = False

        team_A = input("Digite o nome de uma equipa: ")
        goals_A = int(input(f"Digite o número de golos marcados pelo {team_A}: "))

        team_B = input("Digite o nome da outra equipa: ")
        goals_B = int(input(f"Digite o número de golos marcados pelo {team_B}: "))

        input_key_A = input_key(team_A)
        input_key_B = input_key(team_B)

        # Golos 
        tab[input_key_A]['golos'] += goals_A
        tab[input_key_B]['golos'] += goals_B

        # Vitória A & Derrota B
        if goals_A > goals_B:
            tab[input_key_A]['jogos'] += 1
            tab[input_key_A]['vitorias'] += 1
            tab[input_key_A]['pontos'] += 3

            tab[input_key_B]['jogos'] += 1
            tab[input_key_B]['derrotas'] += 1
        # Vitória B & Derrota A
        elif goals_B > goals_A:
            tab[input_key_B]['jogos'] += 1
            tab[input_key_B]['vitorias'] += 1
            tab[input_key_B]['pontos'] += 3

            tab[input_key_A]['jogos'] += 1
            tab[input_key_A]['derrotas'] += 1
        # Empate para ambos
        else: 
            tab[input_key_A]['jogos'] += 1
            tab[input_key_A]['empates'] += 1
            tab[input_key_A]['pontos'] += 1

            tab[input_key_B]['jogos'] += 1
            tab[input_key_B]['empates'] += 1
            tab[input_key_B]['pontos'] += 1

        # Update
        tab_update()
            
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
