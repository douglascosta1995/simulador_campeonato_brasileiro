from unittest import TestCase
from times import Time
from unittest.mock import patch, call
import campeonato


class TimesTest(TestCase):

    def test_imprimir_time(self):
        lista_de_times_test = ['Vasco', 'Flamengo', 'São Paulo', 'Fluminense', 'Corinthians']
        with patch('builtins.print') as mocked_print:
            Time(lista_de_times_test).imprimir_time()
            self.assertEqual(mocked_print.mock_calls, [call(lista_de_times_test[0]),
                                                       call(lista_de_times_test[1]),
                                                       call(lista_de_times_test[2]),
                                                       call(lista_de_times_test[3]),
                                                       call(lista_de_times_test[4])])

    def test_criar_dictionary_de_times(self):
        lista_de_times_teste = ['Vasco', 'Flamengo', 'São Paulo']
        times_e_informacoes_teste = {'Vasco': {'pontos': 0, 'jogos': 0, 'vitorias': 0, 'empates': 0, 'derrotas': 0,
                                               'gols_pro': 0, 'gols_contra': 0, 'saldo_de_gols': 0},
                                     'Flamengo': {'pontos': 0, 'jogos': 0, 'vitorias': 0, 'empates': 0, 'derrotas': 0,
                                                  'gols_pro': 0, 'gols_contra': 0, 'saldo_de_gols': 0},
                                     'São Paulo': {'pontos': 0, 'jogos': 0, 'vitorias': 0, 'empates': 0, 'derrotas': 0,
                                                   'gols_pro': 0, 'gols_contra': 0, 'saldo_de_gols': 0}}

        with patch('builtins.input') as mocked_input:
            with patch('campeonato.Campeonato') as mocked_rodadas:
                mocked_input.side_effect = (' ')
                Time(lista_de_times_teste).criar_dictionary_de_times()
                mocked_rodadas.assert_called_with(times_e_informacoes_teste)
