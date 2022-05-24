# Quake Parser
Parser para o arquivo de log: games.log. 
O arquivo games.log é gerado pelo servidor de quake 3 arena. 
Ele registra todas as informações dos jogos, quando um jogo começa, 
quando termina, quem matou quem, quem morreu pq caiu no vazio, 
quem morreu machucado, entre outros.  
O parser é capaz de ler o arquivo: "games.log" . 
No fim gera um arquivo json: 'Quake.json', com as informações do jogo.

# Tarefa princial(Main)
O programa separa o arquivo linha por linha e as transforma em listas. O arquivo então analisa as linhas e busca alterações na partida e de acordo com as alterações, cria e modifica um dicionario que contem as informações da partida.

O programa então agrupa os dicionarios das partidas em uma grande lista de partidas e finaliza o inserindo em um .json.
