#nyelvi szerkezetek

def ker_ter (a,b):
    k = 2 * a + 2 * b
    t = a * b
    print(f'kerulet: {k}')
    return k,t

felhasznalo_kora = int(input("Hány éves vagy: "))
if felhasznalo_kora >=18:
    print('Gyerek')
elif felhasznalo_kora <=25:
    print('ifjú')
elif felhasznalo_kora <=65:
    print('Koros')
else:
    print('Nyugger')

uzenet = 'Gyere Be' if felhasznalo_kora <=18 else 'Maradj kint'
print(uzenet)

i = 1
while i <10:
    i += 1
    if i==5:
        continue
    if i==5:
        break
    print(i)
else:
    print('gond nélkül lefutott')
print('vége a ciklusnak')

alap = 5
magassag = 3
ker_ter = (alap, magassag)
kerulet = ker_ter[0]
terulet = ker_ter[1]
print(f'kerulet =')