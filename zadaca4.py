"""4. Da se kreira programa koja ke bide za potrebide vo nekoja prodavnica."""
"""Da se kreira dictionary koj ke ima 2 indexi, produkti, ceni koi kkao podatoci ke imaat prazni listi. """
"""Koristnikot da moze da vnesuva produkti i ceni na produktite se dodeka ne izbere deka poveke ne saka da vnese."""
"""Koga ke prestane da vnesuva produkti da se presmeta kolku treba da plati i da se zacuva vo nov index."""
"""Da mu se dade opcija na korisnikot da plati, d a se presmeta dali treba da se vrati kusur ili ne."""
"""Ako treba da se zacuva vo dictionary kolku kusur treba da se vrati. Ako ne treba da se zacuva deka smetkata e platena"""



market = {}
produkt = input("Vnesete produkt koj bi sakale da go naracate: ")
cena = float(input("Vnesete cena koja bi ja platila za produktot: "))
market["produkt"] = produkt
market["cena"] = cena
plakjanje = float(input("Vnesete ja sumata sto ja plakjate: "))
if cena < plakjanje:
    kusur = plakjanje - cena
    print(f"Uspeshno plakjanje, vashiot kusur iznesuva {kusur} denari! ")
elif cena == plakjanje:
    print("Uspeshno plakjanje!")
else:
    print("Nemate dovolno sredstva!")

