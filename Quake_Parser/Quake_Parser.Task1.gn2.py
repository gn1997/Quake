

#Task 1

#Parser para o arquivo de log games.log.

#O arquivo games.log é gerado pelo servidor de quake 3 arena.
#Ele registra todas as informações dos jogos, quando um jogo começa,
#quando termina, quem matou quem, quem morreu pq caiu no vazio,
#quem morreu machucado, entre outros.

#O parser é capaz de ler o arquivo: "games.log" .
#No fim gera um arquivo json: 'Quake.json', com as informações do jogo .


import json

players = []

def findPlayer(id): 
    #Retorna a posição de um jogador na lista após busca-lo pela lista de acordo com o id.
    #id = id do jogador

    for i in range(0, len(players)):
        if players[i]['id'] == id:
            return i
    return -1

def addPlayer(id):
    #Cria um dicionario para o jogador e o adiciona na lista de jogadores
    #id = id do jogador

    player = {
            "id": int(id),
            "nome": " ",
            "kills": 0,
            "old_names": []
        }
    players.append(player)

def changeName(pos, new_name):
    #Altera o nome de um jogador e atualiza a lista de nomes antigos.
    #pos = posição do jogador na lista de jogadores
    #new_name = novo nome do jogador

    #Checa se o nome atual é diferente do novo
    if players[pos]['nome'] != new_name:
        #Busca o novo nome na lista de nomes antigos, se encontrar o remove, senão o adiciona
        verification = False
        for name in players[pos]['old_names']:
            if name == new_name:
                verification = True
        
        if verification == True:
            players[pos]['old_names'].remove(new_name)
        else:
            if players[pos]['nome'] != ' ':
                players[pos]['old_names'].append(players[pos]['nome'])

        #Troca o nome
        players[pos]['nome'] = new_name

def killCount(killer_id, killed_id):
    #Adiciona uma kill caso um jogador tenha eliminado ou subtrai caso tenha morrido pelo <world>
    #killer_id = id do jogador que matou
    #killed_id = id do jogador que morreu

    if killer_id == 1022:
        pos = findPlayer(killed_id)
        if players[pos]['kills'] != 0:
            players[pos]['kills'] -= 1
    else:
        pos = findPlayer(killer_id)
        players[pos]['kills'] += 1

def finish(game_count, total_kills, game_list):
    #Organiza o jogo finalizado em um dicionario e o adiciona na lista de jogos
    #game_count = valor do jogo atual
    #total_kills = valor total de mortes que ocorreram no jogo
    #game_list = lista de jogos

    status = {
        'total_kills': total_kills,
        'players': players
    }
    
    dicionario = {
        'game': game_count,
        'status': status
    }

    game_list.append(dicionario)






def main():
    #Variaveis
    global players
    game_count = 0
    total_kills = 0
    game_list = []

    #Abre o arquivo de texto
    with open("games.log", "r") as arquivo:
        #print("Abrir o arquivo")
        quake_lines = arquivo.readlines()


    #Loop que analisa as linhas
    for line in quake_lines:
        line = line.strip()
        line = line.split(" ", 3)

        #print(line)# printa as linhas para analise da formatação 

        #Adiciona um jogador
        if line[1] == "ClientConnect:":
            addPlayer(int(line[2]))

        #Remove um jogador da lista
        elif line[1] == "ClientDisconnect:":
            id = int(line[2])
            players.pop(findPlayer(id))

        #Termina um jogo e limpa as variaveis para o proximo
        elif line[1] == "ShutdownGame:":
            game_count += 1

            finish(game_count, total_kills, game_list)

            total_kills = 0
            players = []

        #Altera o nome do jogador
        elif line[1] == "ClientUserinfoChanged:":
            line[3] = line[3].split("\\")
            
            id = int(line[2])
            pos = findPlayer(id)
            
            changeName(pos, line[3][1])
        
        #Contabiliza as mortes
        if line[1] == "Kill:":
            line[3] = line[3].split(" ", 2)

            killer_id = int(line[2])
            killed_id = int(line[3][0])

            killCount(killer_id, killed_id)
            total_kills += 1
            

    #Escreve o dicionario de jogos em um .json
    with open('Quake.json', "w") as arq_json:
        json.dump(game_list, arq_json, indent=4)


main()
