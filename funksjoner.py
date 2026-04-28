# Funksjoner for menyen

def vis_alle(komponenter):
    print("\nAlle komponenter:\n")
    for k in komponenter:
        k.vis_komponent()


def filtrer_pris(komponenter):
    lav_pris = int(input("Laveste pris: "))
    maks_pris = int(input("Maksimal pris: "))

    print("\nResultat:\n")
    for k in komponenter:
        if lav_pris <= k.pris <= maks_pris:
            k.vis_komponent()


def finn_dyreste(komponenter):
    dyreste = komponenter[0]
    for k in komponenter:
        if k.pris > dyreste.pris:
            dyreste = k

    print("\nDyreste komponent:\n")
    dyreste.vis_komponent()


def oppdater_pris(komponenter):
    navn = input("Skriv navn på komponent: ")

    for k in komponenter:
        if k.navn.lower() == navn.lower():
            ny_pris = int(input("Ny pris: "))
            k.oppdater_pris(ny_pris)
            print("Pris oppdatert!")
            return

    print("Fant ikke komponent.")   