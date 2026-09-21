# EZ a második labor feladatait tartalmazza
felhasznalo_kor = int(15.45)
felhasznalo_kor = input("Hány éves vagy: ")
felhasznalo_kor *= 2
felhasznalo_neve = 'Józsi'
felhasznalo_neve = input("Kérem a nevet: ")
felhasznalo_neve *= 2
jegyek = [2,5,4,3]
jegyek += [5]
del jegyek [0]
halmaz = {'magyar', 'angol', 'orosz', 3}
hallgato = {'nev': 'Jolán', "kor" : 19}
print(hallgato['nev'])
print(halmaz)
print('Szia',felhasznalo_neve[:-5],'!', felhasznalo_kor , jegyek)

print('Jó reggelt DUE')
print('Új sor\n'
      'kiírás\n'
      '!!!!!!!')
print(f'Szia .{felhasznalo_neve}! \n {jegyek}')
print(f'Kora: {felhasznalo_kor:30}')

print(felhasznalo_neve.rjust(30,'.'))
print(felhasznalo_neve.ljust(30,'.'))
print(felhasznalo_neve.ljust(30,'.'))
print(str(felhasznalo_kor).center(30))
