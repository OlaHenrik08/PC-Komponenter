# Superklasse
class Komponent:
    def __init__(self, navn, pris, produsent):
        self.navn = navn
        self.pris = pris
        self.produsent = produsent

    def vis_komponent(self):
        print("Navn:", self.navn)
        print("Pris:", self.pris, "kr")
        print("Produsent:", self.produsent)

    def oppdater_pris(self, ny_pris):
        self.pris = ny_pris