#Vrať se k úkolu č. 4 z minulé lekce a zkus zpřehlednit kód použitím funkce. Funkce hod_kostkou bude vracet počet pokusů než hráči padla šestka.

from random import randrange

def hod_kostkou(): 
  """Funkce vraci pocet pokusu nez hraci
     padne sestka """
  hra_bezi = True
  pocet_hodu = 0
  print(f">>>Hazi hrac cislo {hod}<<<\n")
  while hra_bezi:
    hod_kostkou = randrange(1,7)
    pocet_hodu += 1
    print(f"Toto je {pocet_hodu} pokus")
    if hod_kostkou < 6:
      print(f"Padla Ti {hod_kostkou}")
    else: 
      hod_kostkou == 6
      hra_bezi = False
      print(f"Hodil jsi sestku na {pocet_hodu} pokus(u)\n")
      return pocet_hodu


nejvyssi_hod = 0
vitezny_hrac = 0

for hod in range(1,5):
  pocet_hodu = hod_kostkou() # funkci hod_kostkou() vlozime do promenne 
  if nejvyssi_hod < pocet_hodu:
    vitezny_hrac = hod
    nejvyssi_hod = pocet_hodu
print(f"\nVitezny hrac cislo {vitezny_hrac} hodil sestku na {nejvyssi_hod}pokusu")

