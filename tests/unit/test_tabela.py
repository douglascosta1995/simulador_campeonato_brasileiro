from unittest import TestCase
from tabela import Tabela
from unittest.mock import patch, call

ESPACAMENTO_IMPRESSAO_TABELA = '%-20s%-5s%-5s%-5s%-5s%-5s%-5s%-5s%-5s'


class TabelaTest(TestCase):
    def test_imprimir_tabela(self):
        """
        Este caso de teste tem como finalidade checar que quando a função imprimir_tabela recebe um python
        dictionary com times não ordenados, ela irá ordená-los seguindo a prioridade e critério de desempate de:
        1. Mais pontos / 2. Mais vitórias / 3. Mais saldo de gols / 4. Mais gols feitos
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

    def test_imprimir_tabela_times_empatados_nos_criterios(self):
        pass

    def test_imprimir_tabela_ultima_rodada(self):
        pass
