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


## Task 1

Construa um parser para o arquivo de log games.log.

O arquivo `games.log` é gerado pelo servidor de quake 3 arena. Ele registra todas as informações dos jogos, quando um jogo começa, quando termina, quem matou quem, quem morreu pq caiu no vazio, quem morreu machucado, entre outros.

O parser deve ser capaz de ler o arquivo, agrupar os dados de cada jogo, e em cada jogo deve coletar as informações de morte.

### Exemplo

  	21:42 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT
  
  O player "Isgalamido" morreu pois estava ferido e caiu de uma altura que o matou.

  	2:22 Kill: 3 2 10: Isgalamido killed Dono da Bola by MOD_RAILGUN
  
  O player "Isgalamido" matou o player Dono da Bola usando a arma Railgun.
  
Para cada jogo o parser deve gerar algo como:

    game_1: {
	    total_kills: 45;
	    players: ["Dono da bola", "Isgalamido", "Zeh"]
	    kills: {
	      "Dono da bola": 5,
	      "Isgalamido": 18,
	      "Zeh": 20
	    }
	  }
