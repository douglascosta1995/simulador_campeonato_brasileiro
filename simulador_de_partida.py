from times_database import times
import random


class Simulador_de_Partidas(object):
    def __init__(self, timeA, timeB):
        self.timeA = timeA
        self.timeB = timeB
        self.forca_timeA = times[timeA][1]
        self.forca_timeB = times[timeB][1]

    def simular(self):
        random_number1 = (random.randint(0, 3) + 1) if self.forca_timeA > self.forca_timeB else random.randint(0, 4)
        random_number2 = (random.randint(0, 3) + 1) if self.forca_timeB > self.forca_timeA else random.randint(0, 4)
        # imprimindo a partida com os placares gerados
        print(f'{self.timeA} {random_number1} x {random_number2} {self.timeB}')

        # dependendo do resultado da partida, será retornado quantos pontos cada equipe ganhou
        if random_number1 > random_number2:
            # talvez seria melhor criar um dictionary para salvar esses valores
            pontos_time_A = 3
            vitorias_time_A = 1
            empates_time_A = 0
            derrotas_time_A = 0
            gols_pro_time_A = random_number1
            gols_contra_time_A = random_number2
            saldo_de_gols_time_A = gols_pro_time_A - gols_contra_time_A
            pontos_time_B = 0
            vitorias_time_B = 0
            empates_time_B = 0
            derrotas_time_B = 1
            gols_pro_time_B = random_number2
            gols_contra_time_B = random_number1
            saldo_de_gols_time_B = gols_pro_time_B - gols_contra_time_B

        elif random_number1 == random_number2:
            pontos_time_A = 1
            vitorias_time_A = 0
            empates_time_A = 1
            derrotas_time_A = 0
            gols_pro_time_A = random_number1
            gols_contra_time_A = random_number2
            saldo_de_gols_time_A = gols_pro_time_A - gols_contra_time_A
            pontos_time_B = 1
            vitorias_time_B = 0
            empates_time_B = 1
            derrotas_time_B = 0
            gols_pro_time_B = random_number2
            gols_contra_time_B = random_number1
            saldo_de_gols_time_B = gols_pro_time_B - gols_contra_time_B

        else:
            pontos_time_A = 0
            vitorias_time_A = 0
            empates_time_A = 0
            derrotas_time_A = 1
            gols_pro_time_A = random_number1
            gols_contra_time_A = random_number2
            saldo_de_gols_time_A = gols_pro_time_A - gols_contra_time_A
            pontos_time_B = 3
            vitorias_time_B = 1
            empates_time_B = 0
            derrotas_time_B = 0
            gols_pro_time_B = random_number2
            gols_contra_time_B = random_number1
            saldo_de_gols_time_B = gols_pro_time_B - gols_contra_time_B

        return pontos_time_A, vitorias_time_A, empates_time_A, derrotas_time_A, \
               gols_pro_time_A, gols_contra_time_A, saldo_de_gols_time_A, pontos_time_B, \
               vitorias_time_B, empates_time_B, derrotas_time_B, gols_pro_time_B, gols_contra_time_B, \
               saldo_de_gols_time_B

