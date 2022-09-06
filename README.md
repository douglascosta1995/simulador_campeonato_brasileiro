# simulador_campeonato_brasileiro


Este simulador foi desenvolvido para quem gosta de simular pontuações de partidas e ver como elas afetam a posição dos times em um campeonato. 
Neste jogo, o usuário pode selecionar 20 times da série A ou série B do campeonato brasileiro.

O campeonato é composto por 20 times, e eles se enfrentarão duas vezes (em casa e fora), resultando em 38 rodadas. 

Os placares em cada rodada serão gerados aleatoriamente e não será possível gerar outros placares na rodada atual.

Após a primeira rodada, a informação das pontuações será armazenada onde:
    VITÓRIA = 3 pontos à equipe vencedora, EMPATE = 1 ponto às duas equipes e uma DERROTA não dá nenhum ponto. 
    
Com essas informações, será gerada uma tabela de classificação. 

A ordem das equipes na tabela de classificação seguirá a prioridade de: 
    1 - Mais pontos / 2 - Mais vitórias / 3 - Mais saldo de gols / 4 - Mais gols feitos. 

Em caso de times com todos os critérios mencionados iguais, o critério de desempate será por ordem alfabética. 

Após cada rodada, a tabela de classificação mudará de acordo com as pontuações, e o usuário poderá consultá-la após cada rodada simulada. 

O time que terminar em 1º lugar na tabela de classificação após as 38 rodadas é o vencedor.

# Testes
Com o código desenvolvido, testes unitários e testes de sistema estão sendo criados com a finalidade de garantir a qualidade do código desenvolvido e verificar se atende aos requisitos.
