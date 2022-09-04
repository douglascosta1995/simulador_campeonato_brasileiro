from unittest import TestCase
from simulador_de_partida import Simulador_de_Partidas
from unittest.mock import patch

class SimuladorDePartidasTest(TestCase):
    def test_simular_vitoria_timeA(self):
        return_esperado_da_funcao = [3, 1, 0, 0, 3, 0, 3, 0, 0, 0, 1, 0, 3, -3]
        with patch('random.randint') as mocked_random:
            with patch('builtins.print') as mocked_print:
                mocked_random.side_effect = (3, 0)
                resultado = Simulador_de_Partidas('Vasco', 'Flamengo').simular()
                lista_resultado = list(resultado)
                mocked_print.assert_called_with('Vasco 3 x 0 Flamengo')
                self.assertListEqual(lista_resultado, return_esperado_da_funcao)

    def test_simular_vitoria_timeB(self):
        return_esperado_da_funcao = [0, 0, 0, 1, 1, 2, -1, 3, 1, 0, 0, 2, 1, 1]
        with patch('random.randint') as mocked_random:
            with patch('builtins.print') as mocked_print:
                mocked_random.side_effect = (1, 2)
                resultado = Simulador_de_Partidas('Fluminense', 'Santos').simular()
                lista_resultado = list(resultado)
                mocked_print.assert_called_with('Fluminense 1 x 2 Santos')
                self.assertListEqual(lista_resultado, return_esperado_da_funcao)

    def test_simular_empate(self):
        return_esperado_da_funcao = [1, 0, 1, 0, 2, 2, 0, 1, 0, 1, 0, 2, 2, 0]
        with patch('random.randint') as mocked_random:
            with patch('builtins.print') as mocked_print:
                mocked_random.side_effect = (2, 2)
                resultado = Simulador_de_Partidas('Palmeiras', 'Internacional').simular()
                lista_resultado = list(resultado)
                mocked_print.assert_called_with('Palmeiras 2 x 2 Internacional')
                self.assertListEqual(lista_resultado, return_esperado_da_funcao)
