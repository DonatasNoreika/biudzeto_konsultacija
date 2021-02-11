
from modules.biudzetas import Biudzetas

biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input("Pasirinkite: \n1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - gauti balansą\n4 - parodyti ataskaitą\n5 - išeiti\n"))
    if pasirinkimas == 1:
        suma = float(input("Įveskite sumą\n"))
        siuntejas = input("Įveskite siuntėją\n")
        tipas = input("Įveskite tipą\n")
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, tipas)
    if pasirinkimas == 2:
        suma = float(input("Įveskite sumą\n"))
        apmokejimo_budas = input("Įveskite apmokėjimo būdą\n")
        preke_paslauga = input("Įveskite prekę/paslaugą\n")
        biudzetas.prideti_islaidu_irasa(suma, apmokejimo_budas, preke_paslauga)
    if pasirinkimas == 3:
        biudzetas.gauti_balansa()
    if pasirinkimas == 4:
        biudzetas.parodyti_ataskaita()
    if pasirinkimas == 5:
        print("Viso gero")
        break