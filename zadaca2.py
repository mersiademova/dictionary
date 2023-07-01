"""2. Da se kreiara prazen dictionary, korisnikot da vnese 2 broevi koi ke se dodadt vo dictionary."""
"""Da se izvrsat 4te osnovni matematicki operacii i da se dodadat rezultatite vo dictionary vo razlicni keys"""



prazen_dict = {}
x = int(input ("Vnesete broj: "))
y = int(input  ("Vnesete uste eden broj: "))
prazen_dict['x'] = x
prazen_dict['y'] = y 
zbir = x + y
razlika = x - y
proizvod = x * y
kolicnik = x / y
prazen_dict ['zbir'] = x + y 
prazen_dict ['razlika'] = x - y 
prazen_dict ['proizvod'] = x * y 
prazen_dict ['kolicnik'] = x / y 
print(prazen_dict)


