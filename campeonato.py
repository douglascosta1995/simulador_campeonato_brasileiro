# Este arquivo será onde o campeonato será simulado de fato.
# A cada rodada o simulador_de_partida.py será executado
# Antes da simulacao, cada time será consultado no banco de dados para saber quem é mais forte
# A cada rodada o times serão atualizados com as informações adquiridas após a rodada
# Ao fim de cada rodada, será mostrada a tabela de classificação
from simulador_de_partida import Simulador_de_Partidas
from tabela import Tabela

# criar um dictionary com as informaçoes das rodadas de cada time
# 1 x 20; 19 x 1 ....
relacao_de_times_e_rodadas = {
    '1': [0, 19],
    '2': [1, 18],
    '3': [2, 17],
    '4': [3, 16],
    '5': [4, 15],
    '6': [5, 14],
    '7': [6, 13],
    '8': [7, 12],
    '9': [8, 11],
    '10': [9, 10]
}


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
        key_list = list(self.info_times)
        for i in range(0, 38):
            print(f'rodada: {i + 1}')
            # garantir que os times joguem dentro e fora de casa
            if i % 2 == 0:
                # timeA x timeB
                Campeonato.gerador_de_partidas_da_proxima_rodada(self, i)
                # iterar sobre todos os valores do dictionary e simular as partidas da rodada atual
                # [0, 19] significa time0 x time19
                for value in relacao_de_times_e_rodadas.values():
                    resultado = Simulador_de_Partidas(key_list[value[0]], key_list[value[1]]).simular()
                    Campeonato.informacao_dos_times(self, key_list[value[0]], resultado[0], resultado[1], resultado[2], resultado[3],
                                            resultado[4],
                                            resultado[5], resultado[6])
                    Campeonato.informacao_dos_times(self, key_list[value[1]], resultado[7], resultado[8], resultado[9], resultado[10],
                                            resultado[11],
                                            resultado[12], resultado[13])

            else:
                # timeB x timeA
                Campeonato.gerador_de_partidas_da_proxima_rodada(self, i)
                for value in relacao_de_times_e_rodadas.values():
                    resultado = Simulador_de_Partidas(key_list[value[1]], key_list[value[0]]).simular()
                    Campeonato.informacao_dos_times(self, key_list[value[1]], resultado[0], resultado[1], resultado[2],
                                                    resultado[3],
                                                    resultado[4],
                                                    resultado[5], resultado[6])
                    Campeonato.informacao_dos_times(self, key_list[value[0]], resultado[7], resultado[8], resultado[9],
                                                    resultado[10],
                                                    resultado[11],
                                                    resultado[12], resultado[13])
        # criar tabela de classificação
        Campeonato.criar_tabela_de_classificacao(self)

    def gerador_de_partidas_da_proxima_rodada(self, rodada):
        # se for primeira rodada, manter como esta:
        if int(rodada) == 0:
            pass
        else:
            # diminuir val[0] e val[1] por 1
            # checar se tem valor igual a zero e substituir por 19 (atualizar dictionary)
            for key, val in relacao_de_times_e_rodadas.items():
                if key == '1':
                    val[1] -= 1
                else:
                    if val[0] == 1:
                        val[0] = 19
                        val[1] -= 1
                    elif val[1] == 1:
                        val[1] = 19
                        val[0] -= 1
                    else:
                        val[0] -= 1
                        val[1] -= 1

    def criar_tabela_de_classificacao(self):
        Tabela(self.info_times).imprimir_tabela()
