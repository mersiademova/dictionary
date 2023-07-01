"""3. Da se kreira programa vo koja korisnikot ke moze da vnese strani na pravoagolnik,"""
"""da se vnesat vo dictionary, da se presmeta plostina i perimetar koja ke bide zacuvana vo dictinary."""
"""Da se proveri dali plostinata ili perimetarot se pogolemi"""


pravoagolnik = {}
a = int(input('Vnesete dimenzii na strana a: '))
b = int(input('Vnesete dimenzii na strana b: '))
pravoagolnik['a'] = a
pravoagolnik['b'] = b
P = pravoagolnik["a"] * pravoagolnik["b"]
L = 2*pravoagolnik['a'] + 2*pravoagolnik['b']
pravoagolnik['P'] = P
pravoagolnik['L'] = L
if P > L:
    print('Plostinata na pravoagolnikot e{} i e pogolema od perimetarot, koj e {}.'.format(P,L))
    pravoagolnik['Pogolem'] = P
else:
    pravoagolnik['Pogolem'] = L
    print('Perimetarot na pravoagolnikot e {} i e pogolem od plostinata, koja e {}.'.format(L,P))
print("Plostinata e: {} * {} = {}".format(pravoagolnik["a"],pravoagolnik["b"], P))
print("Perimetarot e: 2*{} + 2*{} = {}".format(pravoagolnik["a"], pravoagolnik['b'], L))
for i in pravoagolnik.items():
    print(i)


