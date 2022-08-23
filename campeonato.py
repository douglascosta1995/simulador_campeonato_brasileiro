# Este arquivo será onde o campeonato será simulado de fato.
# A cada rodada o simulador_de_partida.py será executado
# Antes da simulacao, cada time será consultado no banco de dados para saber quem é mais forte
# A cada rodada o times serão atualizados com as informações adquiridas após a rodada
# Ao fim de cada rodada, será mostrada a tabela de classificação
from simulador_de_partida import Simulador_de_Partidas
from tabela import Tabela


class Campeonato(object):
    def __init__(self, info_times_inicial):
        self.info_times = info_times_inicial

    def informacao_dos_times(self, time, pontos, vitorias, empates, derrotas, gp, gc, sg):
        self.info_times[time]['pontos'] += pontos
        self.info_times[time]['jogos'] += 1
        self.info_times[time]['vitorias'] += vitorias
        self.info_times[time]['empates'] += empates
        self.info_times[time]['derrotas'] += derrotas
        self.info_times[time]['gols_pro'] += gp
        self.info_times[time]['gols_contra'] += gc
        self.info_times[time]['saldo_de_gols'] += sg

    def rodadas(self):
        key = list(self.info_times)
        # colocar in a loop pra simular as rodadas
        # Testar primeira rodada
        for i in range(0, 10):
            resultado = Simulador_de_Partidas(key[i], key[19-i]).simular()
            Campeonato.informacao_dos_times(self, key[i], resultado[0], resultado[1], resultado[2], resultado[3], resultado[4],
                                            resultado[5], resultado[6])
            Campeonato.informacao_dos_times(self, key[19-i], resultado[7], resultado[8], resultado[9], resultado[10], resultado[11],
                                            resultado[12], resultado[13])

        # criar tabela de classificação
        Campeonato.criar_tabela_de_classificacao(self)

    def criar_tabela_de_classificacao(self):
        Tabela(self.info_times).imprimir_tabela()
