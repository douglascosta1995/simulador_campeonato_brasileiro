# Este arquivo será onde o campeonato será simulado de fato.
# A cada rodada o simulador_de_partida.py será executado
# Antes da simulacao, cada time será consultado no banco de dados para saber quem é mais forte
# A cada rodada o times serão atualizados com as informações adquiridas após a rodada
# Ao fim de cada rodada, será mostrada a tabela de classificação
from simulador_de_partida import Simulador_de_Partidas

class Campeonato(object):
    def __init__(self, info_times_inicial):
        self.info_times_inicial = info_times_inicial
        pass

    def informacao_dos_times(self, time, pontos, vitorias, empates, derrotas, gp, gc, sg):
        self.info_times_inicial[time]['pontos'] += pontos
        self.info_times_inicial[time]['vitorias'] += vitorias
        self.info_times_inicial[time]['empates'] += empates
        self.info_times_inicial[time]['derrotas'] += derrotas
        self.info_times_inicial[time]['gols_pro'] += gp
        self.info_times_inicial[time]['gols_contra'] += gc
        self.info_times_inicial[time]['saldo_de_gols'] += sg

        #print(self.info_times_inicial)

    def rodadas(self):
        key = list(self.info_times_inicial)
        resultado = Simulador_de_Partidas(key[0], key[1]).simular()
        Campeonato.informacao_dos_times(self, key[0], resultado[0], resultado[1], resultado[2], resultado[3], resultado[4],
                                        resultado[5], resultado[6])
        Campeonato.informacao_dos_times(self, key[1], resultado[7], resultado[8], resultado[9], resultado[10], resultado[11],
                                        resultado[12], resultado[13])

        print(self.info_times_inicial)

        '''
        for i in range(0, 10):
            name = key[i]
            resultado = Simulador_de_Partidas(key[i], key[i+1]).simular()
            #print (f'Vasco ganhou {resultado[0]} e Flamengo ganhou {resultado[1]}')
            #resultado = Simulador_de_Partidas("Fluminense", "Santos").simular()
            #print (f'Fluminense ganhou {resultado[0]} e Santos ganhou {resultado[1]}')
            print(list(resultado))
            #Campeonato.informacao_dos_times(name, resultado)
        '''

    def criar_tabela_de_classificacao(self):
        pass