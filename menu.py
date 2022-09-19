from times_database import times
from times import Time

class Menu(object):
    def __init__(self, serie_campeonato):
        self.serie_campeonato = serie_campeonato
        self.times_selecionados = []
        self.titulo = "A" if serie_campeonato == 1 else "B"

    def menu_inicial_selecionar_times(self):
        print(f'A série selecionada é série {self.titulo}')
        # Adicionar os times selecionados
        for time, time_info in times.items():
            if time_info[0] == int(self.serie_campeonato):
                self.times_selecionados.append(time)

        time_escolhido = Time(self.times_selecionados)
        time_escolhido.criar_dictionary_de_times()

    def menu_inicial(self):
        print("Seja bem vindo ao Campeonato")
        resposta_incorreta = True
        while resposta_incorreta:
            try:
                opcao_escolhida = int(input("Pressione qualquer número para iniciar simulador ou 0 para encerrar: "))
                if opcao_escolhida == 0:
                    print("Até logo!! :)")
                    break
                serie = int(input("Escolha qual série do campeonato você quer jogar. Digite '1' para Série A, "
                                  "'2' para Série B: "))
                if serie == 1 or serie == 2:
                    resposta_incorreta = False
                    jogo = Menu(serie)
                    jogo.menu_inicial_selecionar_times()

                else:
                    print("Resposta inválida. Tente novamente")

            except ValueError:
                print("Somente números são aceitos. Tente novamente")


if __name__ == "__main__":
    Menu.menu_inicial(1)
