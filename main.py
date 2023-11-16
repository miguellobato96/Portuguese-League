# Tabela de Classificação 1ª Divisão Liga Portuguesa
# Equipa | Jogos | Vitórias | Derrotas | Empates | Pontos

# import pandas as pd

# Abre ficheiro de credenciais registadas e guarda esse valores
with open("credenciais.txt") as file:
        cred = file.readlines()
        user_data, pw_data = [], []    
        for el in cred:
            u, p = el.split(",")    
            user_data.append(u)
            pw_data.append(p)

# Autenticação
tentativas = 3
while tentativas > 0:
    user_input, pw_input = input("Username: "), input("Password: ")

    if user_input in user_data and pw_input in pw_data:
        pass
    else:
        print("Tente outra vez.")
        tentativas =- 1
        
# Se as tentativas se esgotarem:
print("Acesso negado.")

# Input de equipa
def team_input():
    team_input = input("Insira a equipa: ").lower()
    return team_input

with open ("tabela_classificacao.txt") as file:
    cred = file.readlines()
    team_name = []

if team_input in team_name: 
    pass


# Input de resultado
def result_input():
    return input("Insira o resultado: ") #.lower()

# Update de tabela
tab = {}
keys = ["Equipa", "Jogos", "Vitórias", "Derrotas", "Empates", "Pontos"]
with open("tabela_classificacao.txt") as tab_txt:
    for line in tab_txt:
        (team, games, wins, loses, draws, points) = line.split()
        