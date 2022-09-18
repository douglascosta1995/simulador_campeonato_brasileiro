from unittest import TestCase
from campeonato import Campeonato, relacao_de_times_e_rodadas
from unittest.mock import patch
from times_database import times


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

    def test_gerador_de_partidas_proxima_rodada_primeira(self):
        """
        Este caso de teste tem como finalidade checar que quando a função gerador_de_partidas_proxima_rodada
        é chamada na primeira rodada o python dictionary criado com as informações iniciais sobre a relação
        de times e partidas não é alterado.
        """
        relacao_de_times_e_rodadas_test = relacao_de_times_e_rodadas
        Campeonato({}).gerador_de_partidas_da_proxima_rodada(0)

        self.assertDictEqual(relacao_de_times_e_rodadas_test, relacao_de_times_e_rodadas)

    def test_gerador_de_partidas_proxima_rodada_val0_equals_1(self):
        """
        Este caso de teste tem como finalidade checar que quando a função gerador_de_partidas_proxima_rodada
        é chamada em outra rodada que nao seja a primeira, o python dictionary criado com as informações iniciais
        sobre a relação de times e partidas é alterado, onde que se um dos valores é 1 este será substituído por
        19 e os outros valores diferentes de 1, serão subtraídos por 1. Desta forma, [1, 18] é atualizado para
        [19, 17].
        """
        relacao_de_times_e_rodadas_esperado = {
            '1': [0, 18],
            '2': [19, 17],
            '3': [1, 16],
            '4': [2, 15],
            '5': [3, 14],
            '6': [4, 13],
            '7': [5, 12],
            '8': [6, 11],
            '9': [7, 10],
            '10': [8, 9]
        }
        Campeonato({}).gerador_de_partidas_da_proxima_rodada(1)

        self.assertDictEqual(relacao_de_times_e_rodadas_esperado, relacao_de_times_e_rodadas)

    def test_gerador_de_partidas_proxima_rodada_val1_equals_1(self):
        """
        Este caso de teste tem como finalidade checar que quando a função gerador_de_partidas_proxima_rodada
        é chamada após 10 rodadas o value de index 1 será igual a 1 e assim o python dictionary será também
        modificado onde este valor será substituído por 19, enquanto os outros serão subtraídos por 1.
        Desta forma, [19, 1] é atualizado para [18, 19].
        """
        relacao_de_times_e_rodadas_esperado = {
            '1': [0, 9],
            '2': [10, 8],
            '3': [11, 7],
            '4': [12, 6],
            '5': [13, 5],
            '6': [14, 4],
            '7': [15, 3],
            '8': [16, 2],
            '9': [17, 1],
            '10': [18, 19]
        }
        for i in range(0, 11):
            Campeonato({}).gerador_de_partidas_da_proxima_rodada(i)

        self.assertDictEqual(relacao_de_times_e_rodadas_esperado, relacao_de_times_e_rodadas)

    def test_criar_tabela_de_classificacao(self):
        """
        Este caso de teste tem como finalidade checar que quando a função criar_tabela_de_classificacao é chamada,
        a função imprimir_tabela da classe Tabela será chamada com a informação de qual rodade é atualmente.
        """
        with patch('tabela.Tabela.imprimir_tabela') as mocked_imprimir_tabela:
            Campeonato({}).criar_tabela_de_classificacao(5)
            mocked_imprimir_tabela.assert_called_with(5)

    def test_rodadas(self):
        """
        Este caso de teste tem como finalidade checar a quantidade de vezes que funções externas são chamadas durante
        as 38 rodadas. Considerando uma lista de 20 times, é esperado que a função geradora das partidas seja chamada
        uma vez por rodada; a função simuladora de partida seja chamada 10 vezes por rodada (são 10 partidas a serem
        simuladas); a função de atualização de informação dos times seja chamada 20 vezes por rodada (são 20 times a
        terem suas informações atualizadas); e a função geradora da tabela de classificação seja chamada 1 vez por
        rodada.
        """
        lista_de_times = list(times)

        with patch('builtins.print') as mocked_print:
            with patch('builtins.input', side_effect=[f'{i}' for i in range(0, 38)]):
                with patch('campeonato.Campeonato.gerador_de_partidas_da_proxima_rodada') as mocked_gerador_partidas:
                    with patch('simulador_de_partida.Simulador_de_Partidas.simular') as mocked_simulador:
                        with patch('campeonato.Campeonato.informacao_dos_times') as mocked_info:
                            with patch('campeonato.Campeonato.criar_tabela_de_classificacao') as mocked_tabela:
                                Campeonato(lista_de_times).rodadas()
                                self.assertEqual(mocked_print.call_count, 38)
                                self.assertEqual(mocked_gerador_partidas.call_count, 38)
                                self.assertEqual(mocked_simulador.call_count, 380)
                                self.assertEqual(mocked_info.call_count, 760)
                                self.assertEqual(mocked_tabela.call_count, 38)

