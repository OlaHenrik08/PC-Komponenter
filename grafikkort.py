from komponent import Komponent

class Grafikkort(Komponent):
    def __init__(self, navn, pris, produsent, minne):
        super().__init__(navn, pris, produsent)
        self.minne = minne

    def vis_komponent(self):
        super().vis_komponent()
        print("Minne:", self.minne, "GB")
        print("------")