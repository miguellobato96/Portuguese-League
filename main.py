# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Tabela de Classificação 1ª Divisão Liga Portuguesa  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # Cria dicionário correspondente à tabela # # # 
# Abre ficheiro tabela e cria um array, com um index para cada linha
with open('tabela_classificacao.txt') as file:
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
        jogos, vitorias, derrotas, empates, pontos = int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5])

        # Preenche o dicionário:
        # Cria uma key com o nome da equipa guardada e, como value, cria um dicionário com a restante informação
        # ... Onde cria novamente uma key com o valor correspondente para cada informação
        tab[equipa] = {
             'jogos': jogos,
             'vitorias': vitorias,
             'derrotas': derrotas,
             'empates': empates,
             'pontos': pontos
        }

# Função que reescreve tabela_classificacao.txt
def tab_update():
      with open('tabela_classificacao.txt') as file:
            # Escreve cabeçalhos
            for title in titles:
                file.write(f"{title},")
            file.wirte("\n")
            
            # Escreve os dados para cada equipa
            for team, data in tab.items():
                file.write(f"{equipa},{data['jogos']},{data['vitorias']},{data['derrotas']},{data['empates']},{data['pontos']}\n")


# # # # # # # # #
# Autenticação  #
# # # # # # # # #

# Abre ficheiro de credenciais registadas e guarda esse valores num array
with open('credenciais.txt') as file:
        cred = file.readlines()

#Cria um array para os users e outro array para as passwords
user_data, pw_data = [], []    
for line in cred:
    u, p = line.split(",")    
    user_data.append(u)
    pw_data.append(p)

tentativas = 3
request_credentials = True
while request_credentials == True:
    user_input, pw_input = input("Username: "), input("Password: ")

    if user_input in user_data and pw_input in pw_data:
        print("OK")
        request_credentials = False
    else:
        print("Tente outra vez.")
        tentativas -= 1

        if tentativas == 0:
             request_credentials = False
             print("Acesso negado.")
        
# Input de equipa
def team_input():
    team_input = input("Insira a equipa: ").lower()
    return team_input 

# Se a equipa digitada existir na tabela, pede resultado
if team_input in tab: 
    input("Insira o resultado: ").lower()
