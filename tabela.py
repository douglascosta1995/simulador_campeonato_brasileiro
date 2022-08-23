
class Tabela(object):
    def __init__(self, info_times):
        self.info_times = info_times

    def imprimir_tabela(self):
        # teste código para ordenar times por maior pontuação e outro critérios
        sorted_time = sorted(self.info_times,
                          key=lambda x: (self.info_times[x]['pontos'], self.info_times[x]['vitorias'],
                                         self.info_times[x]['saldo_de_gols'], self.info_times[x]['gols_pro']),
                          reverse=True)
        print(sorted_time)
        print("TABELA DE CLASSIFICAÇÃO")
        # Formatar tabela depois
        print("Time     P   J   V   E   D   GP    GC    SG ")
        for time in sorted_time:
            print(f"{time} :    {self.info_times[time]['pontos']}   "
                  f"{self.info_times[time]['jogos']}   "
                  f"{self.info_times[time]['vitorias']}   "
                  f"{self.info_times[time]['empates']}   "
                  f"{self.info_times[time]['derrotas']}   "
                  f"{self.info_times[time]['gols_pro']}   "
                  f"{self.info_times[time]['gols_contra']}   "
                  f"{self.info_times[time]['saldo_de_gols']}   ")