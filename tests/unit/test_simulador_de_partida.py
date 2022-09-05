from unittest import TestCase
from simulador_de_partida import Simulador_de_Partidas
from unittest.mock import patch


class SimuladorDePartidasTest(TestCase):

    def test_simular_vitoria_timeA(self):
        """
        Este caso de teste tem como finalidade checar que quando o timeA vence o timeB, as informações
        relevantes sobre ambos os times são retornadas. Estas informações são retornadas em sequência.
        Desta forma, o retorno é checado sob a forma de uma lista e comparada com a lista esperada no caso
        de vitória do timeA.

        Sequência:
        [pontosTimeA, vitoriaTimeA, empateTimeA, derrotaTimeA, golsProTimeA, golsContraTimeA, saldoGolsTimeA,
         pontosTimeB, vitoriaTimeB, empateTimeB, derrotaTimeB, golsProTimeB, golsContraTimeB, saldoGolsTimeB]
        """
        return_esperado_da_funcao = [3, 1, 0, 0, 3, 0, 3, 0, 0, 0, 1, 0, 3, -3]
        with patch('random.randint') as mocked_random:
            with patch('builtins.print') as mocked_print:
                mocked_random.side_effect = (3, 0)
                resultado = Simulador_de_Partidas('Vasco', 'Flamengo').simular()
                lista_resultado = list(resultado)
                mocked_print.assert_called_with('Vasco 3 x 0 Flamengo')
                self.assertListEqual(lista_resultado, return_esperado_da_funcao)

    def test_simular_vitoria_timeB(self):
        """
        Este caso de teste tem como finalidade checar que quando o timeB vence o timeA, as informações
        relevantes sobre ambos os times são retornadas. Estas informações são retornadas em sequência.
        Desta forma, o retorno é checado sob a forma de uma lista e comparada com a lista esperada no caso
        de vitória do timeB.

        Sequência:
        [pontosTimeA, vitoriaTimeA, empateTimeA, derrotaTimeA, golsProTimeA, golsContraTimeA, saldoGolsTimeA,
         pontosTimeB, vitoriaTimeB, empateTimeB, derrotaTimeB, golsProTimeB, golsContraTimeB, saldoGolsTimeB]
        """
        return_esperado_da_funcao = [0, 0, 0, 1, 1, 2, -1, 3, 1, 0, 0, 2, 1, 1]
        with patch('random.randint') as mocked_random:
            with patch('builtins.print') as mocked_print:
                mocked_random.side_effect = (1, 2)
                resultado = Simulador_de_Partidas('Fluminense', 'Santos').simular()
                lista_resultado = list(resultado)
                mocked_print.assert_called_with('Fluminense 1 x 2 Santos')
                self.assertListEqual(lista_resultado, return_esperado_da_funcao)

    def test_simular_empate(self):
        """
        Este caso de teste tem como finalidade checar que quando o timeA empata com o timeB, as informações
        relevantes sobre ambos os times são retornadas. Estas informações são retornadas em sequência.
        Desta forma, o retorno é checado sob a forma de uma lista e comparada com a lista esperada no caso
        de empate.

        Sequência:
        [pontosTimeA, vitoriaTimeA, empateTimeA, derrotaTimeA, golsProTimeA, golsContraTimeA, saldoGolsTimeA,
         pontosTimeB, vitoriaTimeB, empateTimeB, derrotaTimeB, golsProTimeB, golsContraTimeB, saldoGolsTimeB]
        """
        return_esperado_da_funcao = [1, 0, 1, 0, 2, 2, 0, 1, 0, 1, 0, 2, 2, 0]
        with patch('random.randint') as mocked_random:
            with patch('builtins.print') as mocked_print:
                mocked_random.side_effect = (2, 2)
                resultado = Simulador_de_Partidas('Palmeiras', 'Internacional').simular()
                lista_resultado = list(resultado)
                mocked_print.assert_called_with('Palmeiras 2 x 2 Internacional')
                self.assertListEqual(lista_resultado, return_esperado_da_funcao)

    def test_timeA_mais_forte(self):
        """
        Este caso de teste tem como finalidade checar que quando o timeA é mais forte que o timeB,
        será adionada uma leve vantagem após o número aleatório escolhido. Por exemplo, se após as duas chamadas
        de número aleatórios para o placar o resultado seria 1 x 1, como o timeA é mais forte, será adicionado
        mais 1, o que irá gerar o resultado final 2 x 1.
        """
        with patch('random.randint') as mocked_random:
            with patch('times_database.times') as mocked_times:
                with patch('builtins.print') as mocked_print:
                    mocked_random.side_effect = (1, 1)
                    mocked_times.return_value = {'América Mineiro': [1, 2],
                                                 'Atlético-PR': [1, 4],
                                                 'Atlético-GO': [1, 3],
                                                 'Atlético-MG': [1, 4]}

                    Simulador_de_Partidas('Atlético-MG', 'América Mineiro').simular()
                    mocked_print.assert_called_with('Atlético-MG 2 x 1 América Mineiro')

    def test_timeB_mais_forte(self):
        """
        Este caso de teste tem como finalidade checar que quando o timeB é mais forte que o timeA,
        será adionada uma leve vantagem após o número aleatório escolhido. Por exemplo, se após as duas chamadas
        de número aleatórios para o placar o resultado seria 2 x 2, como o timeB é mais forte, será adicionado
        mais 1, o que irá gerar o resultado final 2 x 3.
        """
        with patch('random.randint') as mocked_random:
            with patch('times_database.times') as mocked_times:
                with patch('builtins.print') as mocked_print:
                    mocked_random.side_effect = (2, 2)
                    mocked_times.return_value = {'América Mineiro': [1, 2],
                                                 'Atlético-PR': [1, 4],
                                                 'Atlético-GO': [1, 3],
                                                 'Atlético-MG': [1, 4]}

                    Simulador_de_Partidas('Atlético-GO', 'Atlético-PR').simular()
                    mocked_print.assert_called_with('Atlético-GO 2 x 3 Atlético-PR')

    def test_igualmente_fortes(self):
        """
        Este caso de teste tem como finalidade checar que quando ambos os times possuem mesmo índice
        de força, o valor gerado pela função de número aleatório será mantido como placar final.
        """
        with patch('random.randint') as mocked_random:
            with patch('times_database.times') as mocked_times:
                with patch('builtins.print') as mocked_print:
                    mocked_random.side_effect = (2, 2)
                    mocked_times.return_value = {'América Mineiro': [1, 2],
                                                 'Atlético-PR': [1, 4],
                                                 'Atlético-GO': [1, 3],
                                                 'Atlético-MG': [1, 4]}

                    Simulador_de_Partidas('Atlético-MG', 'Atlético-PR').simular()
                    mocked_print.assert_called_with('Atlético-MG 2 x 2 Atlético-PR')

