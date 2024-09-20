data = int(input("Masukkan jumlah angka = "))
total = 0

for i in range(data):
    total += int(input("Masukkan angka = "))

rata = total / data
print("Rata-rata = ", rata)
