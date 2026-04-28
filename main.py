from prosessor import Prosessor
from grafikkort import Grafikkort
from ram import RAM
import funksjoner

import os 
os.system("cls")

# Lage objekter
p1 = Prosessor("Intel i5", 2000, "Intel", 6)
p2 = Prosessor("Ryzen 5", 2200, "AMD", 6)

g1 = Grafikkort("RTX 3050", 3000, "NVIDIA", 8)
g2 = Grafikkort("RX 6600", 2800, "AMD", 8)

r1 = RAM("Corsair", 800, "Corsair", 16)
r2 = RAM("Kingston", 700, "Kingston", 16)

komponenter = [p1, p2, g1, g2, r1, r2]


# Meny
valg = 0

while valg != 5:
    print("\n--- MENY ---")
    print("1. Vis alle komponenter")
    print("2. Filtrer etter pris")
    print("3. Oppdater pris")
    print("4. Vis dyreste komponent")
    print("5. Avslutt")

    valg = int(input("Velg: "))

    if valg == 1:
        funksjoner.vis_alle(komponenter)

    elif valg == 2:
        funksjoner.filtrer_pris(komponenter)

    elif valg == 3:
        funksjoner.oppdater_pris(komponenter)

    elif valg == 4:
        funksjoner.finn_dyreste(komponenter)

    elif valg == 5:
        print("Program avsluttet")

    else:
        print("Ugyldig valg")