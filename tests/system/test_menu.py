from unittest import TestCase
from unittest.mock import patch, call
import menu

MENSAGEM_INICIAL = 'Seja bem vindo ao Campeonato'
MENSAGEM_RESPOSTA_INVALIDA = 'Resposta inválida. Tente novamente'
MENSAGEM_RESPOSTA_INVALIDA_NAO_NUMERICA = 'Somente números são aceitos. Tente novamente'
MENSAGEM_ENCERRANDO_SIMULADOR = 'Até logo!! :)'

class MenuTest(TestCase):
    def test_menu_inicial_resposta_numerica_invalida(self):
        """
        Este caso de teste tem como finalidade checar que quando o simulador é iniciado, o menu inicial será
        chamado e caso o usuário forneça inputs numéricos diferentes dos esperados, uma mensagem de error
        será exibida ao usuário.
        Para fins de teste, Logo após é fornecido ao menu a informação de encerrar o programa.
        """
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = (5, 5, 0)
                menu.Menu.menu_inicial(0)
                self.assertEqual(mocked_print.call_count, 3)
                self.assertEqual(mocked_print.mock_calls, [call(MENSAGEM_INICIAL),
                                                           call(MENSAGEM_RESPOSTA_INVALIDA),
                                                           call(MENSAGEM_ENCERRANDO_SIMULADOR)])

    def test_menu_inicial_resposta_nao_numerica(self):
        """
        Este caso de teste tem como finalidade checar que quando o simulador é iniciado, o menu inicial será
        chamado e caso o usuário forneça inputs não numéricos, uma mensagem de error será exibida ao usuário.
        Para fins de teste, Logo após é fornecido ao menu a informação de encerrar o programa.
        """
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = ('A', ' ', 0)
                menu.Menu.menu_inicial(0)
                self.assertEqual(mocked_print.call_count, 4)
                self.assertEqual(mocked_print.mock_calls, [call(MENSAGEM_INICIAL),
                                                           call(MENSAGEM_RESPOSTA_INVALIDA_NAO_NUMERICA),
                                                           call(MENSAGEM_RESPOSTA_INVALIDA_NAO_NUMERICA),
                                                           call(MENSAGEM_ENCERRANDO_SIMULADOR)])

    def test_menu_inicial_resposta_correta(self):
        """
        Este caso de test tem como finalidade checar que quando o simulador é iniciado, o menu inicial será
        chamado e caso o usuário forneça inputs numéricos corretos, conforme esperado, o simulador iniciará
        corretamente.
        """
        with patch('builtins.input') as mocked_input:
            with patch('builtins.print') as mocked_print:
                mocked_input.side_effect = (f'{i+1}' for i in range(0, 41))
                menu.Menu.menu_inicial(0)
                # seria interessante checar que o simulador finaliza com a mensagem exibindo o campeao
                self.assertTrue(mocked_print.call_count, 1257)

