from times_database import times
from times import Time

class Menu(object):
    def __init__(self, serie_campeonato):
        self.serie_campeonato = serie_campeonato
        self.times_selecionados = []
        self.titulo = "A" if int(serie_campeonato) == 1 else "B"

    def menu_inicial(self):
        print(f'A série selecionada é série {self.titulo}')
        # Adicionar os times selecionados
        for time, time_info in times.items():
            if time_info[0] == int(self.serie_campeonato):
                self.times_selecionados.append(time)

        time_escolhido = Time(self.times_selecionados)
        time_escolhido.criar_dictionary_de_times()


if __name__ == "__main__":
    print("Seja bem vindo ao Campeonato")
    resposta_incorreta = True
    while resposta_incorreta:
        serie = input("Escolha qual série do campeonato você quer jogar. Digite '1' para Série A, "
                              "'2' para Série B: ")
        try:
            if int(serie) == 1 or int(serie) == 2:
                resposta_incorreta = False
                jogo = Menu(serie)
                jogo.menu_inicial()

            else:
                print("Resposta inválida. Tente novamente")

        except ValueError:
            print("Somente números são aceitos. Tente novamente")