from unittest import TestCase
from tabela import Tabela
from unittest.mock import patch, call

ESPACAMENTO_IMPRESSAO_TABELA = '%-20s%-5s%-5s%-5s%-5s%-5s%-5s%-5s%-5s'


class TabelaTest(TestCase):
    def test_imprimir_tabela(self):
        """
        Este caso de teste tem como finalidade checar que quando a função imprimir_tabela recebe um python
        dictionary com times não ordenados, ela irá ordená-los seguindo a prioridade e critério de desempate de:
        1. Mais pontos / 2. Mais vitórias / 3. Mais saldo de gols / 4. Mais gols feitos.
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

        titulo_esperado = 'TABELA DE CLASSIFICAÇÃO'
        titulo_informacoes_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                      % ('Time', 'P', 'J', 'V', 'E', 'D', 'GP', 'GC', 'SG')
        primeiro_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                     % ('Cruzeiro', 16, 7, 5, 1, 1, 15, 1, 14)
        segundo_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                    % ('Grêmio', 16, 7, 5, 1, 1, 14, 1, 13)
        terceiro_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                     % ('Sport', 15, 7, 5, 0, 2, 14, 7, 7)
        quarto_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                   % ('Vasco', 15, 7, 5, 0, 2, 12, 5, 7)
        quinto_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                   % ('Bahia', 15, 7, 4, 3, 0, 14, 3, 11)

        with patch('builtins.print') as mocked_print:
            Tabela(info_times_test).imprimir_tabela(6)
            self.assertEqual(mocked_print.mock_calls, [call(titulo_esperado),
                                                       call(titulo_informacoes_esperado),
                                                       call(primeiro_colocado_esperado),
                                                       call(segundo_colocado_esperado),
                                                       call(terceiro_colocado_esperado),
                                                       call(quarto_colocado_esperado),
                                                       call(quinto_colocado_esperado)
                                                       ])

    def test_imprimir_tabela_times_empatados_nos_criterios_rodada(self):
        """
        Este caso de teste tem como finalidade checar que quando a função imprimir_tabela recebe um python
        dictionary com times não ordenados , e que estes possuem todos os critérios de desempates iguais,
        a ordem que os times estão no dictionary inicial será levada em consideração.
        """
        info_times_test = {'Bahia': {'pontos': 0, 'jogos': 1, 'vitorias': 0, 'empates': 0, 'derrotas': 1,
                                     'gols_pro': 1, 'gols_contra': 2, 'saldo_de_gols': -1},
                           'Cruzeiro': {'pontos': 0, 'jogos': 1, 'vitorias': 0, 'empates': 0, 'derrotas': 1,
                                     'gols_pro': 1, 'gols_contra': 2, 'saldo_de_gols': -1},
                           'Grêmio': {'pontos': 3, 'jogos': 1, 'vitorias': 1, 'empates': 0, 'derrotas': 0,
                                      'gols_pro': 2, 'gols_contra': 0, 'saldo_de_gols': 2},
                           'Sport': {'pontos': 3, 'jogos': 1, 'vitorias': 1, 'empates': 0, 'derrotas':0,
                                        'gols_pro': 2, 'gols_contra': 0, 'saldo_de_gols': 2},
                           'Vasco': {'pontos': 3, 'jogos': 1, 'vitorias': 1, 'empates': 0, 'derrotas': 0,
                                     'gols_pro': 2, 'gols_contra': 0, 'saldo_de_gols': 2}
                           }

        titulo_esperado = 'TABELA DE CLASSIFICAÇÃO'
        titulo_informacoes_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                      % ('Time', 'P', 'J', 'V', 'E', 'D', 'GP', 'GC', 'SG')
        primeiro_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                     % ('Grêmio', 3, 1, 1, 0, 0, 2, 0, 2)
        segundo_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                    % ('Sport', 3, 1, 1, 0, 0, 2, 0, 2)
        terceiro_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                     % ('Vasco', 3, 1, 1, 0, 0, 2, 0, 2)
        quarto_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                   % ('Bahia', 0, 1, 0, 0, 1, 1, 2, -1)
        quinto_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                   % ('Cruzeiro', 0, 1, 0, 0, 1, 1, 2, -1)

        with patch('builtins.print') as mocked_print:
            Tabela(info_times_test).imprimir_tabela(0)
            self.assertEqual(mocked_print.mock_calls, [call(titulo_esperado),
                                                       call(titulo_informacoes_esperado),
                                                       call(primeiro_colocado_esperado),
                                                       call(segundo_colocado_esperado),
                                                       call(terceiro_colocado_esperado),
                                                       call(quarto_colocado_esperado),
                                                       call(quinto_colocado_esperado)])


    def test_imprimir_tabela_ultima_rodada(self):
        """
        Este caso de teste tem como finalidade checar que quando é a última rodada, além de imprimir
        a tabela de classificação ordenada, a função imprimir_tabela também imprime uma mensagem com
        o nome do time campeão.
        """
        info_times_test = {'Flamengo': {'pontos': 72, 'jogos': 38, 'vitorias': 21, 'empates': 9, 'derrotas': 8,
                                     'gols_pro': 59, 'gols_contra': 29, 'saldo_de_gols': 30},
                           'Grêmio': {'pontos': 66, 'jogos': 38, 'vitorias': 18, 'empates': 12, 'derrotas': 8,
                                     'gols_pro': 48, 'gols_contra': 27, 'saldo_de_gols': 21},
                           'Internacional': {'pontos': 69, 'jogos': 38, 'vitorias': 19, 'empates': 12, 'derrotas': 7,
                                      'gols_pro': 51, 'gols_contra': 29, 'saldo_de_gols': 22},
                           'Palmeiras': {'pontos': 80, 'jogos': 38, 'vitorias': 23, 'empates': 11, 'derrotas': 4,
                                        'gols_pro': 64, 'gols_contra': 26, 'saldo_de_gols': 38},
                           'São Paulo': {'pontos': 63, 'jogos': 38, 'vitorias': 16, 'empates': 15, 'derrotas': 7,
                                     'gols_pro': 46, 'gols_contra': 34, 'saldo_de_gols': 12}
                           }

        titulo_esperado = 'TABELA DE CLASSIFICAÇÃO'
        titulo_informacoes_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                      % ('Time', 'P', 'J', 'V', 'E', 'D', 'GP', 'GC', 'SG')
        primeiro_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                     % ('Palmeiras', 80, 38, 23, 11, 4, 64, 26, 38)
        segundo_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                    % ('Flamengo', 72, 38, 21, 9, 8, 59, 29, 30)
        terceiro_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                     % ('Internacional', 69, 38, 19, 12, 7, 51, 29, 22)
        quarto_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                   % ('Grêmio', 66, 38, 18, 12, 8, 48, 27, 21)
        quinto_colocado_esperado = ESPACAMENTO_IMPRESSAO_TABELA \
                                   % ('São Paulo', 63, 38, 16, 15, 7, 46, 34, 12)

        mensagem_campeao_esperado = 'O grande campeão do Campeonato Brasileiro é Palmeiras'

        with patch('builtins.print') as mocked_print:
            Tabela(info_times_test).imprimir_tabela(37)
            self.assertEqual(mocked_print.mock_calls, [call(titulo_esperado),
                                                       call(titulo_informacoes_esperado),
                                                       call(primeiro_colocado_esperado),
                                                       call(segundo_colocado_esperado),
                                                       call(terceiro_colocado_esperado),
                                                       call(quarto_colocado_esperado),
                                                       call(quinto_colocado_esperado),
                                                       call(mensagem_campeao_esperado)])
