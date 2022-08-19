import random

class Simulador_de_Partidas(object):
    def __init__(self, timeA, timeB):
        self.timeA = timeA
        self.timeB = timeB

    def simular(self):
        random_number1 = random.randint(0, 4)
        random_number2 = random.randint(0, 4)
        # imprimindo a partida com os placares gerados
        print(f'{self.timeA} {random_number1} x {random_number2} {self.timeB }')

        # dependendo do resultado da partida, será retornado quantos pontos cada equipe ganhou
        if random_number1 > random_number2:
            pontos_time_A = 3
            pontos_time_B = 0

        elif random_number1 == random_number2:
            pontos_time_A = 1
            pontos_time_B = 1

        else:
            pontos_time_A = 0
            pontos_time_B = 3

        return pontos_time_A, pontos_time_B

'''
if __name__ == "__main__":
    simular = Simulador_de_Partidas("Vasco", "Flamengo")
    simular.simular()
'''

