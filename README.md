# PC-Komponent Register

Et enkelt Python-program for å administrere og filtrere PC-komponenter via et tekstbasert menygrensesnitt.

## Beskrivelse

Programmet lar deg lagre informasjon om ulike PC-komponenter (prosessorer, grafikkort og RAM), og utføre enkle operasjoner som å vise, filtrere og oppdatere dem.

## Filstruktur

```
├── main.py          # Hovedprogram med meny og objekter
├── komponent.py     # Superklasse for alle komponenter
├── prosessor.py     # Subklasse for prosessorer
├── grafikkort.py    # Subklasse for grafikkort
├── ram.py           # Subklasse for RAM
└── funksjoner.py    # Hjelpefunksjoner for menyvalg
```

## Klassehierarki

```
Komponent  (superklasse)
├── Prosessor   – har antall kjerner
├── Grafikkort  – har minnestørrelse (GB)
└── RAM         – har kapasitet (GB)
```

## Funksjoner

| Menyvalg | Funksjon |
|----------|----------|
| 1 | Vis alle komponenter |
| 2 | Filtrer komponenter etter prisintervall |
| 3 | Oppdater prisen på en komponent |
| 4 | Vis den dyreste komponenten |
| 5 | Avslutt programmet |

## Kom i gang

Krever Python 3. Ingen eksterne avhengigheter.

```bash
python main.py
```

## Eksempel på kjøring

```
--- MENY ---
1. Vis alle komponenter
2. Filtrer etter pris
3. Oppdater pris
4. Vis dyreste komponent
5. Avslutt
Velg: 1

Alle komponenter:

Navn: Intel i5
Pris: 2000 kr
Produsent: Intel
Kjerner: 6
------
...
```