from komponent import Komponent

class Prosessor(Komponent):
    def __init__(self, navn, pris, produsent, kjerner):
        super().__init__(navn, pris, produsent)
        self.kjerner = kjerner

    def vis_komponent(self):
        super().vis_komponent()
        print("Kjerner:", self.kjerner)
        print("------")