# Quake Parser

# Tarefa princial(Task Main)
O programa separa o arquivo linha por linha e as transforma em listas. O arquivo então analisa as linhas e busca alterações na partida e de acordo com as alterações, cria e modifica um dicionario que contem as informações da partida.

O programa então agrupa os dicionarios das partidas em uma grande lista de partidas e finaliza o inserindo em um arquivo: .json.


## Task 1

Parser ler o arquivo de log: games.log. 
O arquivo games.log é gerado pelo servidor de quake 3 arena. 
Ele registra todas as informações dos jogos, quando um jogo começa, 
quando termina, quem matou quem, quem morreu pq caiu no vazio, 
quem morreu machucado, entre outros. 
E em cada jogo deve coletado as informações de morte.
No fim gera um arquivo json: 'Quake.json', com as informações do jogo.

### Exemplo


  	21:42 Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT
  
  O player "Isgalamido" morreu pois estava ferido e caiu de uma altura que o matou.

  	2:22 Kill: 3 2 10: Isgalamido killed Dono da Bola by MOD_RAILGUN
  
  O player "Isgalamido" matou o player Dono da Bola usando a arma Railgun.
  
Para cada jogo o parser gera:

    game_1: {
	    total_kills: 45;
	    players: ["Dono da bola", "Isgalamido", "Zeh"]
	    kills: {
	      "Dono da bola": 5,
	      "Isgalamido": 18,
	      "Zeh": 20
	    }
	  }
	  
### Observações

1. Quando o `<world>` mata o player ele perde -1 kill.
2. `<world>` não é um player e não deve aparecer na lista de players e nem no dicionário de kills.
3. `total_kills` são os kills dos games, isso inclui mortes do `<world>`.


## Task 2


## Task 3


## Pré-requisito

Certifique-se de ter Python3 (>=3.6) para executar este aplicativo.

