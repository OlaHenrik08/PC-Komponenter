from komponent import Komponent

class RAM(Komponent):
    def __init__(self, navn, pris, produsent, kapasitet):
        super().__init__(navn, pris, produsent)
        self.kapasitet = kapasitet

    def vis_komponent(self):
        super().vis_komponent()
        print("Kapasitet:", self.kapasitet, "GB")
        print("------")