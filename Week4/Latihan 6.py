gunting = 'gunting'
batu = 'batu'
kertas = 'kertas'
seri = 'seri'
Pilihan1 = input('Player 1 = ')
Pilihan2 = input('Player 2 = ')
if Pilihan1 == Pilihan2:
    print('Seri')
elif (Pilihan1 == 'gunting' and Pilihan2 == 'kertas') or \
     (Pilihan1 == 'batu' and Pilihan2 == 'gunting') or \
     (Pilihan1 == 'kertas' and Pilihan2 == 'batu'):
    print('Player 1 menang')
else:
    print('Player 2 menang')