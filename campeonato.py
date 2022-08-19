# Este arquivo será onde o campeonato será simulado de fato.
# A cada rodada o simulador_de_partida.py será executado
# Antes da simulacao, cada time será consultado no banco de dados para saber quem é mais forte
# A cada rodada o times serão atualizados com as informações adquiridas após a rodada
# Ao fim de cada rodada, será mostrada a tabela de classificação
class Campeonato(object):
    def __init__(self, info_times_inicial):
        self.info_times_inicial = info_times_inicial
        pass

    def informacao_dos_times(self):
        # self.info_times_inicial['América Mineiro']['pontos'] += 1

        print(self.info_times_inicial)

    def rodadas(self):
        pass

    def criar_tabela_de_classificacao(self):
        pass