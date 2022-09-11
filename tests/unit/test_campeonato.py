from unittest import TestCase
from campeonato import Campeonato


class CampeonatoTest(TestCase):

    def test_campeonato_informacao_dos_times(self):
        """
        Este caso de teste tem como finalidade checar que quando a função informação_dos_times é chamada
        com os parâmetros de informações após simulação das partidas, estes valores são adicionados aos
        valores que já estavam guardados anteriormente no dicionário de informações dos times.
        Neste caso específico, somente para fins de checar que o resultado é adicionado, todos os parâmetros
        foram adicionados valor 1.
        """
        info_times_test = {'Vasco': {'pontos': 15, 'jogos': 7, 'vitorias': 5, 'empates': 0, 'derrotas': 2,
                                     'gols_pro': 12, 'gols_contra': 5, 'saldo_de_gols': 7},
                           'Bahia': {'pontos': 15, 'jogos': 7, 'vitorias': 4, 'empates': 3, 'derrotas': 0,
                                     'gols_pro': 14, 'gols_contra': 3, 'saldo_de_gols': 11},
                           'Grêmio': {'pontos': 16, 'jogos': 7, 'vitorias': 5, 'empates': 1, 'derrotas': 1,
                                      'gols_pro': 14, 'gols_contra': 1, 'saldo_de_gols': 13},
                           'Cruzeiro': {'pontos': 16, 'jogos': 7, 'vitorias': 5, 'empates': 1, 'derrotas': 1,
                                        'gols_pro': 15, 'gols_contra': 1, 'saldo_de_gols': 14},
                           'Sport': {'pontos': 15, 'jogos': 7, 'vitorias': 5, 'empates': 0, 'derrotas': 2,
                                     'gols_pro': 14, 'gols_contra': 7, 'saldo_de_gols': 7}
                           }

        info_times_test_esperado = {'Vasco': {'pontos': 16, 'jogos': 8, 'vitorias': 6, 'empates': 1, 'derrotas': 3,
                                              'gols_pro': 13, 'gols_contra': 6, 'saldo_de_gols': 8},
                                    'Bahia': {'pontos': 16, 'jogos': 8, 'vitorias': 5, 'empates': 4, 'derrotas': 1,
                                              'gols_pro': 15, 'gols_contra': 4, 'saldo_de_gols': 12},
                                    'Grêmio': {'pontos': 17, 'jogos': 8, 'vitorias': 6, 'empates': 2, 'derrotas': 2,
                                               'gols_pro': 15, 'gols_contra': 2, 'saldo_de_gols': 14},
                                    'Cruzeiro': {'pontos': 17, 'jogos': 8, 'vitorias': 6, 'empates': 2, 'derrotas': 2,
                                                 'gols_pro': 16, 'gols_contra': 2, 'saldo_de_gols': 15},
                                    'Sport': {'pontos': 16, 'jogos': 8, 'vitorias': 6, 'empates': 1, 'derrotas': 3,
                                              'gols_pro': 15, 'gols_contra': 8, 'saldo_de_gols': 8}
                                    }

        test_campeonato = Campeonato(info_times_test)
        for time in info_times_test:
            test_campeonato.informacao_dos_times(time, 1, 1, 1, 1, 1, 1, 1)

        self.assertDictEqual(info_times_test, info_times_test_esperado)

    def test_gerador_de_partidas_proxima_rodada(self):
        pass

    def test_criar_tabela_de_classificacao(self):
        pass

    def test_rodadas(self):
        pass
