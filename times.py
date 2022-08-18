# Talvez seja melhor transformar isso em um json file
# Aqui deve conter as informacões necessárias de cada time selecionado para o campeonato
# Estas informações devem ser o suficiente para montar a tabela de classificação

class Time(object):
    def __init__(self, lista_de_times):
        self.lista_de_times = lista_de_times
        self.pontos = 0
        self.jogos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_pro = 0
        self.gols_contra = 0
        self.saldo_de_gols = 0


    def imprimir_time(self):
        for time in self.lista_de_times:
            print(time)

    def criar_dictionary_de_times(self):
        times_e_informacoes = {}
        for time in self.lista_de_times:
            times_e_informacoes[time] = {
                    'pontos': self.pontos,
                    'jogos': self.jogos,
                    'vitorias': self.vitorias,
                    'empates': self.empates,
                    'derrotas': self.derrotas,
                    'gols_pro': self.gols_pro,
                    'gols_contra': self.gols_contra,
                    'saldo_de_gols': self.saldo_de_gols
                }

        print(times_e_informacoes)
'''
if __name__ == "__main__":

    jogo = Time([])
    jogo.criar_dictionary_de_times()
'''
