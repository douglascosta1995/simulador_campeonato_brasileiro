
class Tabela(object):
    def __init__(self, info_times):
        self.info_times = info_times

    def imprimir_tabela(self, rodada):
        # teste código para ordenar times por maior pontuação e outro critérios
        sorted_time = sorted(self.info_times,
                          key=lambda x: (self.info_times[x]['pontos'], self.info_times[x]['vitorias'],
                                         self.info_times[x]['saldo_de_gols'], self.info_times[x]['gols_pro']),
                          reverse=True)
        print("TABELA DE CLASSIFICAÇÃO")
        # Formatar tabela depois
        print('%-20s%-5s%-5s%-5s%-5s%-5s%-5s%-5s%-5s' % ('Time', 'P', 'J', 'V', 'E', 'D', 'GP', 'GC', 'SG'))

        for time in sorted_time:
            print('%-20s%-5s%-5s%-5s%-5s%-5s%-5s%-5s%-5s' % (time, self.info_times[time]['pontos'],
                                     self.info_times[time]['jogos'],
                                     self.info_times[time]['vitorias'],
                                     self.info_times[time]['empates'],
                                     self.info_times[time]['derrotas'],
                                     self.info_times[time]['gols_pro'],
                                     self.info_times[time]['gols_contra'],
                                     self.info_times[time]['saldo_de_gols']))

        if int(rodada) == 37:
            print(f'O grande campeão do Campeonato Brasileiro é {sorted_time[0]}')
